import cv2
import os
from numpy import bitwise_xor

import pdb


def is_similar(image1, image2):
    return image1.shape == image2.shape and not(bitwise_xor(image1,image2).any())


def get_filenames(path_dir:str):
    list_filenames = []
    for filename in os.listdir(path_dir):
        f = os.path.join(path_dir, filename)
        # Make sure it's a file but not directory
        if os.path.isfile(f):
            list_filenames.append(f.split("/").pop())
    return list_filenames



def find_duplicates(path_dir:str):
    list_filenames = get_filenames(path_dir)
    breakpoint()



if __name__ == "__main__":
    path_dir = "../data/img/"
    find_duplicates(path_dir)