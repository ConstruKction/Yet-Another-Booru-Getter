import re

from src.image_downloader import ImageDownloader
from src.metadata_logger import MetadataLogger
from src.images.image_interface import ImageInterface

FILE_EXTENSION_RE = re.compile(".*\\.(\\w+)")
SAFEBOORU_IMAGE_URL_TEMPLATE = "https://safebooru.org/images/%s"


class SafebooruImage(ImageInterface):
    def __init__(self, json_dict):
        self.id_image = json_dict.get('id')
        self.directory = json_dict.get('directory')
        self.image = json_dict.get('image')
        self.hash = json_dict.get('hash')
        self.tags = json_dict.get('tags')
        self.rating = json_dict.get('rating')
        self.width = json_dict.get('width')
        self.height = json_dict.get('height')
        self.image_location = f"{self.directory}/{self.image}"
        self.url = SAFEBOORU_IMAGE_URL_TEMPLATE % (self.image_location)
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
            f"rating: {self.rating}",
            f"width: {self.width}",
            f"height: {self.height}",
            f"extension: {self.extension}"
        ]
        return metadata_items

    def log_metadata(self, path):
        metadata_logger = MetadataLogger(path, self.id_image, self.filename, self.get_metadata())
        metadata_logger.log_metadata()
