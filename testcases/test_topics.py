from sdk.client_sdk import ClientSDK
from common.logger import logger
import pytest

sdk = ClientSDK()

def test_create_topic():
    test_data = {
        "accesstoken": "c1647158-1d48-4977-86c8-a0a4b0d5603f",   # c1647158-1d48-4977-86c8-a0a4b0d5603f
        "title": "test_create_topic",
        "tab": "ask",
        "content": "发布话题测试"
    }
    res = sdk.do_requests('post', '/topics', desc='新建主题', data=test_data)
    print(res)

    assert res.status_code == 200
    jsonData = res.json()
    logger.info(f'result: {jsonData}')
    assert jsonData['topic_id'] != ""


"""
测试异常场景
创建话题失败场景

数据驱动
可使用pytest 参数化 pytest.param 需引用pytest 添加装饰器@pytest.mark.parametrize
"""

test_data1 = {
        "accesstoken": "",
        "title": "test_create_topic",
        "tab": "ask",
        "content": "发布话题测试"
    }
test_data2 = {
        "accesstoken": "c1647158-1d48-4977-86c8-a0a4b0d5603f",
        "title": "",
        "tab": "ask",
        "content": "发布话题测试"
    }
@pytest.mark.parametrize("test_data", [test_data1, test_data2])
def test_topics_failed(test_data):

    res = sdk.do_requests('post', '/topics', desc='新建主题', data=test_data)
    jsonData = res.json()
    logger.debug(f'运行结果：{jsonData}')

    # assert res.status_code == 401
    # jsonData = res.json()
    # assert jsonData['error_msg'] == "错误的accessToken"
    #
    # res = sdk.do_requests('post', '/topics', desc='新建主题', data=test_data)
    # assert res.status_code == 400
    # jsonData = res.json()
    # assert jsonData['error_msg'] == "标题不能为空"