import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

from arg_parser import ArgParser
from booru_requests.request_factory import RequestFactory
from booru_requests.request_interface import RequestInterface
from exclusion import Exclusion
from images.image_factory import ImageFactory
from images.local_image import LocalImage
from tag_requests.tag import Tag

ILLEGAL_CHARACTERS = '<>:"/\\|?*.'
DATE = datetime.now().strftime('%Y_%m_%d')

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


def get_local_files(directory_path: str) -> list[LocalImage]:
    filepath_list = []
    files = os.listdir(directory_path)
    for file in files:
        filepath_list.append(LocalImage(f"{directory_path}/{file}"))
    return filepath_list


def print_filename_exists_message(booru_image_filename: str, local_image_filename: str):
    if booru_image_filename != local_image_filename:
        logging.info(f"{booru_image_filename} exists as {local_image_filename}")
    else:
        logging.info(f"{booru_image_filename} exists")


def create_tag_object_list(tags_string: str, exclude: Exclusion) -> list[Tag]:
    tag_object_list = []
    if tags_string is None:
        return tag_object_list

    for tag_value in tags_string.split(","):
        tag_object = Tag(tag_value, exclude)
        tag_object_list.append(tag_object)

    return tag_object_list


def sanitize(string: str) -> str:
    if 'None' in string:
        return string.replace('_None', '')

    for illegal_character in ILLEGAL_CHARACTERS:
        if illegal_character in string:
            return DATE

    return string.replace(',', '_')


def new_request(tags: str,
                exclude_tags: str,
                count: int,
                target_dir_path: str,
                booru_name: str,
                increment_num: int) -> Optional[RequestInterface]:
    request_factory = RequestFactory()
    request_object = request_factory.get_request(booru_name)

    page_number = request_factory.get_default_first_page(booru_name)

    if args.all:
        page_number += increment_num

    if not request_object:
        return

    tags = create_tag_object_list(tags, Exclusion.INCLUDED) + create_tag_object_list(exclude_tags, Exclusion.EXCLUDED)

    request = request_object(tags, count, page_number)

    local_images = get_local_files(target_dir_path)

    r = request.get_json()
    if r is None:
        return
    for json_object in r:
        image_factory = ImageFactory()
        image_object = image_factory.get_image(booru_name)

        if not image_object:
            return

        image = image_object(json_object)

        image.safety_rating = image_factory.get_safety_rating(booru_name, image.safety_rating)

        file_found = False

        if not image.hash:
            logging.error(f"{image.filename} MD5 hash not found.")
            continue

        for local_image in local_images:
            if local_image.hash == image.hash:
                print_filename_exists_message(image.filename, local_image.filename)
                file_found = True

        if file_found:
            continue

        if args.safe_for_work and image.safety_rating == 'nsfw':
            logging.info(f"Image {image.filename} is NSFW -> skipping")
            continue

        if args.not_safe_for_work and image.safety_rating == 'sfw':
            logging.info(f"Image {image.filename} is SFW -> skipping")
            continue

        image.download(target_dir_path, tags)

        if args.log:
            image.log_metadata(target_dir_path)

    return request


def process_boorus(boorus, tags, exclude, count, directory_path, all_requests):
    for booru in boorus:
        logging.info(f"Processing source: {booru}.")
        increment = 0

        if all_requests:
            while new_request(tags, exclude, count, directory_path, booru, increment) is not None:
                increment += 1
        else:
            new_request(tags, exclude, count, directory_path, booru, increment)

        logging.info(f"Finished processing source: {booru}.")


if __name__ == "__main__":
    arg_parser = ArgParser()
    args = arg_parser.parse_args()

    if len(sys.argv) == 1:
        args.print_help(sys.stderr)
        sys.exit()

    if not args.boorus:
        logging.error("Need at least one booru (e.g. -s gelbooru)")
        sys.exit()

    if args.safe_for_work and args.not_safe_for_work:
        logging.error("Both SFW and NSFW arguments used! Please pick only one or neither.")
        sys.exit()

    if args.safe_for_work:
        logging.info("SFW Mode Enabled")

    if args.not_safe_for_work:
        logging.info("NSFW Mode Enabled")

    if args.log:
        logging.info("Logging metadata enabled.")

    increment_number = 0
    target_directory_name = sanitize(f"{args.tags}")
    target_directory_path = f"{Path().resolve()}/{target_directory_name}"

    if Path(target_directory_name).exists():
        logging.info(f"{target_directory_name} directory exists. Storing there.")
    else:
        os.makedirs(target_directory_name)
        logging.info(f"Created directory {target_directory_name}.")

    process_boorus(args.boorus, args.tags, args.exclude, args.count, target_directory_path, args.all)