from fastapi import FastAPI

from app.core.config import settings

from app.core.logging_config import get_logger,setup_logging


setup_logging()
logger=get_logger(__name__)



#创建应用,把写死的值变成可配置值
#创建了一个叫app的fastapi应用对象,
# 但是他不会自动监听8000窗口，也不会自动变成一个可以访问的网站
app=FastAPI(title=settings.app_name,version=settings.app_version)

#定义GET接口
@app.get("/health")
def health():
    logger.info("Health endpoint called")
    return {"status": "ok"}


@app.get("/version")
def version():
    logger.info("Version endpoint called")
    return {
        "app_name":settings.app_name,
        "version":settings.app_version,
        "log_level":settings.log_level
    }