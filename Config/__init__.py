import os
import yaml


class config:

    def __init__(self,config_file_path=None):
        if not config_file_path:
            config_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../resource/Config.yaml')
        config_file = open(config_file_path)
        self.consts = yaml.safe_load(config_file)
        config_file.close()

    def __getitem__(self,prop):
        return self.consts[prop]
