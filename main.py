from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.routes import auth, contacts


app_dir = Path(__file__).parent

app = FastAPI()
app.mount("/src/routes/static", StaticFiles(directory="src/routes/static"), name="routes_static")
templates = Jinja2Templates(directory=app_dir / "src/routes/templates")

origins = [
  "*",
  "0.0.0.0",
  "https://contactsclient.olieksandrkond3.repl.co",
  "https://Contactsserver.olieksandrkond3.repl.co",
  "http://localhost:5500",
  "http://127.0.0.1:5500",
  "http://localhost:8000",
  "http://95.134.189.14:5500",
  "https://172.31.128.1:5500",
  "http://172.31.196.1:8000",
  "https://172.31.196.1:8000",  
]

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(auth.router)
app.include_router(contacts.router)

@app.get('/')
def hello(request: Request):
    return templates.TemplateResponse("contacts.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)