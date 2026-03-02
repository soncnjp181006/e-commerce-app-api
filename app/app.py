from fastapi import FastAPI, APIRouter

app = FastAPI()

# app.include_router()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)