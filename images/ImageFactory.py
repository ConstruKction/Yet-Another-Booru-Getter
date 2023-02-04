from images.DanbooruImage import DanbooruImage
from images.GelbooruImage import GelbooruImage
from images.KonachanImage import KonachanImage
from images.SafebooruImage import SafebooruImage
from images.YandereImage import YandereImage


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
        else:
            return
