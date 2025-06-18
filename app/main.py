import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

from app.routers import clients, auth
from fastapi import FastAPI
from app.routers import clients
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(
    title="BlackDent — Учёт Пациентов",
    version="1.0.0"
)

# Правильные пути
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Роутеры
app.include_router(clients.router, prefix="/clients", tags=["Клиенты"])
app.include_router(auth.router, tags=["Аутентификация"])

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/clients.html")
def show_clients(request: Request):
    return templates.TemplateResponse("clients.html", {"request": request})

@app.get("/favicon.ico")
async def favicon():
    return FileResponse(os.path.join(BASE_DIR, "static", "favicon.ico"))

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
