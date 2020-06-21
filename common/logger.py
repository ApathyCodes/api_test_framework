"""
封装logging日志 提供统一日志记录
"""
import logging
import os

# 将所有的日志文件统一放到 logging 目录  做路径拼接 (当前在common目录下logger文件)
BaseDir = os.path.dirname(os.path.dirname(__file__))   # 获取项目根目录

logsDir = os.path.join(BaseDir, 'logs')   # 设置logs所在目录

# 设置log 文件于logs下
log_file = os.path.join(logsDir, 'example.log')
"""
废弃代码:
# 定义logger对象实例化 指定logger_name
logger = logging.getLogger('apitest')
# 设置日志级别
logger.setLevel(logging.DEBUG)

frm = logging.Formatter('%(asctime)s %(message)s')
logging.StreamHandler()
"""
# 创建logger 对象  设置日志级别为DEBUG
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# 创建命令行输出日志并设置级别为DEBUG
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 创建格式   时间-名字-级别-打印信息
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 定义的格式传给ch命令行输出
ch.setFormatter(formatter)

# 命令行输出穿给logger对象
logger.addHandler(ch)

# 文件处理
fh = logging.FileHandler(filename=log_file, encoding='UTF-8')
fh.setLevel(logging.DEBUG)

# 设置文件输出流格式
fh.setFormatter(formatter)
# 文件处理添加至logger中
logger.addHandler(fh)

if __name__ == '__main__':
    logger.debug('hiiiii')
    logger.warning('HHHHHH')
