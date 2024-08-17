import argparse

from split_arguments import SplitArguments


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-t', '--tags', help='comma-separated tags (e.g. cute,vanilla)')
        self.parser.add_argument('-e', '--exclude', help='comma-separated tags to exclude')
        self.parser.add_argument('-c', '--count', help='amount of images desired, max 100', default=10, type=int)
        self.parser.add_argument('-l', '--log', help='log filenames with their respective tags in a txt file',
                                 default=False,
                                 action=argparse.BooleanOptionalAction)
        self.parser.add_argument('-a', '--all', help='download ALL images with specified tags', default=False,
                                 action=argparse.BooleanOptionalAction)
        self.parser.add_argument('-b', '--boorus',
                                 help='specify boorus from which to download (e.g. -s gelbooru,danbooru)',
                                 action=SplitArguments)
        self.parser.add_argument('-sfw', '--safe-for-work', help='download only sfw images', default=False,
                                 action=argparse.BooleanOptionalAction)
        self.parser.add_argument('-nsfw', '--not-safe-for-work', help='download only nsfw images', default=False,
                                 action=argparse.BooleanOptionalAction)

    def parse_args(self):
        return self.parser.parse_args()
