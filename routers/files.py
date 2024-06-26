import shutil

from PIL import Image
from fastapi import APIRouter, UploadFile, File, Query
from fastapi import status
from pytesseract import pytesseract as ts

from scripts.utils import validate_language

router = APIRouter(
    prefix="/upload",
    tags=["files"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def upload_file_view(
        upload_file: UploadFile = File(...),
        lang: str = Query(
            default="eng",
            description="Chosen language for recognition.",
            examples=["eng", "rus", "eng+rus"]
        )
):
    validate_language(lang)
    files_dir_path = 'files'
    path = f"{files_dir_path}/{upload_file.filename}"

    with open(path, "wb") as f:
        shutil.copyfileobj(upload_file.file, f)
    text = ts.image_to_string(Image.open(path), lang='eng+rus')

    return {'text': text}
