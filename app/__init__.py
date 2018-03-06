from util.Singleton import Singleton
from util import log

from Config import config

class GW_APP:
    __metaclass__ = Singleton
    def __init__(self,app_name=None,config_file_path=None):
        log.Ilog("GW_APP Singleton instace __init__");
        self.app_name =app_name
        self.config = config(config_file_path=config_file_path);






