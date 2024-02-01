from PIL import Image
import pytesseract
import cv2

import pdb



def extract_text():
    img = cv2.imread('../data/q1.jpg', 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img)
    return text


if __name__ == "__main__":
    extract_text()
    breakpoint()