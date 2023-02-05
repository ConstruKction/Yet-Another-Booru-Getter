import argparse
import logging
import os
import pathlib
import sys
from datetime import datetime

from Exclusion import Exclusion
from SplitArguments import SplitArguments
from Tag import Tag
from images.ImageFactory import ImageFactory
from images.LocalImage import LocalImage
from source_requests.RequestFactory import RequestFactory

ILLEGAL_CHARACTERS = '<>:"/\\|?*.'
DATE = datetime.now().strftime('%Y_%m_%d')

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


def get_local_files(directory_path):
    filepath_list = []
    files = os.listdir(directory_path)
    for file in files:
        filepath_list.append(LocalImage(f"{directory_path}/{file}"))
    return filepath_list


def print_filename_exists_message(booru_image_filename, local_image_filename):
    if booru_image_filename != local_image_filename:
        logging.info(f"{booru_image_filename} exists as {local_image_filename}")
    else:
        logging.info(f"{booru_image_filename} exists")


def create_tag_object_list(tags_string, exclude):
    tag_object_list = []
    if tags_string is None:
        return tag_object_list

    for tag_value in tags_string.split(","):
        tag_object = Tag(tag_value, exclude)
        tag_object_list.append(tag_object)

    return tag_object_list


def sanitize(string):
    if 'None' in string:
        return string.replace('_None', '')

    for illegal_character in ILLEGAL_CHARACTERS:
        if illegal_character in string:
            return DATE

    return string.replace(',', '_')


def new_request(tags, exclude_tags, count, target_directory_path, source, increment_number):
    request_factory = RequestFactory()
    request_object = request_factory.get_request(source)

    page_number = request_factory.get_default_first_page(source)

    if args.all:
        page_number += increment_number

    if not request_object:
        return

    tags = create_tag_object_list(tags, Exclusion.INCLUDED) + create_tag_object_list(exclude_tags, Exclusion.EXCLUDED)

    request = request_object(tags, count, page_number)

    local_images = get_local_files(target_directory_path)

    r = request.get_json()
    if r is None:
        return
    for json_object in r:
        image_factory = ImageFactory()
        image_object = image_factory.get_image(source)

        if not image_object:
            return

        image = image_object(json_object)

        image.rating = image_factory.get_safety_rating(source, image.rating)

        file_found = False

        for local_image in local_images:
            if local_image.hash == image.hash:
                print_filename_exists_message(image.filename, local_image.filename)
                file_found = True

        if file_found:
            continue

        if args.safe_for_work and image.rating == 'nsfw':
            logging.info(f"Image {image.filename} is NSFW -> skipping")
            continue

        if args.not_safe_for_work and image.rating == 'sfw':
            logging.info(f"Image {image.filename} is SFW -> skipping")
            continue

        image.download(target_directory_path, tags)

        if args.log:
            image.log_metadata(target_directory_path)

    return request


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tags', help='tags split by a comma (e.g. cute,vanilla)')
    parser.add_argument('-e', '--exclude', help='tags to exclude split by a comma')
    parser.add_argument('-c', '--count', help='amount of images desired, max 100', default=10, type=int)
    parser.add_argument('-l', '--log', help='log filenames with their respective tags in a txt file', default=False,
                        action=argparse.BooleanOptionalAction)
    parser.add_argument('-a', '--all', help='download ALL images with specified tags', default=False,
                        action=argparse.BooleanOptionalAction)
    parser.add_argument('-s', '--sources', help='specify sources from which to download (e.g. -s gelbooru,danbooru)',
                        action=SplitArguments)
    parser.add_argument('-sfw', '--safe-for-work', help='download only sfw images', default=False,
                        action=argparse.BooleanOptionalAction)
    parser.add_argument('-nsfw', '--not-safe-for-work', help='download only nsfw images', default=False,
                        action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit()

    if args.safe_for_work and args.not_safe_for_work:
        logging.error("Both SFW and NSFW arguments found. Please pick only one or neither.")
        sys.exit()

    if args.safe_for_work:
        logging.info("SFW Mode Enabled")

    if args.not_safe_for_work:
        logging.info("NSFW Mode Enabled")

    if args.log:
        logging.info("Logging metadata enabled.")

    increment_number = 0
    target_directory_name = sanitize(f"{DATE}_{args.tags}")
    target_directory_path = f"{pathlib.Path().resolve()}/{target_directory_name}"

    if pathlib.Path(target_directory_name).exists():
        logging.info(f"{target_directory_name} directory exists. Storing there.")
    else:
        os.makedirs(target_directory_name)
        logging.info(f"Created directory {target_directory_name}.")

    for source in args.sources:
        logging.info(f"Current source: {source}.")

        if not args.all:
            new_request(args.tags, args.exclude, args.count, target_directory_path, source, increment_number)
        else:
            while True:
                if (new_request(args.tags, args.exclude, args.count, target_directory_path, source,
                                increment_number) is None):
                    break
                increment_number += 1
