import cv2
import os
import numpy as np
import re

from tqdm import tqdm
import pdb


def is_the_same(image1:np.ndarray, image2:np.ndarray) -> bool:
    """Returns true if two images are exactly the same"""
    return image1.shape == image2.shape and not(np.bitwise_xor(image1,image2).any())


def mse(img1:np.ndarray, img2:np.ndarray) -> (float, np.ndarray):
    """Calculate the Mean Square Error between two images.
    The two images should be converted into greyscale beforehand.

            Parameters:
                    img1 (np.ndarray): First image, should be in greyscale.

                    img2 (np.ndarray): Second image, should be in greyscale.

            Returns:
                    mse, diff (tuple(float, np.ndarray)): mse and difference of two matrice.
    """
    h, w = img1.shape
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff**2)
    mse = err/(float(h*w))
    return mse, diff



def is_similar(image1:np.ndarray, image2:np.ndarray) -> bool:
    """Determines whether two images are similar.
    Determined by the mse of the pixel values of the two images.
    The threshold is 2 by default.

            Parameters:
                    image1 (np.ndarray): First image, should be in greyscale.

                    image2 (np.ndarray): Second image, should be in greyscale.

            Returns:
                    (bool): True if two images are similar.
    """
    error, diff = mse(image1, image2)
    if error < 2:
        return True
    else:
        return False



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
    """Sort list of filenames by the number inside filename by ascending order.\n
    Before sort: frame_1.jpg  frame_100.jpg  frame_2.jpg
    After sort:  frame_1.jpg  frame_2.jpg    frame_100.jpg

            Parameters:
                    list_filenames (list): list of filenames, not sorted.

            Returns:
                    sorted_filenames (list): sorted list of filenames
    """
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



def compare_frames_in_list(path_dir:str, sorted_filenames:list):
    # iterate through the list of sorted_filenames
    # compare one by one if images are the same
    list_uniq = []
    list_uniq.append(sorted_filenames[0])
    for i in tqdm(range(len(sorted_filenames)-1)):
        image1 = cv2.imread(path_dir + sorted_filenames[i])
        image2 = cv2.imread(path_dir + sorted_filenames[i+1])
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        #if is_the_same(image1, image2):
        #    list_duplicate.append(image2)
        if not is_similar(image1, image2):
            list_uniq.append(sorted_filenames[i+1])
    return list_uniq



def find_unique_frames(path_dir:str):
    list_filenames = get_filenames(path_dir)
    sorted_filenames = sort_filenames(list_filenames)
    list_uniq = compare_frames_in_list(path_dir, sorted_filenames)
    return list_uniq



def main():
    path_dir = "../data/img/"
    res = find_unique_frames(path_dir)
    print(res)


if __name__ == "__main__":
    main()