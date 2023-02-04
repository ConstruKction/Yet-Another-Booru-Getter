import logging


class MetadataLogger:
    def __init__(self, path, id_image, filename, metadata):
        self.path = path
        self.id_image = id_image
        self.filename = filename
        self.metadata = metadata

    def log_metadata(self):
        log_file_name = f"{self.id_image}.txt"
        filepath = f"{self.path}/{log_file_name}"

        with open(filepath, 'w') as f:
            f.write(f"filename: {self.filename}\n")

            for metadata_item in self.metadata:
                f.write(f"{metadata_item}\n")

            f.close()
