# Weepie
The weepies are always weepy.  


## 0. Table of content
- [Description](#description)
- [Prepare environment](#prepare-environment)
- [Usage](#usage)


## 1. Description
Weepie extract images from a video then extract texts from image.  
These two steps are executed separatly by three subparsers (in fact they can be improved into two). For more details, see [Usage](#usage).


## 2. Prepare environment
### pyenv
First you need pyenv to manage your python versions. This project is build with python 3.11.4.  
To install pyenv, follow the doc on their [github](https://github.com/pyenv/pyenv).

### pyenv virtualenv
It is recommended to use a virtual environment to manage packages. First of all, cd to weepie/.
```shell
# Specify python version of the current folder
$ pyenv local 3.11.4

# create a virtual env called "weepie" with version 3.11.4.
# It is suggested that the virtual env and the project use the same name.
$ pyenv virtualenv 3.11.4 weepie

# Activate virtual env.
# Normally if you pyenv is installed correctly, the virutal env will
# be activated automatically each time you cd to the directory.
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



## 3. Usage
Weepie has three subparsers: `extractFrames`, `delDupFrames` and `extractText`. (And the script find_unique_frame.py is used by extractFrames, normally you won't use it directly.)   
As the name indicates, there are three steps: 
1. Extract frames from the video. Weepie is not smart enough to tell which frame is different from others, so it extracts frames at a fix frequence, by default each ten seconds. --> It is now smart enough (by calculating mse) to tell whether two frames are the same, however mse is not smart enough to tell whether the texts are the same.
2. (This step is not truely necessary if you put -s flag in extractFrames) Find unique frames then delete duplicated frames. Compare the matrix of pixel of each frame then delete duplicated frames.  
3. Extract text from frames. OCR stuffs, done by pytesseract. It is possible to fine-tune the tesseract model, but i don't think i have enough time to do so.  



### Usage - extractFrames
```shell
$ python3 weepie.py extractFrames -i <dir of images>  <path to video>
```
- __Name__  
weepie extractFrames - extract frames from a video file.  
- __SYNOPSIS__  
weepie -i file extractFrames [options] file  
- __Description__  
  - -i, --imageDirPath:  
  Path to the directory of images (where you want to store output extracted iamges). By default data/img/.
  - videoPath:  
  A mandatory (and positional) argument, path to the file of video. It is a postional argument but it can be placed whereever you want, since all others are optional arguments.  
  - -f, --frequency:  
  Frequency of extraction of images in seconds. By default 10 seconds.  
  - -s, --scrolling:  
  Put this flag if the video is not static powerpoint slides but a scrolling pdf. While using the -s flag, the -f (--frequency) will not be taken into account. With this flag, duplicated frames will not be extracted, so you don't need to execute delDupFrames.   
- __Examples__  
  - `$ python3 weepie.py extractFrames  ../data/video/csa.mp4`  
  Extract images from the video file csa.mp4 and use default path to store images. Use the default frequency: extract image each 10 seconds.
  - `$ python3 weepie.py extractFrames -i ../data/img/csa/ ../data/video/csa.mp4 -f 20`  
  Extract images from the video file csa.mp4 and store images to ../data/img/csa/, extract images each 20 seconds.
  - `$ python3 weepie.py extractFrames -i ../data/img/cad/ ../data/video/cad.mp4 -s`  
  Extract images from the video file cad.mp4 and store images to ../data/img/cad/, duplicated images will not be extracted. In this case, the frequency no longer matters as each unique image will be extracted.


### Usage - delDupFrames (legacy)
```shell
$ python3 weepie.py delDupFrames -i <dir of images> 
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
  - `$ python3 weepie.py delDupFrames -i ../data/img/csa/`  
  Delete duplicated images in the folder ../data/img/csa/ and use the default value as threshold. There might still be two or three duplicated iamges but no image will be deleted accidently.
  - `$ python3 weepie.py delDupFrames -i ../data/img/csa/ -t 4`  
  Delete duplicated images in the folder ../data/img/csa/ and set 4 as threshold. With this value, there will be no more duplicated images, however two or three unique images will be deleted accidently.


### Usage - extractText
```shell
$ python3 weepie.py extractText -i <dir or input images> -o <dir of output txt>
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
  - `$ python3 weepie.py extractText -i ../data/img/cad/ -o ../out/cad.txt`  
  Read images in ../data/img/cad/, extract text and write the txt file to ../out/cad.txt.  



## later...
to explain:
- MSE and threshold
- how to compare (list of image should be sorted)
- the -s flag

## Contributing