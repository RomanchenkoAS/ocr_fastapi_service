import os

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from exception import InvalidLanguage
from routers.files import router as files_router
from routers.api import router as service_router

app = FastAPI()
app.include_router(files_router)
app.include_router(service_router)

os.makedirs('files', exist_ok=True)


@app.exception_handler(InvalidLanguage)
async def invalid_language_exception_handler(exc: InvalidLanguage):
    return JSONResponse(
        status_code=418,
        content={"success": False, "message": exc.message},
    )
