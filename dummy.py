import os
import configparser
config = configparser.ConfigParser()
cwd = os.getcwd()
channel_details_file = os.path.join(cwd,'channel_details.ini')
print(channel_details_file)
with open(channel_details_file, 'r', encoding='utf-8') as file:
    config.read_file(file)
    api_id=config['channel']['channel_one']
    # api_hash=config['channel']['api_hash']
    print(api_id)
    # cwd = os.getcwd()


# config_path = os.path.join(cwd,'telegram_automation.ini')
# print(config_path)
# config.read(config_path)
# api_id=config['telegram_automation']['api_id']
# api_hash=config['telegram_automation']['api_hash']
# channel = config['telegram_automation']['channel']
# print(channel)