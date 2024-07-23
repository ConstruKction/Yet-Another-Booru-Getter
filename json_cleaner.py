import re


class JSONCleaner:
    def __init__(self, dirty_json: str, regular_expressions: dict):
        self.dirty_json = dirty_json
        self.regular_expressions = regular_expressions

    def clean_json(self) -> str:
        json = self.dirty_json
        for regular_expression, substitution in self.regular_expressions.items():
            json = re.sub(regular_expression, substitution, json)

        return json
