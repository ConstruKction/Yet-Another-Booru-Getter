import json
import logging
from typing import Optional

import requests

from booru_requests.request_interface import RequestInterface
from tag_requests.tag import Tag

YANDERE_API_URL_TEMPLATE = "https://yande.re/post.json?tags=%s&limit=%s&page=%s"


class YandereRequest(RequestInterface):
    def __init__(self, tags: list[Tag], count: int, page_number: int):
        self.page_number = page_number
        self.api_url = YANDERE_API_URL_TEMPLATE % (self.create_tags_string(tags), count, self.page_number)

    def get_json(self) -> Optional[dict]:
        response_json = json.loads(requests.get(self.api_url).text)
        if len(response_json) == 0:
            logging.info("No more posts found. Finished.")
            return

        return response_json

    def create_tags_string(self, tags: list[Tag]) -> str:
        tags_string = ''
        for tag in tags:
            tags_string = f"{tags_string}{tag}+"

        return tags_string
