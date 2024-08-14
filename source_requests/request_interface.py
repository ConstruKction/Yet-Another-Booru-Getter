from tag import Tag


class RequestInterface:
    def get_json(self):
        raise NotImplementedError

    def create_tags_string(self, tags: list[Tag]):
        raise NotImplementedError
