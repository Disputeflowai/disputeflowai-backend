from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "DisputeFlowAI running"}

@app.get("/health")
def health():
    return {"status": "ok", "app": "DisputeFlowAI Backend"}
