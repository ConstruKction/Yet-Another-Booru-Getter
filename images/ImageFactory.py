from images.DanbooruImage import DanbooruImage
from images.GelbooruImage import GelbooruImage
from images.KonachanImage import KonachanImage
from images.LolibooruImage import LolibooruImage
from images.SafebooruImage import SafebooruImage
from images.YandereImage import YandereImage

GELBOORU_NSFW_RATINGS = ['explicit, questionable, sensitive']
DANBOORU_NSFW_RATINGS = ['e, q, s']
KONACHAN_NSFW_RATINGS = ['e, q']
LOLIBOORU_NSFW_RATINGS = ['e, q']
SAFEBOORU_NSFW_RATINGS = ['questionable']
YANDERE_NSFW_RATINGS = ['e, q']


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
        else:
            return
