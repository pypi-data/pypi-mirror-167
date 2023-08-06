import requests
import json

from .config import FCM_URL, FCM_MAX_BATCH_SIZE
from .utils import chunks


class FCMClient:
    url = FCM_URL
    max_batch_size = FCM_MAX_BATCH_SIZE
    
    def __init__(self, api_key):
        self.api_key = api_key
        
    def create_headers(self, api_key):
        return {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*', 
            'User-Agent': 'PostmanRunTime/7.29.2', 
            'Connection': 'keep-alive',  
            'Content-Type': 'application/json', 
            'Authorization': 'key='+api_key
        } 
        
    def create_payload(self, data_map):
        data_map['text'] = data_map.get('body')
        data = data_map
        notification = data_map
        priority = "high"
        collapse_key = "collapse_key"
        payload = {
                    'collapse_key': collapse_key,
                    'data': data,
                    'notification': notification,
                    'priority': priority,
                }
        return payload
    
    def send(self, data_map, tokens):
        try:    
            headers = self.create_headers(self.api_key)
            payload = self.create_payload(data_map)
            fcm_response = []
            for curr_batch in chunks(tokens, self.max_batch_size):
                payload['registration_ids'] = curr_batch
                curr_batch_response = requests.post(self.url, data=json.dumps(payload), headers=headers)
                curr_batch_response.raise_for_status()
                fcm_response.append(curr_batch_response.json())
            return fcm_response
        except Exception as e:
            print('send to fcm exception', str(e))