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



## Usage
Weepie has three subprograms: `extractFrames`, `delDupFrames` and `extractText`.  
As the name indicates, there are three steps: 
1. Extract frames from the video. Weepie is not smart enough to tell which frame is different from others, so it extracts frames at a fix frequence, by default each ten seconds.
2. Delete duplicated frames. Compare the matrix of pixel of each frame then delete duplicated frames.  
3. Extract text from frames. OCR stuffs, done by pytesseract.  

### Usage - extractFrames
```shell
$ python3 weepie.py -i <dir of images> extractFrames <path to video>
```
- __Name__  
weepie extractFrames - extract frames from a video file.  
- __SYNOPSIS__  
weepie -i file [options] file  
- __Description__  
  - -i, --imageDirPath:  
  Path to the directory of images (where you want to store output extracted iamges). By default data/img/.
  - videoPath:  
  A mandatory argument, path to the file of video.  
  - -f, --frequency:  
  Frequency of extraction of images in seconds. By default 10 seconds.  
- __Examples__  
  - `$ python3 weepie.py extractFrames ../data/video/cad.mp4`
  - `$ python3 weepie.py -i ../data/img/cad/ extractFrames ../data/video/cad.mp4 -f 20`



## later...
to explain:
- MSE and threshold
- how to compare (list of image should be sorted)

## Contributing