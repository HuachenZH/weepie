import pandas as pd

import pdb



def read_text(path_text:str) -> str:
    with open(path_text) as f:
        return f.read()



def main():
    path_text = "../out/doc_cad0_truncated.txt"
    text = read_text(path_text)
    breakpoint()

if __name__ == "__main__":
    main()