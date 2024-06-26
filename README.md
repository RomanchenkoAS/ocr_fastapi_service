# Installation

## Install poetry

<ul>
    <li>If poetry package manager is not installed, you can install it like this for Windows:
        <pre><code>(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python - <br>
curl -sSL https://install.python-poetry.org | python -</code></pre>
<li>Verify installation</li>
        <pre><code>poetry --version</code></pre>
    </li>
    <li>For Linux:
        <pre><code>curl -sSL https://install.python-poetry.org | python3 -</code></pre>

<li>Verify installation</li>
        <pre><code>poetry --version</code></pre>
<li>Optional step: you can configure poetry to keep all dependencies in the project repository. For that, move into the project directory and run:
        <pre><code>poetry config virtualenvs.in-project true        </code></pre>
    </li>
</ul>

## Install Tesseract

<ul>
    <li>For Windows:
        <ol>
            <li>Download the Tesseract installer from the official repository: <a href="https://github.com/UB-Mannheim/tesseract/wiki">Tesseract at UB Mannheim</a></li>
            <li>Run the installer and follow the installation instructions.</li>
            <li>Add Tesseract to your system's PATH:
                <ol>
                    <li>Open Control Panel -> System and Security -> System -> Advanced system settings</li>
                    <li>Click on "Environment Variables"</li>
                    <li>Under "System variables", find the <code>Path</code> variable, select it, and click "Edit"</li>
                    <li>Click "New" and add the path to the Tesseract executable (e.g., <code>C:\Program Files\Tesseract-OCR</code>)</li>
                    <li>Click OK to close all dialogs</li>
                </ol>
            </li>
            <li>Verify the installation by running:
                <pre><code>tesseract --version</code></pre>
            </li>
        </ol>
    </li>
    <li>For Linux:
        <ol>
            <li>Update your package list and install Tesseract:
                <pre><code>sudo apt update && sudo apt install tesseract-ocr</code></pre>
            </li>
            <li>Verify the installation by running:
                <pre><code>tesseract --version</code></pre>
            </li>
        </ol>
    </li>
    <li>For macOS:
        <ol>
            <li>Install Homebrew if it is not already installed. You can install Homebrew from <a href="https://brew.sh/">here</a>.</li>
            <li>Use Homebrew to install Tesseract:
                <pre><code>brew install tesseract</code></pre>
            </li>
            <li>Verify the installation by running:
                <pre><code>tesseract --version</code></pre>
            </li>
        </ol>
    </li>
</ul>

### Configure Tesseract

<ul>
    <li>Tesseract can be configured by specifying the path to the language data files. By default, Tesseract searches for the language data files in the <code>tessdata</code> directory inside the Tesseract installation directory.</li>
    <li>You can set the <code>TESSDATA_PREFIX</code> environment variable to point to the directory containing the language data files:
        <pre><code>export TESSDATA_PREFIX=/path/to/tessdata/</code></pre>
    </li>
</ul>

<p>With Poetry and Tesseract installed, you are now ready to proceed with setting up your OCR application.</p>



### Add languages

- You can download any additional languages you want installed at https://github.com/tesseract-ocr/tessdata
- After downloading you need to place them into tesseract data directory:
```shell
sudo cp -r /path/to/your/traindata/* /usr/share/tesseract-ocr/4.00/tessdata/
```
- Verify installation with:
```python
from pytesseract import pytesseract as tess

print(tess.get_languages())
```

### Tesseract details

You can find more detailed information about tesseract on it's [official Github page](https://github.com/madmaze/pytesseract).
