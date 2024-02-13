import av
from exif import Image
from tqdm import tqdm

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



if __name__ == "__main__":
    fpath = "../data/video/csa.mp4"
    out_dir = "../data/img/"
    freq = 10
    extract_frame_simple(fpath, out_dir, freq)