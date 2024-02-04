from PIL import Image
import pytesseract
import cv2
import os
import exif

from find_unique_frame import sort_filenames

from tqdm import tqdm
import pdb



def extract_text(image_path_filename:str) -> str:
    """Extract texts in an image using Tesseract OCR.

            Parameters:
                    image_path_filename (str): path and filename to the image.

            Returns:
                    text (str)
    """
    img = cv2.imread(image_path_filename, 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img)
    return text



def build_doc(path_dir:str) -> (list, list):
    """Iterate through all images in the folder and extract text.

            Parameters:
                    path_dir (str): path to the folder of images.

            Returns:
                    (list, list): a tuple of lists. 
                    The first one: list of text extracted.
                    The second one: list of timestamp of each image.
    """
    list_doc = []
    list_timestamp = []
    list_doc.append("placeholder")
    list_timestamp.append("placeholder")
    count_duplicate = 0
    sorted_filenames = sort_filenames(os.listdir(path_dir))
    print("OCR in progress... keep an eye on the temperature of your GPU, don't burn it.")
    print("If you feel your pc hotter than 12 hours of minecraft, hit ctrl+C to halt the program.")
    for filename in tqdm(sorted_filenames):
        f = os.path.join(path_dir, filename)
        if os.path.isfile(f):
            text = extract_text(f)
            # Discard the image if duplicated
            if text == list_doc[-1]:
                count_duplicate -=- 1
            else:
                list_doc.append(text)
                # Get time information from EXIF
                with open(f, "rb") as image_file:
                    my_image = exif.Image(image_file)
                time = my_image.get("datetime")
                list_timestamp.append(time)
    list_doc = list_doc[1::] # shift the placeholder
    list_timestamp = list_timestamp[1::]
    print(f"Found {count_duplicate} duplicated questions.")
    return list_doc, list_timestamp



def write_doc(path_dir:str, out_path:str) -> None:
    """Extract text from images and write it to disk.

            Parameters:
                    path_dir (str): path to the folder of images.
 
                    out_path (str): path and filename to the output text.

            Returns:
                    None. File written to disk directly.
    """
    list_doc, list_timestamp = build_doc(path_dir)
    list_doc_timestamp = [doc+timestamp+"\n" for doc, timestamp in zip(list_doc, list_timestamp)]
    str_doc_timestamp = "\n%>%\n\n".join(list_doc_timestamp)
    with open(out_path, "w+") as f:
        f.write(str_doc_timestamp)
        print(f"File written to disk: {out_path}")


if __name__ == "__main__":
    path_dir = "../data/img/"
    out_path = "../data/doc_csa.txt"
    write_doc(path_dir, out_path)