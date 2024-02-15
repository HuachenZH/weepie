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



def extract_frame_simple(path_input:str, path_output_dir:str, freq:int) -> None:
    """Extract frames of a video with a certain frequency.

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
        with open(path_output_dir + filename, "rb") as f:
            my_image = Image(f)
        str_time = time_formatter(frame.pts * float(frame.time_base))
        my_image.set("datetime", str_time)
        with open(path_output_dir + filename, "wb") as new_f:
            new_f.write(my_image.get_file())

    print(f"{count} images are written to disk.")
    container.close()



def extract_frame_complex(path_input:str, path_output_dir:str) -> None:
    if path_output_dir[-1] != "/": path_output_dir += "/"
    container = av.open(path_input)
    # take first video stream
    stream = container.streams.video[0]
    
    # First iteration: find static frames
    freq = 2 # check frames for each 1 seconds
    num = 0
    prev = np.zeros(5)
    list_tmp = []
    breakpoint()
    for idx, frame in tqdm(enumerate(container.decode(stream))):
        if frame.pts % (freq/float(frame.time_base)) != 0:
            continue
        #if idx == 0: continue
        num = int(frame.pts / (freq/float(frame.time_base))) # equals int(idx/freq/10)
        arr = frame.to_ndarray()
        if idx != 0:
            #list_tmp.append((int(idx/freq/10), is_similar(prev, arr, 1)))
            list_tmp.append((int(idx/freq/10), mse(prev, arr)[0]))
        prev = copy.deepcopy(arr)
        #cv2.imwrite(f"../data/img/test_frame/item_{num}_arr.jpg", arr)
        #frame.to_image().save(f"../data/img/test_frame/item_{num}_img.jpg")
        if num > 50:
            breakpoint()
            return
    return


if __name__ == "__main__":
    fpath = "../data/video/cad.mp4"
    out_dir = "../data/img/cad/"
    freq = 10
    #extract_frame_simple(fpath, out_dir, freq)
    extract_frame_complex(fpath, out_dir)