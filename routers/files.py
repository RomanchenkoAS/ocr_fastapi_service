import os
import shutil

from PIL import Image
from fastapi import APIRouter, UploadFile, File, Query
from fastapi import status
from fastapi.responses import JSONResponse
from pytesseract import pytesseract as tess

from scripts.utils import validate_language

router = APIRouter(prefix="/upload", tags=["files"])

MEGABYTE = 1024 * 1024


@router.post("/", status_code=status.HTTP_200_OK)
async def upload_file_view(
    upload_file: UploadFile = File(...),
    lang: str = Query(
        default="eng",
        description="Chosen language for recognition.",
        examples=["eng", "rus", "eng+rus"],
    ),
):
    validate_language(lang)

    # Check file size
    # Move the cursor to the end of the file
    upload_file.file.seek(0, 2)
    # Get the file size in bytes
    file_size = upload_file.file.tell()
    # Move the cursor back to the beginning of the file
    upload_file.file.seek(0)

    if file_size > MEGABYTE:
        return JSONResponse(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            content={"detail": "File too large. Maximum size is 1 MB."},
        )

    files_dir_path = "files"
    path = f"{files_dir_path}/{upload_file.filename}"

    with open(path, "wb") as f:
        shutil.copyfileobj(upload_file.file, f)

    # Set correct privileges for saved image
    os.chmod(path, 0o666)

    text = tess.image_to_string(Image.open(path), lang="eng+rus")

    return {
        "success": True,
        "text": text
    }
