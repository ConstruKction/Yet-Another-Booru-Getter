from tag_requests.tag import Tag


class ImageInterface:
    def download(self, path: str, tags: list[Tag]):
        raise NotImplementedError

    def log_metadata(self, path: str):
        raise NotImplementedError

    def get_metadata(self):
        raise NotImplementedError
