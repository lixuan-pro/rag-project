#用来读取环境变量
import os
#导入load_dotenv函数：把.env文件的内容加载到当前的运行环境里
from dotenv import load_dotenv

#把.env的内容读进来
load_dotenv()

#定义一个配置类：把项目要用的配置统一收纳到一个对象里
class Settings:
    def __init__(self):
        #从环境变量中读取app_name,没有就默认用第二个参数
        self.app_name=os.getenv("APP_NAME","RAG Project")
        self.app_version = os.getenv("APP_VERSION", "0.1.0")
        self.log_level = os.getenv("LOG_LEVEL", "INFO")


#创建一个全局可用的配置对象
settings = Settings()