import cv2
import os
import numpy as np

import pdb


def is_the_same(image1:np.ndarray, image2:np.ndarray) -> bool:
    """Returns true if two images are exactly the same"""
    return image1.shape == image2.shape and not(np.bitwise_xor(image1,image2).any())


def get_filenames(path_dir:str) -> list:
    """Get name of files in a folder. They are suppose to be like frame_1.jpg.

            Parameters:
                    path_dir (str): Path to the folder.

            Returns:
                    list_filenames (list): a list of unsorted filenames
    """
    list_filenames = []
    for filename in os.listdir(path_dir):
        f = os.path.join(path_dir, filename)
        # Make sure it's a file but not directory
        if os.path.isfile(f):
            list_filenames.append(f.split("/").pop())
    return list_filenames



def sort_filenames(list_filenames:list):
    return



def find_duplicates(path_dir:str):
    list_filenames = get_filenames(path_dir)
    breakpoint()



if __name__ == "__main__":
    path_dir = "../data/img/"
    list_filenames = get_filenames(path_dir)
    list_filenames = sort_filenames(list_filenames)
    find_duplicates(path_dir)