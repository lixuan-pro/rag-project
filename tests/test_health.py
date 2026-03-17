"""
FastAPI的接口测试代码
作用：自动检查/health接口是不是按照预期工作
client:客户端（发送请求的一方）
assert:断言（检查结果正确，否则报错）


"""


#导入Fastapi提供的测试客户端
from fastapi.testclient import TestClient
from app.main import app

#用FastAPI应用app创建一个测试客户端
client=TestClient(app)

def test_health():
    #测试客户端发送一个GET请求，返回响应
    response=client.get("/health")
    #检查接口返回200，否则测试失败报错
    assert response.status_code==200
    #检查接口返回json数据
    assert response.json()=={"status":"ok"}



