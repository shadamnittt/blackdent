import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.routers import clients, auth  # Роутеры

app = FastAPI(
    title="BlackDent — Учёт Пациентов",
    version="1.0.0"
)

# Подключение роутеров
app.include_router(clients.router, prefix="/clients", tags=["Клиенты"])
app.include_router(auth.router, tags=["Аутентификация"])

# Корневой маршрут
@app.get("/")
def root():
    return {"message": "Сервер работает!"}

# Подключение статики
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Favicon
@app.get("/favicon.ico")
async def favicon():
    return FileResponse(os.path.join("app", "static", "favicon.ico"))
