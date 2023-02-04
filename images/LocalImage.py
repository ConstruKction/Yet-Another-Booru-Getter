import hashlib

class LocalImage:
    def __init__(self, filepath):
        self.filename = filepath.split('/')[2]
        self.hash = self.calculate_hash(filepath)

    @staticmethod
    def calculate_hash(filepath):
        hash_md5 = hashlib.md5()

        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(2 ** 20), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
