import av
from tqdm import tqdm

import pdb


def extract_frame(path_input:str, path_output_dir:str, freq:int) -> None:
    """Extract frames of a video with a certain frequency.

            Parameters:
                    path_input (str): Path to the input mp4 file.

                    path_output_dir (str): Path to the output directory (not file).

                    freq (int): For every how many seconds you want to extract frame. 
                    e.g. 30 for 30 seconds.

            Returns:
                    None. Changes are written to disk directly.
    """
    container = av.open(path_input)
    # take first video stream
    stream = container.streams.video[0]
    # get video fps
    average_fps = int(stream.average_rate)
    
    count = 0
    for idx, frame in tqdm(enumerate(container.decode(stream))):
        #if idx % average_fps != 0:
        if frame.pts % (freq/float(frame.time_base)) != 0:
            continue
        count += 1
        frame.to_image().save(path_output_dir + f"frame_{count}.jpg")
    print(f"{count} images are written to disk.")
    
    #for packet in container.demux(stream):
    #        for frame in packet.decode():
    #            # Check if the frame timestamp is a multiple of the interval
    #            if frame.pts % 30 == 0:
    #                # Save the frame as an image (e.g., using Pillow)
    #                frame.to_image().save(path_output_dir + f"frame_{frame.pts}.jpg")
    #            breakpoint()
    
    container.close()



if __name__ == "__main__":
    fpath = "../data/video/csa.mp4"
    out_dir = "../data/img/"
    freq = 10
    extract_frame(fpath, out_dir, freq)