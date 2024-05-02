# Development logs

## info
- an article: https://nanonets.com/blog/ocr-with-tesseract/
- another article: https://pyimagesearch.com/2021/08/23/your-first-ocr-project-with-tesseract-and-python/


## Feature 3: extract video of CAD.
It's a bit hard to extract frames from the video of CAD because the images are not fixed, the presentor was scrolling all the time.  

__Solution__: iterate the video two times. The first time weepie will compare each frame with previous frames, if they are different, then it means it's scrolling. If it's stable for five or ten frames, then it's fixed. Note the frame pts.  
THen iterate for the second time and extract noted frames.


## Feature 4: extract text from hrsd.mp4
This video is a bit different: the correct answers are not written in text but shown in another color.  
I need to extract red text from black text.

It's harder than i thought. I need to make some image preprocessing:
- sharpen the image


## Feature 5: fill the excel template
columns in the template excel:
- "Certification"
- "Category"
- "Label"
- "Answers"
- " "
- "Réponse 1"
- "True/False" (put true of the answer is correct)
- "Réponse 2"
- "True/False"
- ...
- "Réponse 8"
- "True/False"

You need to find solution for:
- how to extract the label
- how to extract each "réponse"
- how to retrieve the correct answer

- it seems that in OCR, "next question is" is always well recognized, i can use this to separate questions.

## Encountered
- cv2 error: cv2.error: OpenCV(4.9.0) /io/opencv/modules/core/src/arithm.cpp:672: error: (-5:Bad argument) When the input arrays in add/subtract/multiply/divide functions have different types, the output array type must be explicitly specified in function 'arithm_op'
  - cause: `cv2.subtract(img1, img2)`, img1 and img2 are np.ndarray with diffrerent dtype
  - solution: use np.npdarray.astype(int) to convert arrays to same data type before calling cv2.subtract()

- argument (frequency) type error: if not specified, python will take input as string, even though you give an int.
  - In argparse, specify type=int

- i have "A" stocked to a variable, i want to append backslach and a dot to it and to use it as a regex pattern.  
I failed to append just a single backslash.


## To improve / future work
- ~~in `delete_duplicate.py`, the function `is_the_same` is built. You can build another one, is_similar, calculate the error between two matrices, return true of error is smaller than the threshold.~~
- in `delete_duplicate.py`, the function `is_similar` can be much improved. For the moment lots of duplicates will be returned
- ~~for unsure OCR, give at which time (min, sec) of the video~~ --> Done by adding the info into exif
- find a way to determine similar texts
- hrsd: the answers are not written, they are shown in different color
  - solution: image pre processing, color detection. If red, keep. Else, turn to white. Then OCR on the image, there will only be the correct answer on the image.
- ~~cad: in the video, the presenter scrolls a pdf....~~ --> Done by comparing frames before extraction 
- `extract_frame_simple` can be deprecated, as the new function is much more powerful
- preprocessing of image : [this post](https://stackoverflow.com/questions/37745519/use-pytesseract-ocr-to-recognize-text-from-an-image)


- sometimes "B" is recognized as "8"

## To resume
- reviewing `doc_cad0.txt`, search "resumehere"



## 自己挖的坑
- in the folder `data/img/`, images should be named like "frame_1.jpg", "frame_100.jpg"
- in `extract_text.py`, input image must have exif info, if not, error.

- in text:
  - the first answer must contains "A."
  - answers should start with an uppercase letter and a dot, eg "A.", "B."
  - different questions must be seperated by "%>%"
  - there will be start_flag and answer_flag





to_resume:
extract each questions

