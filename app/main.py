from fastapi import FastAPI
#创建应用
app = FastAPI(title="RAG Project", version="0.1.0")

#定义GET接口
@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": "0.1.0"}