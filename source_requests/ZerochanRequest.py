import json
import logging
import re

import requests
from fake_useragent import UserAgent

from source_requests.RequestInterface import RequestInterface
from users.ZerochanUser import ZerochanUser

ZEROCHAN_API_URL_TEMPLATE = "https://www.zerochan.net/%s?l=%s&json&p=%s&s=id"
ZEROCHAN_API_HTML_RE = re.compile("<.+>", flags=re.S)


class ZerochanRequest(RequestInterface):
    def __init__(self, tags, count, page_number):
        self.page_number = page_number
        self.api_url = ZEROCHAN_API_URL_TEMPLATE % (self.create_tags_string(tags), count, self.page_number)

    def get_json(self):
        zerochan_user = ZerochanUser()
        z_id = zerochan_user.z_id
        z_hash = zerochan_user.z_hash

        user_agent = UserAgent()
        headers = {
            'user-agent': user_agent.chrome
        }
        cookies = {
            'z_id': z_id,
            'z_hash': z_hash,
            'PHPSESSID': self.get_session_id(self.api_url)
        }

        response_json = requests.get(self.api_url, headers=headers, cookies=cookies).text

        if 'div' in response_json:
            response_json = ZerochanRequest.clean_json(response_json)

        response_json = json.loads(response_json)

        if 'items' not in response_json:
            logging.info("No more posts found. Finished.")
            return

        return response_json['items']

    @staticmethod
    def create_tags_string(tags):
        tags_string = ''
        for tag in tags:
            tags_string = f"{tags_string}{tag},"

        return tags_string

    @staticmethod
    def clean_json(dirty_json):
        clean_json = re.sub(ZEROCHAN_API_HTML_RE, '', dirty_json)
        return clean_json

    @staticmethod
    def get_session_id(api_url):
        user_agent = UserAgent()

        session = requests.Session()
        session.headers = {'user-agent': user_agent.chrome}
        session_id = session.get(api_url, headers={'user-agent': user_agent.chrome}).cookies.get('PHPSESSID')

        return session_id
