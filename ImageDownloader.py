import logging
from http import HTTPStatus

import requests
from fake_useragent import UserAgent
from tqdm import tqdm


class ImageDownloader:
    def __init__(self, url, path, filename):
        self.url = url
        self.download_path = path
        self.filename = filename

    def download(self):
        if not self.url:
            logging.error(f"No URL present for {self.filename} in the API self!")
            return

        user_agent = UserAgent()
        headers = {'user-agent': user_agent.chrome}

        response = requests.get(self.url, stream=True, headers=headers)
        expected_size = int(response.headers.get('content-length', 0))
        progress_bar = tqdm(total=expected_size, unit='B', unit_scale=True, desc=self.filename)

        if response.status_code != HTTPStatus.OK:
            logging.error(response.status_code)
            return

        with open(self.download_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    progress_bar.update(len(chunk))
                    f.write(chunk)
                    f.flush()

        progress_bar.close()

        if expected_size != 0 and progress_bar.n != expected_size:
            logging.error(f"Something went wrong while storing {self.filename}")
