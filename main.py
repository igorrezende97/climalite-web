import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="ClimaLite API")

# 1. Servir os arquivos estáticos (CSS, JS, imagens) da pasta 'static'
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# 2. Rota principal que entrega a interface web (index.html)
@app.get("/")
def read_root():
    return FileResponse("index.html")

# --- Aqui seguem as suas rotas de API existentes (Open-Meteo, SQLite, etc.) ---
