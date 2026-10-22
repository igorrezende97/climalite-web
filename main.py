from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
import datetime

app = FastAPI(title="ClimaLite API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def init_db():
    conn = sqlite3.connect("climalite.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedbacks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mensagem TEXT NOT NULL,
            data_envio TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

class FeedbackSchema(BaseModel):
    mensagem: str

@app.get("/")
def home():
    return {"status": "ok", "mensagem": "API do ClimaLite rodando perfeitamente!"}

@app.post("/api/feedback")
def salvar_feedback(data: FeedbackSchema):
    if not data.mensagem.strip():
        raise HTTPException(status_code=400, detail="O texto do feedback não pode estar vazio.")
    
    conn = sqlite3.connect("climalite.db")
    cursor = conn.cursor()
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO feedbacks (mensagem, data_envio) VALUES (?, ?)", (data.mensagem, data_atual))
    conn.commit()
    conn.close()
    
    return {"status": "sucesso", "mensagem": "Feedback salvo no banco de dados!"}

@app.get("/api/feedback")
def listar_feedbacks():
    conn = sqlite3.connect("climalite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, mensagem, data_envio FROM feedbacks ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    
    feedbacks = [{"id": r[0], "mensagem": r[1], "data_envio": r[2]} for r in rows]
    return {"total": len(feedbacks), "feedbacks": feedbacks}
