import json
import logging

import requests

from src.source_requests.request_interface import RequestInterface

ATF_API_URL_TEMPLATE = "https://booru.allthefallen.moe/posts.json?tags=%s&limit=%s&page=%s"


class ATFRequest(RequestInterface):
    def __init__(self, tags, count, page_number):
        self.page_number = page_number
        self.api_url = ATF_API_URL_TEMPLATE % (self.create_tags_string(tags), count, self.page_number)

    def get_json(self):
        response_json = json.loads(requests.get(self.api_url).text)
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
