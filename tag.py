from exclusion import Exclusion
from tag_requests.danbooru_tag_request import DanbooruTagRequest


class Tag:
    def __init__(self, value, exclude):
        self.value = value
        self.exclude = exclude

    def __str__(self):
        if self.exclude == Exclusion.EXCLUDED:
            return f"-{self.value}"

        return f"{self.value}"

    def get_danbooru_tag_post_count(self):
        tag_request = DanbooruTagRequest(self.value)
        tag_request = tag_request.get_json()
        danbooru_tag_post_count = tag_request['post_count']

        return danbooru_tag_post_count
