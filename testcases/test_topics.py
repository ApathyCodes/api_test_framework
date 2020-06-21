from sdk.client_sdk import ClientSDK


sdk = ClientSDK()

def test_create_topic():
    test_data = {
        "accesstoken": "c1647158-1d48-4977-86c8-a0a4b0d5603f",
        "title": "test_create_topic",
        "tab": "ask",
        "content": "发布话题测试"
    }
    res = sdk.do_requests('post', '/topics', desc='新建主题', data=test_data)
    print(res)
    assert res.status_code == 200
    jsonData = res.json()
    assert jsonData['topic_id'] != ""
    # assert jsonData['ask'] == 'ask'