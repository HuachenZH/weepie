# Weepie
The weepies are always weepy.  

## Prepare environment
### pyenv
First you need pyenv to manage your python versions. This project is build with python 3.11.4.  

### pyenv virtualenv
It is recommended to use a virtual environment to manage packages.
```shell
$ pyenv local 3.11.4

$ pyenv virtualenv 3.11.4 weepie

$ pyenv local weepie
```

### Libraries
As there is `requirements.txt`,  
```shell
$ pip install -r requirements.txt
```

### Tesseract OCR
This project is based on the open source OCR tool Tesseract. Apart from installing pytesseract (the Python library for Tesseract (and is included in requirements.txt)), you need to install the Tesseract executable in your working environment.  
- If you work on Linux, follow this: [doc](https://tesseract-ocr.github.io/tessdoc/Installation.html)
- If you work on Windows, follow this: [doc](https://github.com/UB-Mannheim/tesseract/wiki)



## info
- an article: https://nanonets.com/blog/ocr-with-tesseract/
- another article: https://pyimagesearch.com/2021/08/23/your-first-ocr-project-with-tesseract-and-python/
