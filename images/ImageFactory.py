from images.DanbooruImage import DanbooruImage
from images.GelbooruImage import GelbooruImage


class ImageFactory:
    @staticmethod
    def get_image(source_name):
        if source_name == 'gelbooru':
            return GelbooruImage
        elif source_name == 'danbooru':
            return DanbooruImage
        else:
            raise ValueError()
