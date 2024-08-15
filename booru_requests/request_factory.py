import logging
from typing import Type, Union

from booru_requests.atf_request import ATFRequest
from booru_requests.danbooru_request import DanbooruRequest
from booru_requests.gelbooru_request import GelbooruRequest
from booru_requests.konachan_request import KonachanRequest
from booru_requests.request_interface import RequestInterface
from booru_requests.safebooru_request import SafebooruRequest
from booru_requests.yandere_request import YandereRequest
from booru_requests.zerochan_request import ZerochanRequest


class RequestFactory:
    @staticmethod
    def get_request(booru_name: str) -> Union[Type[RequestInterface], None]:
        if booru_name == 'gelbooru':
            return GelbooruRequest
        elif booru_name == 'danbooru':
            return DanbooruRequest
        elif booru_name == 'konachan':
            return KonachanRequest
        elif booru_name == 'safebooru':
            return SafebooruRequest
        elif booru_name == 'yandere' or booru_name == 'yande.re':
            return YandereRequest
        elif booru_name == 'zerochan':
            return ZerochanRequest
        elif booru_name == 'atf':
            return ATFRequest
        else:
            return logging.error(f"Unsupported source: {booru_name}!")

    @staticmethod
    def get_default_first_page(booru_name: str) -> Union[int, None]:
        if booru_name == 'gelbooru':
            return 0
        elif booru_name == 'danbooru':
            return 1
        elif booru_name == 'konachan':
            return 1
        elif booru_name == 'safebooru':
            return 0
        elif booru_name == 'yandere' or booru_name == 'yande.re':
            return 1
        elif booru_name == 'zerochan':
            return 1
        elif booru_name == 'atf':
            return 1
        else:
            return logging.error(f"Can't get the default first page value for {booru_name}!")
