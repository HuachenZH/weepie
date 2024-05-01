import pandas as pd
import re

import pdb



def read_text(path_text:str) -> str:
    with open(path_text) as f:
        return f.read()


def prune_doc(doc:str) -> str:
    # replace the whole line of "NEXT QUESTION IS ..." by start flag
    pattern = "^NEXT.*$"
    doc = re.sub(pattern, "start_flag", doc, flags=re.MULTILINE)
    # i no longer need "xx min xx seconds"
    pattern = "^.*min.*seconds$"
    doc = re.sub(pattern, "", doc, flags=re.MULTILINE | re.IGNORECASE)
    # Delete "most voted"
    pattern = "most voted"
    doc = re.sub(pattern, "", doc, flags=re.IGNORECASE)   
    return doc



def retrieve_label(doc:str) -> str:
    # match the question label
    # From start flag until r"A.", it can contain any character including new line
    pattern = "start_flag(?:\n|\r|.)*A\."
    match = re.search(pattern, doc, re.MULTILINE)
    if match:
        str_label = match[0]
        # slice the heading "start_flag" and the tailing "A."
        str_label = str_label[len("start_flag") : -2]
        # replace newline by space
        str_label = str_label.replace("\n", " ").replace("\r", " ").strip()
        # sometimes there are "\n+ A.", now you can find them by " +"
        str_label = str_label.replace(" +", "").strip()
        return str_label
    else:
        print("label not found")
        return "error"


def retrieving(str_doc:str):
    list_doc = str_doc.split("%>%")
    list_label = []
    list_answers = []

    list_choice_1 = [] # A
    list_flag_1 = []

    list_choice_2 = [] # B
    list_flag_2 = []

    list_choice_3 = [] # C
    list_flag_3 = []

    list_choice_4 = [] # D
    list_flag_4 = []

    list_choice_5 = [] # E
    list_flag_5 = []

    list_choice_6 = [] # F
    list_flag_6 = []

    list_choice_7 = [] # G
    list_flag_7 = []

    list_choice_8 = [] # H
    list_flag_8 = []

    for doc in list_doc:
        

        

        # Retrieve label
        list_label.append(retrieve_label(doc))

        # Retrieve each choice. We assume that there are at least A and B


    breakpoint()


def main():
    path_text = "../out/doc_cad0_truncated.txt"
    str_doc = read_text(path_text)
    retrieving(str_doc)

if __name__ == "__main__":
    main()


