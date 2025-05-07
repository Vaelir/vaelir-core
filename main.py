from fastapi import FastAPI

app = FastAPI()

@app.get("/vaelir/status")
def status():
    return {"status": "ativo", "fase": "1", "mensagem": "Vaelir despertou com sucesso."}

@app.get("/vaelir/memory")
def memory():
    return {"memória": "inicializada", "entradas": []}
