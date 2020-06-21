"""
封装 requests 请求库
1. 添加自己的日志系统
2. 添加异常处理
"""
import requests

class ClientSDK:  # 建类

    # 构造器
    def __init__(self):
        # 初始化实例变量
        self.base_url = 'http://49.233.108.117:3000/api/v1'  # 设置api 前置路径

    # 定义方法方便调用，统一处理中心
    def do_requests(self, method: str, url: str, desc=None, params=None, data=None, **kwargs):

        """
        统一封装请求处理方法
        :param method:   请求方法 get post
        :param url:     请求路径
        :param desc:    api描述
        :param params:  get 查询参数
        :param data:    post 请求表单数据
        :param kwargs:  其他参数
        :return:
        """

        url = self.base_url+url
        # 手动print日志
        print(f'{method}请求  请求路径：{url}---{desc}')
        if method == "get":
           res = requests.get(url, params=params, **kwargs)
           # 手动print状态码
           print(f'get请求数据:{params}---状态码：{res.status_code} ')
        elif method == 'post':
            res = requests.post(url, data=data, **kwargs)
            # 手动print状态码
            print(f'post请求数据:{data}---状态码：{res.status_code} ')

if __name__ == '__main__':
    sdk = ClientSDK()
    sdk.do_requests('get', '/topics', '主题首页')
    sdk.do_requests('post', '/topics', '新建主题')
