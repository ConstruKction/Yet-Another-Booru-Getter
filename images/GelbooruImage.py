import re
from datetime import datetime

from ImageDownloader import ImageDownloader
from images.ImageInterface import ImageInterface

FILE_EXTENSION_RE = re.compile(".*\\.(\\w+)")
DATE = datetime.now().strftime('%Y_%m_%d')


class GelbooruImage(ImageInterface):
    def __init__(self, json_dict):
        self.id_image = json_dict.get('id')
        self.url = json_dict.get('file_url')
        self.hash = json_dict.get('md5')
        self.tags = json_dict.get('tags')
        self.extension = re.search(FILE_EXTENSION_RE, self.url).group(1)
        self.filename = f"{self.id_image}.{self.extension}"

    def download(self, path):
        filepath = f"{path}/{self.filename}"
        image_downloader = ImageDownloader(self.url, filepath, self.filename)
        image_downloader.download()

    def log_metadata(self, path):
        tags = self.tags.replace(" ", ", ")
        log_file_name = f"{self.id_image}.txt"
        filepath = f"{path}/{log_file_name}"

        with open(filepath, 'w') as f:
            f.write(f"{self.filename} {tags}\n")
            f.close()
