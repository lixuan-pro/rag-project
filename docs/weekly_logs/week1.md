# Week 1 周志：项目设置与骨架

## 1. 本周目标

本周目标是完成项目初始化和后端骨架搭建，建立后续 RAG 项目的基础工程结构，具体包括：

- 创建 GitHub 仓库并完成本地项目初始化
- 搭建 FastAPI 最小服务骨架
- 实现 `/health` 和 `/version` 接口
- 增加 `.env` 配置读取
- 增加基础日志模块
- 为项目添加首个 pytest 测试
- 初始化 README 和周志
- 建立 `develop` 分支，形成后续开发主线

---

## 2. 本周实际完成

### 已完成的工程基础

- 完成项目目录结构初始化：
  - `app/`
  - `tests/`
  - `docs/`
  - `data/`
  - `eval/`
  - `scripts/`

- 完成 FastAPI 最小服务骨架搭建
- 实现 `GET /health` 健康检查接口
- 实现 `GET /version` 版本信息接口
- 完成 `.env.example` 与 `.env` 配置文件
- 编写 `app/core/config.py`，实现配置统一读取
- 编写 `app/core/logging_config.py`，实现控制台 + 文件日志输出
- 编写 `tests/test_health.py`，完成首个自动化测试
- 完成 README 初版，写清项目定位、启动方式、测试方式和当前进度
- 完成本地 Git 初始化、首次 commit、首次 push
- 建立并推送 `develop` 分支

### 当前项目状态

当前项目已经具备以下最小闭环：

- 服务可启动
- `/health` 可访问
- `/version` 可访问
- 配置可读取
- 日志可输出到终端和文件
- `/health` 可通过 pytest 自动化验证
- GitHub 仓库已同步，可作为后续持续开发基础

---

## 3. 本周关键问题与修复记录

### 问题 1：日志模块命名冲突
一开始把日志模块命名为 `logging.py`，与 Python 标准库 `logging` 重名，导致导入时出现循环导入样式报错。

**修复方式：**
- 将文件改名为 `logging_config.py`
- 修改 `main.py` 中的导入路径
- 后续避免使用与标准库重名的文件名

### 问题 2：pytest 导入失败
运行测试时，出现 `ModuleNotFoundError: No module named 'app'`。

**修复方式：**
- 为 `app/`、`app/core/`、`app/api/` 补充 `__init__.py`
- 使用 `python -m pytest` 运行测试

### 问题 3：对 FastAPI 启动方式理解不清
一开始不理解为什么要使用：

```bash
uvicorn app.main:app --reload