from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Render!"}

@app.get("/jobs")
def get_jobs():
    return [{"name": "Make Ready Tool NESC Demo, editing to make sure start up is not too bad", "status": "active"}]

print()
