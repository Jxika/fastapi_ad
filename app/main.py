from fastapi import FastAPI
from app.api.v1.endpoints import user
from app.db.session import engine
from app.db.base import Base

app = FastAPI()

# 创建所有数据库表
Base.metadata.create_all(bind=engine)

# 根路径路由
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

app.include_router(user.router, prefix="/api/v1")
