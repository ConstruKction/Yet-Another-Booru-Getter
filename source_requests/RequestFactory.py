import logging

from source_requests.DanbooruRequest import DanbooruRequest
from source_requests.GelbooruRequest import GelbooruRequest
from source_requests.KonachanRequest import KonachanRequest
from source_requests.SafebooruRequest import SafebooruRequest
from source_requests.YandereRequest import YandereRequest


class RequestFactory:
    @staticmethod
    def get_request(source_name):
        if source_name == 'gelbooru':
            return GelbooruRequest
        elif source_name == 'danbooru':
            return DanbooruRequest
        elif source_name == 'konachan':
            return KonachanRequest
        elif source_name == 'safebooru':
            return SafebooruRequest
        elif source_name == 'yandere' or source_name == 'yande.re':
            return YandereRequest
        else:
            return logging.error(f"Unsupported source: {source_name}!")
