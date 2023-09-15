## client get historical message scraping###
# testing historical data--client
import configparser
import json
import asyncio
import datetime
# from datetime import date, datetime
import pytz
import os
import time
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputPeerChannel
from telethon.tl import functions, types
import re
import pandas
from match_pattern import FindMatch
from config_channel import ConfigManage
# api_id = 16158085
# api_hash = '740de8906a6c696fd29c9a041c8dfd01'
# channel_three = '⚡️Dr Profit Arena BY GodLeak ⚡️'
# channel_two = '⚡️Devil Crypto BY GodLeak ⚡️'
# channel_one = '⚡️Bitcoin Ted BY GodLeak ⚡️'
# channel_four = '⚡️Always win trade BY GodLeak ⚡️'
# channel_five = '⚡️Alex Friedman Premium BY GodLeak ⚡️'
def get_config():
    config_manager = ConfigManage()
    if not config_manager.solveException():
        credentials = config_manager.get_channel_id()
        if credentials:
            return credentials
        else:
            return None

class GetChatId():
    def get_channel():
        cwd = os.getcwd()
        channel_details_file = os.path.join(cwd,'channel_details.txt')
        file_path = channel_details_file

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                contents = file.read()
                print(contents)
        except FileNotFoundError:
            print(f"The file '{file_path}' was not found.")
        except IOError as e:
            print(f"An error occurred while reading the file: {str(e)}")

# session_file_location = os.path.join(
#     cwd, 'FINAL_PROJ', 'client_Session.session')
# print(session_file_location)

async def main(channel,client):
    dialogs = await client.get_dialogs()
    today = datetime.datetime.today().date()
    yesterday = today - datetime.timedelta(days=1)
    print(yesterday)
    for dialog in dialogs:
        # sort
        # if dialog.title in channel_id[try this later]
        print(dialog.title)
        if dialog.is_channel:
            if channel == dialog.title:  # use if Channel_id == channel_entity.id: instead of username after getting client id
                # Adjust the 'limit' as needed
                channel_entity = dialog.entity
                messages = await client.get_messages(channel_entity, limit=200)
                for message in messages:
                    print('------------------------------------------------------------------')
                    print(f'message:{message.text}')
                    try:
                        grp_four_obj = FindMatch(message=message.text)
                        matched_data = grp_four_obj.p1_match()  #excute pn_match accordingly{later task}
                    except Exception as e:
                        print(e)
                        continue
                    print('back')
                    created_at = message.date.strftime('%Y-%m-%d %H:%M:%S')
                    matched_data['created_at'] = created_at
                    data = {"pair": matched_data.get('pair', ''),
                            "position": matched_data.get('position', ''), "entry": matched_data.get('entry', ''),
                            "entryAverage": matched_data.get('entryAverage', ''), "t_series": matched_data.get('t_series', ''),
                            "stopLoss": matched_data.get('stopLoss', ''), "created_at": matched_data.get('created_at', '')}
                    print(f"Message from {message.sender_id}: text:{matched_data}")

                break
            ####code for date wise sorting####
#             for message in messages:
#                 count+=1
#                 print(f"Message from {message.sender_id}: {message.text} ,  entity date:{channel_entity.date}")
#                 filtered_messages = [message for message in messages if message.date.date()== yesterday]
#     #             print(f"Messages in channel: {dialog.title}")
#             for msg in filtered_messages:

#             print(f'entity::{channel_entity}')
if __name__ == '__main__':
    import asyncio
    config = get_config()
    if config:
        api_id= config['api_id']
        api_hash = config['api_hash']
        channel = config['channel']
        is_historical = config['is_historical']
        print(f'asdad::{is_historical}')
        session_file_location="C:\\Users\\vishw\\Untitled Folder 3\\FINAL_PROJ\\client_session.session"
        with TelegramClient(session_file_location, api_id, api_hash) as client:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main(channel,client))
    else:
        raise Exception('credentials not found')
    #     except Exception as e:
    #         print(e)
