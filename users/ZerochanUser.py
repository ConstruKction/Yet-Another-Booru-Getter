import json
import logging
import pathlib
import sys

from users.UserInterface import UserInterface


class ZerochanUser(UserInterface):
    def __init__(self):
        self.z_id = self.initialize_user().get('z_id')
        self.z_hash = self.initialize_user().get('z_hash')

    def initialize_user(self):
        if __debug__:
            zerochan_config_location = f"{pathlib.Path().resolve()}/debug_files/zerochan_debug.json"
        else:
            zerochan_config_location = f"{pathlib.Path().resolve()}/config/zerochan.json"

        if not pathlib.Path(zerochan_config_location).exists():
            logging.critical(
                f"zerochan.json config file not found!\n Get one from here, fill out your z_id and z_hash and put it "
                f"in a folder named 'config': "
                f"https://github.com/ConstruKction/Yet-Another-Booru-Getter/blob/master/config/zerochan.json")
            sys.exit()

        f = open(zerochan_config_location)
        json_config = json.load(f)

        return json_config
