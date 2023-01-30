import re
import logging
from http import HTTPStatus
from datetime import datetime

import requests
from tqdm import tqdm

FILE_EXTENSION_RE = re.compile(".*\\.(\\w+)")
DATE = datetime.now().strftime('%Y_%m_%d')


class BooruImage:
    def __init__(self, json_dict):
        self.id_image = json_dict.get('id')
        self.url = json_dict.get('file_url')
        self.hash = json_dict.get('hash')
        self.tags = json_dict.get('tags')
        self.extension = re.search(FILE_EXTENSION_RE, self.url).group(1)
        self.filename = f"{self.id_image}.{self.extension}"

    def download(self, path):
        response = requests.get(self.url, stream=True)
        expected_size = int(response.headers.get('content-length', 0))
        progress_bar = tqdm(total=expected_size, unit='B', unit_scale=True, desc=self.filename)

        if response.status_code != HTTPStatus.OK:
            logging.error(response.status_code)
            return

        filepath = f"{path}/{self.filename}"

        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    progress_bar.update(len(chunk))
                    f.write(chunk)
                    f.flush()

        progress_bar.close()

        if expected_size != 0 and progress_bar.n != expected_size:
            logging.error(f"Something went wrong while storing {self.filename}")

    def log_metadata(self, path):
        tags = self.tags.replace(" ", ",")
        log_file_name = f"{self.id_image}.txt"
        filepath = f"{path}/{log_file_name}"

        with open(filepath, 'w') as f:
            f.write(f"{self.filename} {tags}\n")
            f.close()
