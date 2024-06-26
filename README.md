# FastAPI OCR service

## Description

This is a simple OCR (Optical Character Recognition) application built with FastAPI and Tesseract. The application
allows users to upload images and extracts text from these images using Tesseract OCR.

This app supports multiple languages by utilizing Tesseract's language data files.
Users can specify the language(s) to be used for text extraction, and the app will validate and process the images
accordingly.

## Requirements

- Python 3.12
- Poetry
- Tesseract

## Installation

### Install Poetry

- If poetry package manager is not installed, you can install it like this for Windows:

```shell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python - <br>
curl -sSL https://install.python-poetry.org | python -
```

- Verify installation

```shell
poetry --version
```

- For Linux:

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

- Verify installation

```shell
poetry --version
```

- Optional step: you can configure poetry to keep all dependencies in the project repository. For that, move into the
  project directory and run:

```shell
poetry config virtualenvs.in-project true
```

### Install Tesseract

1. For Windows:

    - Download the Tesseract installer from the official
      repository: <a href="https://github.com/UB-Mannheim/tesseract/wiki">Tesseract at UB Mannheim</a>
    - Run the installer and follow the installation instructions.
    - Add Tesseract to your system's PATH:
        - Open Control Panel -> System and Security -> System -> Advanced system settings
        - Click on "Environment Variables"
        - Under "System variables", find the <code>Path</code> variable, select it, and click "Edit"
        - Click "New" and add the path to the Tesseract executable (e.g., <code>C:\Program Files\Tesseract-OCR</code>)
        - Click OK to close all dialogs
    - Verify the installation by running:
      ```shell 
      tesseract --version
      ```

2. For Linux:

    - Update your package list and install Tesseract:

      ```shell 
      sudo apt update && sudo apt install tesseract-ocr
      ```

    - Verify the installation by running:

      ```shell
      tesseract --version
      ```

3. For macOS:

    - Install Homebrew if it is not already installed. You can install Homebrew from <a href="https://brew.sh/">
      here</a>.
    - Use Homebrew to install Tesseract:

      ```shell
      brew install tesseract
      ```

    - Verify the installation by running:

      ```shell
      tesseract --version
      ```

### Configure Tesseract

- Tesseract can be configured by specifying the path to the language data files. By default, Tesseract searches for the
  language data files in the <code>tessdata</code> directory inside the Tesseract installation directory.
- You can set the <code>TESSDATA_PREFIX</code> environment variable to point to the directory containing the language
  data files:

   ```shell
   export TESSDATA_PREFIX=/path/to/tessdata/
   ```

### Add languages

- You can download any additional languages you want installed at https://github.com/tesseract-ocr/tessdata
- After downloading you need to place them into tesseract data directory:

```shell
sudo cp -r /path/to/your/traindata/* /usr/share/tesseract-ocr/4.00/tessdata/
```

- Verify language installation with:

```python
from pytesseract import pytesseract as tess

print(tess.get_languages())
```

### Tesseract details

You can find more detailed information about tesseract on
it's [official Github page](https://github.com/madmaze/pytesseract).

With Poetry and Tesseract installed, you are now ready to proceed with setting up your OCR application.</p>

## Running the Application

Build and run the Docker containers:

```shell
docker-compose up --build
```

### Access the application:

Open a web browser and go to http://localhost. The FastAPI application should be accessible through the Nginx reverse
proxy.

### Usage

- Upload an image through the **/upload** endpoint and specify the language for text extraction.
- Retrieve available languages using the **/api/languages** endpoint.
- Explore the API documentation at **/docs**.

With these steps, your OCR application should be up and running, ready to accept and process image files for text
extraction.