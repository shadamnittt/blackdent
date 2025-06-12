from fastapi import FastAPI
from app.routers import clients
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(
    title="BlackDent — Учёт Пациентов",
    version="1.0.0"
)

app.include_router(clients.router)

# Пример проверки
@app.get("/")
def root():
    return {"message": "Сервер работает!"}

# Подключаем статику
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Роут для favicon.ico
@app.get("/favicon.ico")
async def favicon():
    return FileResponse(os.path.join("app", "static", "favicon.ico"))