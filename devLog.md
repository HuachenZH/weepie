# Development logs

## info
- an article: https://nanonets.com/blog/ocr-with-tesseract/
- another article: https://pyimagesearch.com/2021/08/23/your-first-ocr-project-with-tesseract-and-python/


## Feature 3: extract video of CAD.
It's a bit hard to extract frames from the video of CAD because the images are not fixed, the presentor was scrolling all the time.  

__Solution__: iterate the video two times. The first time weepie will compare each frame with previous frames, if they are different, then it means it's scrolling. If it's stable for five or ten frames, then it's fixed. Note the frame pts.  
THen iterate for the second time and extract noted frames.

To resume:  


## Encountered
- cv2 error: cv2.error: OpenCV(4.9.0) /io/opencv/modules/core/src/arithm.cpp:672: error: (-5:Bad argument) When the input arrays in add/subtract/multiply/divide functions have different types, the output array type must be explicitly specified in function 'arithm_op'
  - cause: `cv2.subtract(img1, img2)`, img1 and img2 are np.ndarray with diffrerent dtype
  - solution: use np.npdarray.astype(int) to convert arrays to same data type before calling cv2.subtract()


## To improve / future work
- in `delete_duplicate.py`, the function `is_the_same` is built. You can build another one, is_similar, calculate the error between two matrices, return true of error is smaller than the threshold. 
- in `delete_duplicate.py`, the function `is_similar` can be much improved. For the moment lots of duplicates will be returned
- for unsure OCR, give at which time (min, sec) of the video
- find a way to determine similar texts
- hrsd: the answers are not written, they are shown in different color
- cad: in the video, the presenter scrolls a pdf....
- `extract_frame_simple` can be deprecated, as the new function is much more powerful

## 自己挖的坑
- in the folder `data/img/`, images should be named like "frame_1.jpg", "frame_100.jpg"
- in `extract_text.py`, input image must have exif info, if not, error.


