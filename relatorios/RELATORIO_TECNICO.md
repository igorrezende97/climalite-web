# Relatório Técnico de Arquitetura e Implementação — ClimaLite

**Projeto Integrador — UNIVESP (Polo São José dos Campos)**  
**Desenvolvedor:** Igor Leonardo Rezende Nascimento  

---

## 1. Descrição Geral do Projeto
O **ClimaLite** é uma aplicação web full-stack desenvolvida para fornecer informações meteorológicas em tempo real de forma leve, responsiva e altamente acessível, atendendo aos requisitos acadêmicos e técnicos do Projeto Integrador da UNIVESP.

---

## 2. Arquitetura do Sistema
A solução foi arquitetada utilizando o modelo desacoplado (Front-End e Back-End):

1. **Front-End (Interface do Usuário):**
   - HTML5, CSS3 puro e JavaScript ES6+.
   - **Acessibilidade:** Integração nativa com o **VLibras** e modo de **Alto Contraste**.
   - **Persistência Local:** Utilização de `localStorage` para memorizar a última cidade pesquisada.
   - **Consumo de APIs Externas:** Integração com a **Open-Meteo API** (Geocoding + Forecast).

2. **Back-End (Servidor REST):**
   - Framework **FastAPI** (Python 3.10+) executado via **Uvicorn**.
   - Suporte a **CORS** habilitado para comunicação com o front-end.

3. **Banco de Dados (Persistência):**
   - **SQLite3** embutido para armazenar os feedbacks.

---

## 3. Endpoints da API REST (`main.py`)

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/` | Health-check da API. |
| `POST` | `/api/feedback` | Armazena um novo feedback no SQLite. |
| `GET` | `/api/feedback` | Retorna os feedbacks armazenados em JSON. |

---

## 4. Requisitos de Acessibilidade
- **Deficiência Auditiva:** Widget VLibras integrado na parte inferior direita da tela.
- **Baixa Visão / Daltonismo:** Botão alternador para modo de Alto Contraste com alta luminescência.
