from argparse import ArgumentParser, Namespace, Action


class SplitArguments(Action):
    def __call__(self, parser: ArgumentParser, namespace: Namespace, values: str, option_string: str = None):
        setattr(namespace, self.dest, values.split(','))
