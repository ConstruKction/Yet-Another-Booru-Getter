import json
import logging
import time

import requests

DANBOORU_TAG_API_URL_TEMPLATE = "https://danbooru.donmai.us/tags.json?hide_empty=yes&search[order]=count&search[" \
                                "name_or_alias_matches]=%s"


class DanbooruTagRequest:
    def __init__(self, tag):
        self.tag = tag
        self.danbooru_tag_api_url = DANBOORU_TAG_API_URL_TEMPLATE % (tag)

    def get_json(self):
        default_count = 0
        return self.__get_json(default_count)

    def __get_json(self, count):
        count += 1

        response_json = json.loads(requests.get(self.danbooru_tag_api_url).text)
        if len(response_json) == 0:
            logging.error(f"No matches found for tag: {self.tag}.")
            return

        if 'success' in response_json:
            logging.info(f"Query timeout for tag: {self.tag}. Trying again..."
                         f"\nAttempt #{count}")

            time.sleep(1)

            return self.__get_json(count)

        return response_json[0]
