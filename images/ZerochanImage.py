import json
import logging
import re
from time import sleep

import requests
from fake_useragent import UserAgent

from ImageDownloader import ImageDownloader
from MetadataLogger import MetadataLogger
from images.ImageInterface import ImageInterface

FILE_EXTENSION_RE = re.compile(".*\\.(\\w+)")
ZEROCHAN_IMAGE_DETAILS_API_URL_TEMPLATE = "https://www.zerochan.net/%s?json"


class ZerochanImage(ImageInterface):
    def __init__(self, json_dict):
        self.id_image = json_dict.get('id')
        self.tags = json_dict.get('tags')
        self.image_details = self.get_image_details()
        self.hash = self.image_details.get('hash')
        self.source = self.image_details.get('source')
        self.rating = 'nsfw' if self.is_nsfw() else 'sfw'
        self.url = self.image_details.get('full')
        self.width = self.image_details.get('width')
        self.height = self.image_details.get('height')
        self.extension = re.search(FILE_EXTENSION_RE, self.url).group(1)
        self.filename = f"{self.id_image}.{self.extension}"

    def download(self, path, tags):
        filepath = f"{path}/{self.filename}"
        image_downloader = ImageDownloader(self.url, filepath, self.filename)
        image_downloader.download()

    def get_image_details(self):
        user_agent = UserAgent()
        headers = {'user-agent': user_agent.chrome}

        image_detail_page_request = requests.get((ZEROCHAN_IMAGE_DETAILS_API_URL_TEMPLATE % self.id_image),
                                                 headers=headers).text

        if 'full' not in image_detail_page_request:
            logging.error(f"Can't get image details -> skipping")
            return

        image_detail_page = json.loads(image_detail_page_request)

        sleep(2)

        return image_detail_page

    def get_metadata(self):
        metadata_items = [
            f"url: {self.url}",
            f"md5: {self.hash}",
            f"tags: {self.tags}",
            f"source: {self.source}",
            f"rating: {self.rating}",
            f"width: {self.width}",
            f"height: {self.height}",
            f"extension: {self.extension}"
        ]
        return metadata_items

    def log_metadata(self, path):
        metadata_logger = MetadataLogger(path, self.id_image, self.filename, self.get_metadata())
        metadata_logger.log_metadata()

    def is_nsfw(self):
        if 'Not Safe for Work' in self.tags:
            return True
