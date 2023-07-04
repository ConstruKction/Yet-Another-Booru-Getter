from src.images.atf_image import ATFImage
from src.images.danbooru_image import DanbooruImage
from src.images.gelbooru_image import GelbooruImage
from src.images.konachan_image import KonachanImage
from src.images.lolibooru_image import LolibooruImage
from src.images.safebooru_image import SafebooruImage
from src.images.yandere_image import YandereImage
from src.images.zerochan_image import ZerochanImage

GELBOORU_NSFW_RATINGS = ['explicit', 'questionable', 'sensitive']
DANBOORU_NSFW_RATINGS = ['e', 'q', 's']
KONACHAN_NSFW_RATINGS = ['e', 'q']
LOLIBOORU_NSFW_RATINGS = ['e', 'q']
SAFEBOORU_NSFW_RATINGS = ['questionable']
YANDERE_NSFW_RATINGS = ['e', 'q']
ATF_NSFW_RATINGS = ['e', 'q']


class ImageFactory:
    @staticmethod
    def get_image(source_name):
        if source_name == 'gelbooru':
            return GelbooruImage
        elif source_name == 'danbooru':
            return DanbooruImage
        elif source_name == 'konachan':
            return KonachanImage
        elif source_name == 'safebooru':
            return SafebooruImage
        elif source_name == 'yandere' or source_name == 'yande.re':
            return YandereImage
        elif source_name == 'lolibooru':
            return LolibooruImage
        elif source_name == 'zerochan':
            return ZerochanImage
        elif source_name == 'atf':
            return ATFImage
        else:
            return

    @staticmethod
    def get_safety_rating(source_name, rating):
        if source_name == 'gelbooru':
            return 'sfw' if rating not in GELBOORU_NSFW_RATINGS else 'nsfw'
        elif source_name == 'danbooru':
            return 'sfw' if rating not in DANBOORU_NSFW_RATINGS else 'nsfw'
        elif source_name == 'konachan':
            return 'sfw' if rating not in KONACHAN_NSFW_RATINGS else 'nsfw'
        elif source_name == 'safebooru':
            return 'sfw' if rating not in SAFEBOORU_NSFW_RATINGS else 'nsfw'
        elif source_name == 'yandere' or source_name == 'yande.re':
            return 'sfw' if rating not in YANDERE_NSFW_RATINGS else 'nsfw'
        elif source_name == 'lolibooru':
            return 'sfw' if rating not in LOLIBOORU_NSFW_RATINGS else 'nsfw'
        elif source_name == 'zerochan':
            return 'sfw'
        elif source_name == 'atf':
            return 'sfw' if rating not in ATF_NSFW_RATINGS else 'nsfw'
        else:
            return
