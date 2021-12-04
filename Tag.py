from Exclusion import Exclusion


class Tag:
    def __init__(self, value, exclude):
        self.value = value
        self.exclude = exclude

    def __str__(self):
        if self.exclude == Exclusion.EXCLUDED:
            return f"-{self.value}"

        return f"{self.value}"
