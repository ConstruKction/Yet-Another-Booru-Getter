import json


import requests

GELBOORU_API_URL_TEMPLATE = "https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&tags=%s&limit=%s"


class BooruRequest:
    def __init__(self, tags, count):
        self.api_url = GELBOORU_API_URL_TEMPLATE % (self.create_tags_string(tags), count)

    def get_json(self):
        return json.loads(requests.get(self.api_url).text)['post']

    @staticmethod
    def create_tags_string(tags):
        tags_string = ''
        for tag in tags:
            tags_string = f"{tags_string}{tag}+"

        return tags_string
