import os

from fastapi import FastAPI
from routers.files import router as files_router
from routers.service import router as service_router

app = FastAPI()
app.include_router(files_router)
app.include_router(service_router)

os.makedirs('files', exist_ok=True)
