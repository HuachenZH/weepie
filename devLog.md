# Development logs

## info
- an article: https://nanonets.com/blog/ocr-with-tesseract/
- another article: https://pyimagesearch.com/2021/08/23/your-first-ocr-project-with-tesseract-and-python/


## Feature 3: extract video of CAD.
It's a bit hard to extract frames from the video of CAD because the images are not fixed, the presentor was scrolling all the time.  

__Solution__: iterate the video two times. The first time weepie will compare each frame with previous frames, if they are different, then it means it's scrolling. If it's stable for five or ten frames, then it's fixed. Note the frame pts.  
THen iterate for the second time and extract noted frames.

To resume:  
Study the bottom part of arr image, it seems that when the image change, the bottom part of matrix will also changes.  
To do so, you compare with numpy arrays directly.
I need to learn the "frame" object of pyav



## To improve / future work
- in `delete_duplicate.py`, the function `is_the_same` is built. You can build another one, is_similar, calculate the error between two matrices, return true of error is smaller than the threshold. 
- in `delete_duplicate.py`, the function `is_similar` can be much improved. For the moment lots of duplicates will be returned
- for unsure OCR, give at which time (min, sec) of the video
- find a way to determine similar texts
- hrsd: the answers are not written, they are shown in different color
- cad: in the video, the presenter scrolls a pdt....


## 自己挖的坑
- in the folder `data/img/`, images should be named like "frame_1.jpg", "frame_100.jpg"



to resume:  
- extract_text.py, now i have the list, join it into text
- in each question, add at which second it is appeared