class ImageInterface:
    def download(self, path, tags):
        raise NotImplementedError

    def log_metadata(self, path):
        raise NotImplementedError

    def get_metadata(self):
        raise NotImplementedError
