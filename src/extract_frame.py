import cv2
import av
from exif import Image
from tqdm import tqdm
import numpy as np
import copy

from find_unique_frame import is_similar
from find_unique_frame import mse

import pdb


def time_formatter(time_seconds:float) -> str:
    """Format time.
    62 s --> 1 min 2 s
    4056 s --> 1 h 7 min 36 s

            Parameters:
                    time_seconds (float): the frame appears at which second.

            Returns:
                    (str)
    """
    if time_seconds < 3600:
        return f"{int(time_seconds//60)} min {int(time_seconds%60)} seconds"
    else:
        return f"{int(time_seconds//3600)} h {int(time_seconds%3600//60)} min {int(time_seconds%3600%60)} seconds"



def modify_exif(path_output_dir:str, filename:str, pts:int, time_base) -> None:
    """Modify the exif of an image. Add the timestamp (image appeared at which second of the video)
    to the 'datatime' field of the exif.
 
            Parameters:
                    path_output_dir (str): path to the directory of output images.
 
                    filename (str): file name of the output image.
 
                    pts (int): the presentation timestamp.
 
                    time_base (fractions.Fraction): the unit of time in which timestamps are expressed.
  
            Returns:
                    None. Images are written to disk directly.
    """
    with open(path_output_dir + filename, "rb") as f:
        my_image = Image(f)
        str_time = time_formatter(pts * float(time_base))
        my_image.set("datetime", str_time)
        with open(path_output_dir + filename, "wb") as new_f:
            new_f.write(my_image.get_file())
    return



def extract_frame_simple(path_input:str, path_output_dir:str, freq:int) -> None:
    """Extract frames of a video with a certain frequency.
    Use case is simple: only static images in the video.

            Parameters:
                    path_input (str): Path to the input mp4 file.

                    path_output_dir (str): Path to the output directory (not file).

                    freq (int): For every how many seconds you want to extract frame. 
                    e.g. 30 for 30 seconds.

            Returns:
                    None. Changes are written to disk directly.
    """
    if path_output_dir[-1] != "/": path_output_dir += "/"
    container = av.open(path_input)
    # take first video stream
    stream = container.streams.video[0]
    # get video fps
    average_fps = int(stream.average_rate)
    
    count = 0
    for idx, frame in tqdm(enumerate(container.decode(stream))):
        # Save the frame to jpg with pyav
        if frame.pts % (freq/float(frame.time_base)) != 0:
            continue
        count += 1
        filename = f"frame_{count}.jpg"
        frame.to_image().save(path_output_dir + filename)
        # Re-read the image to modify its exif
        modify_exif(path_output_dir, filename, frame.pts, frame.time_base)

    print(f"{count} images are written to disk.")
    container.close()



def extract_frame_complex(path_input:str, path_output_dir:str) -> None:
    """Extract frames of a video.
    Use case is complex: scrolling in the video.

            Parameters:
                    path_input (str): Path to the input mp4 file.

                    path_output_dir (str): Path to the output directory (not file).

            Returns:
                    None. Changes are written to disk directly.
    """
    if path_output_dir[-1] != "/": path_output_dir += "/"
    container = av.open(path_input)
    # take first video stream
    stream = container.streams.video[0]
    
    # First iteration: find static frames
    freq = 2 # check frames for each 2 seconds
    num = 0
    # Initialize a "zero" frame as the first "previous" frame
    for frame in container.decode(stream):
        prev = np.zeros(frame.to_ndarray().shape).astype(int)
        break

    for idx, frame in tqdm(enumerate(container.decode(stream))):
        # Skip the iteration if not at each x second. x is the frequency.
        if frame.pts % (freq/float(frame.time_base)) != 0:
            continue
        num = int(frame.pts / (freq/float(frame.time_base))) # equals int(idx/freq/10)
        # num * freq = at which second of the video.
        arr = frame.to_ndarray().astype(int)
        # Save image to disk if the current frame is different from the previous frame
        if mse(prev, arr)[0] > 3:
            #cv2.imwrite(f"../data/img/test_frame/item_{num}_arr.jpg", arr)
            filename = f"frame_{num}.jpg"
            frame.to_image().save(path_output_dir + filename)
            modify_exif(path_output_dir, filename, frame.pts, frame.time_base)
        prev = copy.deepcopy(arr)



if __name__ == "__main__":
    fpath = "../data/video/cad.mp4"
    out_dir = "../data/img/cad/"
    freq = 10
    #extract_frame_simple(fpath, out_dir, freq)
    extract_frame_complex(fpath, out_dir)