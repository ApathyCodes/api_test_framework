# import requests
#
# class APIClink():
#     def __init__(self):
#         self.base_url = 'http://49.233.108.117:3000/api/v1'
#
#     def do_requests(self, method: str, url: str, params=None, data=None, json= None, **kwargs):
#         """
#         :param method:
#         :param url:
#         :param params:
#         :param data:
#         :param json:
#         :param kwargs:
#         :return:
#         """
#         url = self.base_url+url
#         method = method.lower()
#         try:
#             if method == 'get':
#                 return requests.get(url, params= params, **kwargs)
#             elif method == 'post':
#                 return requests.post(url, data=data, json=json, **kwargs)
#         except Exception:
#             print("程序异常")

import logging
import os

# 将所有的日志统一封装到 logs目录下
basedir = os.path.dirname(os.path.dirname(__file__))  # 获取项目根目录

# 设置log 目录
logDir = os.path.join(basedir, 'logs')

# 设置log 文件
log_file = os.path.join(logDir, 'example.log')

# 配置log级别
logging.basicConfig(filename=log_file, level=logging.DEBUG)

if __name__ == '__main__':
    logging.debug('hhhh')
    logging.warning('kkk')
