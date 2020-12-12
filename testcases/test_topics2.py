import pytest
from common.utils import FileHandler
from sdk.client_sdk import ClientSDK
from common.logger import logger
import json


sdk = ClientSDK()
fh = FileHandler()
test_date = fh.do_Excel("testdata.xlsx", "Sheet1")  # 传文件名


datanames = "id,desc,method,url,data,expect_val,code"

@pytest.mark.parametrize(datanames, test_date)
def test_create_topic(id, desc, method, url, data, expect_val, code):
    logger.info(f"开始执行第{id}用例, {type(data)}")
    # 若失败 异常处理
    try:
        # 数据驱动
        res = sdk.do_request(method, url, desc=desc, data=json.loads(data), params=json.loads(data))  # 引用json.loads将str转换成dict

        jsonData = res.json()
        if method == 'get':
            assert res.status_code == code
            assert jsonData['data'] != None

        elif method == 'post':
            # logger.debug(f'运行结果：{jsonData}')
            assert res.status_code == code
            assert jsonData == json.loads(expect_val)

    except Exception as e:
        logger.error(f"运行失败:{e}")
        raise Exception  # 抛出异常
    logger.info("用例运行通过")


