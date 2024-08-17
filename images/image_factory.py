import logging
from typing import Union, Type

from images.atf_image import ATFImage
from images.danbooru_image import DanbooruImage
from images.gelbooru_image import GelbooruImage
from images.image_interface import ImageInterface
from images.konachan_image import KonachanImage
from images.safebooru_image import SafebooruImage
from images.yandere_image import YandereImage
from images.zerochan_image import ZerochanImage

GELBOORU_NSFW_RATINGS = ['explicit', 'questionable', 'sensitive']
DANBOORU_NSFW_RATINGS = ['e', 'q', 's']
KONACHAN_NSFW_RATINGS = ['e', 'q']
SAFEBOORU_NSFW_RATINGS = ['questionable']
YANDERE_NSFW_RATINGS = ['e', 'q']
ATF_NSFW_RATINGS = ['e', 'q']


class ImageFactory:
    @staticmethod
    def get_image(booru_name: str) -> Union[Type[ImageInterface], None]:
        if booru_name == 'gelbooru':
            return GelbooruImage
        elif booru_name == 'danbooru':
            return DanbooruImage
        elif booru_name == 'konachan':
            return KonachanImage
        elif booru_name == 'safebooru':
            return SafebooruImage
        elif booru_name == 'yandere' or booru_name == 'yande.re':
            return YandereImage
        elif booru_name == 'zerochan':
            return ZerochanImage
        elif booru_name == 'atf':
            return ATFImage
        else:
            return logging.error(f"Couldn't link Image Object to source: '{booru_name}'.")

    @staticmethod
    def get_safety_rating(booru_name: str, safety_rating: str) -> Union[str, None]:
        if booru_name == 'gelbooru':
            return 'sfw' if safety_rating not in GELBOORU_NSFW_RATINGS else 'nsfw'
        elif booru_name == 'danbooru':
            return 'sfw' if safety_rating not in DANBOORU_NSFW_RATINGS else 'nsfw'
        elif booru_name == 'konachan':
            return 'sfw' if safety_rating not in KONACHAN_NSFW_RATINGS else 'nsfw'
        elif booru_name == 'safebooru':
            return 'sfw' if safety_rating not in SAFEBOORU_NSFW_RATINGS else 'nsfw'
        elif booru_name == 'yandere' or booru_name == 'yande.re':
            return 'sfw' if safety_rating not in YANDERE_NSFW_RATINGS else 'nsfw'
        elif booru_name == 'zerochan':
            return 'sfw'
        elif booru_name == 'atf':
            return 'sfw' if safety_rating not in ATF_NSFW_RATINGS else 'nsfw'
        else:
            return logging.error(f"Couldn't determine safety rating for: {booru_name}")
