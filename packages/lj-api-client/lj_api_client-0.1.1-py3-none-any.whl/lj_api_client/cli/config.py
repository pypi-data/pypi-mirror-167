import os
import json
from pathlib import Path

class Config:
    CONFIG_DEFAULT_DIR_PATH = os.path.join(Path.home(), '.live_journey')
    CONFIG_DEFAULT_FILE_NAME = 'config'

    @classmethod
    def get_config_data(cls):
        cls.create_config_file()
        config_file_path = os.path.join(cls.CONFIG_DEFAULT_DIR_PATH, cls.CONFIG_DEFAULT_FILE_NAME)

        with open(config_file_path, 'r') as f:
            data = json.load(f)

        return data

    @classmethod
    def create_config_file(cls, force=False):
        if not os.path.exists(cls.CONFIG_DEFAULT_DIR_PATH):
            os.mkdir(cls.CONFIG_DEFAULT_DIR_PATH)

        config_file_path = os.path.join(cls.CONFIG_DEFAULT_DIR_PATH, cls.CONFIG_DEFAULT_FILE_NAME)
        if os.path.exists(config_file_path) and not force:
            return

        with open(config_file_path, 'w') as f:
            json.dump({}, f)

    @classmethod
    def update_config(cls, **args):
        new_config = cls.get_config_data()
        new_config.update(args)
        config_file_path = os.path.join(cls.CONFIG_DEFAULT_DIR_PATH, cls.CONFIG_DEFAULT_FILE_NAME)

        with open(config_file_path, 'w') as f:
            json.dump(new_config, f)