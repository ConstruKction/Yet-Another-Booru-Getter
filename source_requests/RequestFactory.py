from source_requests.DanbooruRequest import DanbooruRequest
from source_requests.GelbooruRequest import GelbooruRequest


class RequestFactory:
    @staticmethod
    def get_request(source_name):
        if source_name == 'gelbooru':
            return GelbooruRequest
        elif source_name == 'danbooru':
            return DanbooruRequest
        else:
            raise ValueError()
