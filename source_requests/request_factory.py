import logging

from source_requests.atf_request import ATFRequest
from source_requests.danbooru_request import DanbooruRequest
from source_requests.gelbooru_request import GelbooruRequest
from source_requests.konachan_request import KonachanRequest
from source_requests.lolibooru_request import LolibooruRequest
from source_requests.safebooru_request import SafebooruRequest
from source_requests.yandere_request import YandereRequest
from source_requests.zerochan_request import ZerochanRequest


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
        elif source_name == 'lolibooru':
            return LolibooruRequest
        elif source_name == 'zerochan':
            return ZerochanRequest
        elif source_name == 'atf':
            return ATFRequest
        else:
            return logging.error(f"Unsupported source: {source_name}!")

    @staticmethod
    def get_default_first_page(source_name):
        if source_name == 'gelbooru':
            return 0
        elif source_name == 'danbooru':
            return 1
        elif source_name == 'konachan':
            return 1
        elif source_name == 'safebooru':
            return 0
        elif source_name == 'yandere' or source_name == 'yande.re':
            return 1
        elif source_name == 'lolibooru':
            return 1
        elif source_name == 'zerochan':
            return 1
        elif source_name == 'atf':
            return 1
        else:
            return 0
