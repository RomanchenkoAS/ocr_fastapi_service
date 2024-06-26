import os
import shutil

from PIL import Image
from fastapi import APIRouter, UploadFile, File
from fastapi import status
from pytesseract import pytesseract as ts

router = APIRouter(
    prefix="/upload",
    tags=["files"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def upload_file_view(upload_file: UploadFile = File(...)):
    files_dir_path = 'files'
    path = f"{files_dir_path}/{upload_file.filename}"

    os.makedirs(files_dir_path, exist_ok=True)

    with open(path, "wb") as f:
        shutil.copyfileobj(upload_file.file, f)

    text = ts.image_to_string(Image.open(path), lang='eng+rus')

    return {'text': text}
