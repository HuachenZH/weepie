import pandas as pd
import re

import pdb



def read_text(path_text:str) -> str:
    with open(path_text) as f:
        return f.read()



def prune_text(str_doc:str):
    list_doc = str_doc.split("%>%")
    list_label = []
    for doc in list_doc:
        # replace "NEXT QUESTION IS" by start flag
        pattern = "^NEXT.*$"
        doc = re.sub(pattern, "start_flag", doc, flags=re.MULTILINE)
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
            list_label.append(str_label)
        else:
            print("label not found")
            list_label.append("error")
            breakpoint()
        # remove "xx min xx seconds"
        pattern = "^.*min.*sec.*$"
        doc = re.sub(pattern, "", doc)

    breakpoint()


def main():
    path_text = "../out/doc_cad0_truncated.txt"
    str_doc = read_text(path_text)
    prune_text(str_doc)

if __name__ == "__main__":
    main()


