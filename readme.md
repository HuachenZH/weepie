# Weepie
The weepies are always weepy.  


## Table of content
- [Description](#description)
- [Prepare environment](#prepare-environment)
- [Usage](#usage)


## Description
Weepie extract images from a video then extract texts from image.  
These two steps are executed separatly by two subprograms. For more details, see [Usage](#usage).


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
weepie -i file extractFrames [options] file  
- __Description__  
  - -i, --imageDirPath:  
  Path to the directory of images (where you want to store output extracted iamges). By default data/img/.
  - videoPath:  
  A mandatory argument, path to the file of video.  
  - -f, --frequency:  
  Frequency of extraction of images in seconds. By default 10 seconds.  
  - -s, --scrolling:  
  Put this flag if the video is not static powerpoint slides but a scrolling pdf. While using the -s flag, the -f (--frequency) will not be taken into account. With this flag, duplicated frames will not be extracted, so you don't need to execute delDupFrames.   
- __Examples__  
  - `$ python3 weepie.py extractFrames ../data/video/csa.mp4`  
  Extract images from the video file csa.mp4 and use default path to store images. Use the default frequency: extract image each 10 seconds.
  - `$ python3 weepie.py -i ../data/img/csa/ extractFrames ../data/video/csa.mp4 -f 20`  
  Extract images from the video file csa.mp4 and store images to ../data/img/csa/, extract images each 20 seconds.
  - `$ python3 weepie.py -i ../data/img/cad/ extractFrames ../data/video/cad.mp4 -s`  
  Extract images from the video file cad.mp4 and store images to ../data/img/cad/, duplicated images will not be extracted. In this case, the frequency no longer matters as each unique image will be extracted.


### Usage - delDupFrames (legacy)
```shell
$ python3 weepie.py -i <dir of images> delDupFrames 
```
- __Name__  
weepie delDupFrames - delete duplicated frames (images) in a folder.
- __SYNOPSIS__  
weepie -i file delDupFrames [options]  
- __Description__  
  - -i, --imageDirPath:  
  Path to the directory of images. Duplicated images in this directory will be deleted directly. By default data/img/.
  - -t, --threshold:  
  The threshold of determining whether an image is a duplicate. It is the value of MSE, smaller than this value, the two images will be considered as duplicate and the second match will be deleted. By default 2.
- __Examples__  
  - `$ python3 weepie.py -i ../data/img/csa/ delDupFrames`  
  Delete duplicated images in the folder ../data/img/csa/ and use the default value as threshold. There might still be two or three duplicated iamges but no image will be deleted accidently.
  - `$ python3 weepie.py -i ../data/img/csa/ delDupFrames -t 4`  
  Delete duplicated images in the folder ../data/img/csa/ and set 4 as threshold. With this value, there will be no more duplicated images, however two or three unique images will be deleted accidently.


### Usage - extractText
```shell
$ python3 weepie.py -i <dir or input images> extractText -o <dir of output txt>
```
- __Name__  
weepie extractText - extract text from images.
- __SYNOPSIS__  
weepie -i file extractText -o file  
- __Description__  
  - -i, --imageDirPath:  
  Path to the directory of images.  
  - -o, --outputPath:  
  Path to the output txt file.
- __Examples__  
  - `$ python3 weepie.py -i ../data/img/cad/ extractText -o ../out/cad.txt`
  Read images in ../data/img/cad/, extract text and write the txt file to ../out/cad.txt.  



## later...
to explain:
- MSE and threshold
- how to compare (list of image should be sorted)
- the -s flag

## Contributing