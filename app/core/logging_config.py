#库中用于记录程序运行日志的模块
import logging
#导入Path，方便处理文件路径
from pathlib import Path

from app.core.config import settings

LOG_DIR=Path("logs")
LOG_DIR.mkdir(exist_ok=True)

#定义一个函数，初始化日志配置，让日志同时输出到终端和文件
def setup_logging()->None:
    # 本质：在logging里找配置中的日志级别(字符串-->logging常量)
    level = getattr(logging, settings.log_level.upper(), logging.INFO)
    #快速配置root logger
    logging.basicConfig(
        #设置日志最低的记录级别
        level=level,
        #定义日志的显示格式
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        #
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(LOG_DIR / "app.log",encoding="utf-8"),

        ],
        force=True
    )


def get_logger(name):
    return logging.getLogger(name)








