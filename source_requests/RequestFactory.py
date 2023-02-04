import logging

from source_requests.DanbooruRequest import DanbooruRequest
from source_requests.GelbooruRequest import GelbooruRequest
from source_requests.KonachanRequest import KonachanRequest


class RequestFactory:
    @staticmethod
    def get_request(source_name):
        if source_name == 'gelbooru':
            return GelbooruRequest
        elif source_name == 'danbooru':
            return DanbooruRequest
        elif source_name == 'konachan':
            return KonachanRequest
        else:
            return logging.error(f"Unsupported source: {source_name}!")
