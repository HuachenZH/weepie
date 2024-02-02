import cv2
import os
import numpy as np
import re

from tqdm import tqdm
import pdb

from find_unique_frame import *



def compare_frames_in_list_for_deletion(path_dir:str, sorted_filenames:list):
    # iterate through the list of sorted_filenames
    # compare one by one if images are the same
    list_dup = []
    print("Comparing frames...")
    for i in tqdm(range(len(sorted_filenames)-1)):
        image1 = cv2.imread(path_dir + sorted_filenames[i])
        image2 = cv2.imread(path_dir + sorted_filenames[i+1])
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        if is_similar(image1, image2):
            list_dup.append(sorted_filenames[i+1])
    print("Done")
    return list_dup



def find_duplicated_frames(path_dir:str) -> list:
    list_filenames = get_filenames(path_dir)
    sorted_filenames = sort_filenames(list_filenames)
    list_dup = compare_frames_in_list_for_deletion(path_dir, sorted_filenames)
    print(f"Found {len(list_dup)} duplicated frames")
    return list_dup



def delete_duplicated_frames(path_dir:str, list_dup:list) -> None:
    if len(list_dup) == 0:
        print("Nothing to be deleted")
        return
    print("Deleting duplicated frames...")
    for duplicate in tqdm(list_dup):
        if os.path.exists(path_dir+duplicate):
            os.remove(path_dir+duplicate)
            print(f"File removed: {duplicate}")
        else:
            print(f"The file {duplicate} is not found.")
    print("Done")



def main():
    path_dir = "../data/img/"
    list_dup = find_duplicated_frames(path_dir)
    delete_duplicated_frames(path_dir, list_dup)


if __name__ == "__main__":
    main()