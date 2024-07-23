import re

from image_downloader import ImageDownloader
from images.image_interface import ImageInterface
from metadata_logger import MetadataLogger

FILE_EXTENSION_RE = re.compile(".*\\.(\\w+)")


class GelbooruImage(ImageInterface):
    def __init__(self, json_dict):
        self.id_image = json_dict.get('id')
        self.url = json_dict.get('file_url')
        self.hash = json_dict.get('md5')
        self.tags = json_dict.get('tags')
        self.source = json_dict.get('source')
        self.rating = json_dict.get('rating')
        self.width = json_dict.get('width')
        self.height = json_dict.get('height')
        self.extension = re.search(FILE_EXTENSION_RE, self.url).group(1)
        self.filename = f"{self.id_image}.{self.extension}"

    def download(self, path, tags):
        filepath = f"{path}/{self.filename}"
        image_downloader = ImageDownloader(self.url, filepath, self.filename)
        image_downloader.download()

    def get_metadata(self):
        metadata_items = [
            f"url: {self.url}",
            f"md5: {self.hash}",
            f"tags: {self.tags.replace(' ', ',')}",
            f"source: {self.source}",
            f"rating: {self.rating}",
            f"width: {self.width}",
            f"height: {self.height}",
            f"extension: {self.extension}"
        ]
        return metadata_items

    def log_metadata(self, path):
        metadata_logger = MetadataLogger(path, self.id_image, self.filename, self.get_metadata())
        metadata_logger.log_metadata()
