from fastapi import status


def test_main(test_client):
    """Test general accessibility of app."""
    response = test_client.get("/")
    assert response.status_code == status.HTTP_200_OK


def test_get_languages(test_client):
    response = test_client.get("/api/languages")
    assert response.status_code == status.HTTP_200_OK
    assert "eng" in response.json()["languages"]
    assert "osd" not in response.json()["languages"]


def test_upload_file_view(test_client):
    """Expect correct string recognized in response."""
    expected_line = (
        "FastAPI is a modern, fast (high-performance), web framework for building APIs "
        "with Python based on standard Python type hints"
    )

    with open("tests/test_images/test_image_1.png", "rb") as image_file:
        image_bytes = image_file.read()

    files = {"upload_file": ("test_image_1.png", image_bytes, "image/png")}
    response = test_client.post("/upload", files=files, params={"lang": "eng+rus"})

    assert response.status_code == status.HTTP_200_OK

    response_data = response.json()
    assert response_data["success"] is True
    assert expected_line in response_data["text"]


def test_bad_language(test_client):
    """Language is wrong, expect error."""
    with open("tests/test_images/test_image_1.png", "rb") as image_file:
        image_bytes = image_file.read()

    files = {"upload_file": ("test_image_1.png", image_bytes, "image/png")}
    response = test_client.post(
        "/upload", files=files, params={"lang": "WRONG_LANGUAGE"}
    )

    assert response.status_code == status.HTTP_418_IM_A_TEAPOT
    assert response.json()["success"] is False
    assert response.json()["message"] == "Language is not valid"


def test_upload_cat_file_view(test_client):
    """This is a cat picture, we expect no text here"""
    expected_line = ""

    with open("tests/test_images/test_image_2_cat.png", "rb") as image_file:
        image_bytes = image_file.read()

    files = {"upload_file": ("test_image_2_cat.png", image_bytes, "image/png")}
    response = test_client.post("/upload", files=files, params={"lang": "eng+rus"})

    assert response.status_code == status.HTTP_200_OK

    response_data = response.json()
    assert response_data["success"] is True
    assert expected_line in response_data["text"]
