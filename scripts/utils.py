from pytesseract import pytesseract as tess

from exception import InvalidLanguage


def validate_language(lang_input: str) -> None:
    """ Validate language string inputted by user """
    if "+" in lang_input:
        languages = lang_input.split("+")
    else:
        languages = [lang_input]

    existing_languages = tess.get_languages()

    if any(language not in existing_languages for language in languages):
        raise InvalidLanguage(f"Language is not valid")
