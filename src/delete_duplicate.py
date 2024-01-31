import cv2
import os
import numpy as np
import re

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
    # Construct a list of dictionaries. 
    # Each dictionary has two key value pairs:
    # "name" : the filename
    # "order": the number extracted from filename

    # Construct list of dict
    list_dict = []
    pattern = "_[0-9]*\...."
    for filename in list_filenames:
        dict_filename = {}
        dict_filename["name"] = filename
        order = re.findall(pattern, filename)
        if len(order) > 1:
            raise Exception(f"There is an error with the filename {filename}, regex finds more than one matches with the pattern {pattern}.")
        try:
            dict_filename["order"] = int(order[0][1:-4]) # slice the heading "_" and tha tailing ".jpg"
        except:
            print(f"Regex finds no match in this filename: {filename}")
            continue
        list_dict.append(dict_filename)
    
    # Sort list of dict by the value of the key "order"
    sorted_list = sorted(list_dict, key=lambda x: x["order"])
    # Extract value of the key "name" into a new list
    sorted_filenames = [utena["name"]  for utena in sorted_list]
    return sorted_filenames



def find_duplicates(path_dir:str, sorted_filenames:list):
    # iterate through the list of sorted_filenames
    # compare one by one if images are the same
    list_filenames = get_filenames(path_dir)



def main():
    path_dir = "../data/img/"
    list_filenames = get_filenames(path_dir)
    sorted_filenames = sort_filenames(list_filenames)
    breakpoint()
    find_duplicates(path_dir, sorted_filenames)


if __name__ == "__main__":
    main()