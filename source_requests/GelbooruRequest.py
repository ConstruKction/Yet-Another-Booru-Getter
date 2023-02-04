import json
import logging

import requests

from source_requests.RequestInterface import RequestInterface

GELBOORU_API_URL_TEMPLATE = "https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&tags=%s&limit=%s&pid=%s"


class GelbooruRequest(RequestInterface):
    def __init__(self, tags, count, page_number):
        self.page_number = page_number
        self.api_url = GELBOORU_API_URL_TEMPLATE % (self.create_tags_string(tags), count, self.page_number)

    def get_json(self):
        response_json = json.loads(requests.get(self.api_url).text)
        if 'post' not in response_json:
            logging.info("No more posts found. Finished.")
            return

        return response_json['post']

    @staticmethod
    def create_tags_string(tags):
        tags_string = ''
        for tag in tags:
            tags_string = f"{tags_string}{tag}+"

        return tags_string
