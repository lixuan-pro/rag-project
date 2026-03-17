# rag-project

一个面向 RAG 工程学习的 FastAPI 后端骨架项目。  
当前阶段主要完成了项目初始化、基础接口、配置读取、日志输出和首个自动化测试，为后续文档导入、切块、检索与最小 RAG 回路打基础。

## 当前进度

已完成内容：

- FastAPI 最小服务骨架
- `GET /health` 健康检查接口
- `GET /version` 版本信息接口
- `.env` 配置读取
- 控制台 + 文件日志输出
- pytest 首个接口测试
- GitHub 仓库初始化与首次推送

## 项目目录结构

```text
rag-project/
├─ app/
│  ├─ api/
│  ├─ core/
│  │  ├─ config.py
│  │  └─ logging_config.py
│  ├─ __init__.py
│  └─ main.py
├─ data/
├─ docs/
├─ eval/
├─ logs/
├─ scripts/
├─ tests/
│  └─ test_health.py
├─ .env.example
├─ .gitignore
├─ README.md
└─ requirements.txt