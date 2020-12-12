import requests
import pytest
import logging
import unittest

logging.basicConfig(filename='Conde-logs.log', level=logging.DEBUG)

class Clinet_Cnode():

    def __init__(self):
        self.base_url = 'http://49.233.108.117:3000/api/v1'

    def do_requests(self, method: str, url: str, desc=None, params=None, data=None, **kwargs):

        url = self.base_url+url
        print(f'{method}---{url}---{desc}')
        if method == 'get':
            response = requests.get(url,params=params, **kwargs)
            print(f'{response.status_code}--{data}')
            logging.info(f'{response.status_code}--{data}')
            return response
        elif method == 'post':
            response = requests.post(url, data=data, **kwargs)
            print(f'{response.status_code}---{data}')
            logging.info(f'{response.status_code}--{data}')
            return response


if __name__ == '__main__':
    sdk = Clinet_Cnode()
    sdk.do_requests('get', '/topics', '主题首页')
    sdk.do_requests('post', '/topics', '新建主题')