"""
封装logging日志 提供统一日志记录
"""
import logging
import os

# 将所有的日志文件统一放到 logging 目录  做路径拼接
BaseDir = os.path.dirname(os.path.dirname(__file__))   # 获取项目根目录

logsDir = os.path.join(BaseDir, 'logs')   # 设置logs所在目录

# 设置log 文件与logs下
log_file = os.path.join(logsDir, 'example.log')

logging.basicConfig(filename=log_file, level=logging.DEBUG)


if __name__ == '__main__':
    logging.debug('hi')
    logging.warning('HHH')
