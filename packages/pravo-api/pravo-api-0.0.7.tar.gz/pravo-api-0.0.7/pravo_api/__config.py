import configparser

from worker.api import Configs

def read_config():
    config = configparser.ConfigParser()
    config.optionxform = lambda option: option
    config.read('config.ini', encoding='utf-8')
    return config


api_config = read_config()['Api_Settings']

api_config = Configs(**api_config)
# print('api_config.DATA_FOLDER---',api_config.DATA_FOLDER)
# print(api_config)
# for e in ['DATA_FOLDER', 'RAW_FILES_FOLDER', 'REGION_FOLDER']:
#     print('attr',e, '==',getattr(api_config, e))
