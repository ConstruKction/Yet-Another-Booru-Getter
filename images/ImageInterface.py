class ImageInterface:
    def download(self, path):
        raise NotImplementedError

    def log_metadata(self, path):
        raise NotImplementedError

    def get_metadata(self):
        raise NotImplementedError
