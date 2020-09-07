import logging
import os

basedir = os.path.dirname(os.path.dirname(__file__))

logsdir = os.path.join(basedir, 'logs')

logs_file = os.path.join(logsdir, 'Condelogs.log')

# logging.basicConfig(filename=logs_file, level=logging.DEBUG)

# 自定义loger对象并定义log级别
logger = logging.getLogger('Cnodeapi')
logger.setLevel(logging.DEBUG)

#  创建命令行输出日志 并设置日志级别
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

# 创建日志输出格式
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

# 定义的格式穿给命令行输出
sh.setFormatter(formatter)

logger.addHandler(sh)

fh =logging.FileHandler(filename=logs_file, encoding='UTF-8')
fh.setLevel(logging.DEBUG)

fh.setFormatter(formatter)
logger.addHandler(fh)

# if __name__ == '__main__':
#     logger.info('1111')
#     logger.debug('222')
#     logger.warning('3333')
#     logger.error('55555555')
