import json
import logging

import requests

from source_requests.request_interface import RequestInterface

SAFEBOORU_API_URL_TEMPLATE = "https://safebooru.org/index.php?page=dapi&s=post&q=index&json=1&tags=%s&limit=%s&pid=%s"


class SafebooruRequest(RequestInterface):
    def __init__(self, tags, count, page_number):
        self.page_number = page_number
        self.api_url = SAFEBOORU_API_URL_TEMPLATE % (self.create_tags_string(tags), count, self.page_number)

    def get_json(self):
        r = requests.get(self.api_url).text
        if len(r) == 0:
            logging.info("No more posts found. Finished.")
            return

        response_json = json.loads(r)
        if len(response_json) == 0:
            logging.info("No more posts found. Finished.")
            return

        return response_json

    @staticmethod
    def create_tags_string(tags):
        tags_string = ''
        for tag in tags:
            tags_string = f"{tags_string}{tag}+"

        return tags_string
