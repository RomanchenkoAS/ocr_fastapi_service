from fastapi import APIRouter
from pytesseract import pytesseract as ts

router = APIRouter(
    prefix="/api",
    tags=["service"]
)


@router.get("/languages")
async def get_languages():
    return {
        'success': True,
        'languages': [lang for lang in ts.get_languages(config='') if lang != 'osd']
    }
