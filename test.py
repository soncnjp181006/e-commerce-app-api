from fastapi import FastAPI, APIRouter #, Depends
from test.app.api.api import router
app = FastAPI()

app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)