import configparser
import os
class ConfigParser:
    def __init__(self):
        self.config=configparser.ConfigParser()
        base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path=os.path.join(base_dir,'config','config.ini')
        self.config.read(config_path,encoding='utf-8')
    def get(self,section,key):
        return self.config[section][key]
    
    def getint(self,section,key):
        return self.config[section].getint(key)
    

config=ConfigParser()