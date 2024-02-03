from PIL import Image
import pytesseract
import cv2
import os

from find_unique_frame import sort_filenames

from tqdm import tqdm
import pdb



def extract_text(image_path_filename:str):
    img = cv2.imread(image_path_filename, 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img)
    return text



def build_doc(path_dir:str):
    list_doc = []
    list_doc.append("placeholder")
    count_duplicate = 0
    sorted_filenames = sort_filenames(os.listdir(path_dir))
    print("OCR in progress... keep an eye on the temperature of your GPU, don't burn it.")
    for filename in tqdm(sorted_filenames):
        f = os.path.join(path_dir, filename)
        if os.path.isfile(f):
            text = extract_text(f)
            if text == list_doc[-1]:
                count_dupplicate -=- 1
            else:
                list_doc.append(text)
    list_doc = list_doc[1::] # shift the placeholder
    print(f"Found {count_duplicate} duplicated questions.")
    breakpoint()
    return list_doc



if __name__ == "__main__":
    path_dir = "../data/img/"
    build_doc(path_dir)