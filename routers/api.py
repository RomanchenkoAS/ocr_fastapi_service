from fastapi import APIRouter
from pytesseract import pytesseract as tess

router = APIRouter(prefix="/api", tags=["service"])


@router.get("/languages")
async def get_languages():
    return {
        "success": True,
        "languages": [lang for lang in tess.get_languages(config="") if lang != "osd"],
    }
