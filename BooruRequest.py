import json


import requests

GELBOORU_API_URL_TEMPLATE = "https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&tags=%s&limit=%s&pid=%s"


class BooruRequest:
    def __init__(self, tags, count, page_number):
        self.page_number = page_number
        self.api_url = GELBOORU_API_URL_TEMPLATE % (self.create_tags_string(tags), count, self.page_number)

    def get_json(self):
        try:
            return json.loads(requests.get(self.api_url).text)['post']
        except requests.exceptions.RequestException as e:
            if e is not KeyError:
                raise SystemExit(e)

            raise SystemExit("No more posts found. Finished.")

    @staticmethod
    def create_tags_string(tags):
        tags_string = ''
        for tag in tags:
            tags_string = f"{tags_string}{tag}+"

        return tags_string
