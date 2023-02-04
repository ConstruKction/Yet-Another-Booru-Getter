from ImageDownloader import ImageDownloader
from MetadataLogger import MetadataLogger
from images.ImageInterface import ImageInterface


class DanbooruImage(ImageInterface):
    def __init__(self, json_dict):
        self.id_image = json_dict.get('id')
        self.url = json_dict.get('large_file_url')
        self.hash = json_dict.get('md5')
        self.tags = json_dict.get('tag_string')
        self.source = json_dict.get('source')
        self.artists = json_dict.get('tag_string_artist')
        self.rating = json_dict.get('rating')
        self.width = json_dict.get('image_width')
        self.height = json_dict.get('image_height')
        self.extension = json_dict.get('file_ext')
        self.filename = f"{self.id_image}.{self.extension}"

    def download(self, path):
        filepath = f"{path}/{self.filename}"
        image_downloader = ImageDownloader(self.url, filepath, self.filename)
        image_downloader.download()

    def get_metadata(self):
        metadata_items = [
            f"url: {self.url}",
            f"md5: {self.hash}",
            f"tags: {self.tags.replace(' ', ',')}",
            f"source: {self.source}",
            f"artists: {self.artists.replace(' ', ',')}",
            f"rating: {self.rating}",
            f"width: {self.width}",
            f"height: {self.height}",
            f"extension: {self.extension}"
        ]
        return metadata_items

    def log_metadata(self, path):
        metadata_logger = MetadataLogger(path, self.id_image, self.filename, self.get_metadata())
        metadata_logger.log_metadata()
