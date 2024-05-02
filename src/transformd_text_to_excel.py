import pandas as pd
import re

import pdb



def read_text(path_text:str) -> str:
    with open(path_text) as f:
        return f.read()



def prune_whole_doc(str_doc) -> str:
    """Prune the whole doc, replace and delete some string.
    Delete "xx min xx seconds", delete "most voted".
    Replace the whole line of "Next question is " by %>% and start_flag.
    Replace "correct answer is" by answer_flag.

            Parameters:
                    doc (str): Each question+choice+answer between two %>%.

            Returns:
                    doc (str): Pruned doc.
    """
    # Remove legacy "%>%"
    pattern = "%>%"
    str_doc = re.sub(pattern, "", str_doc)
    # Replace the whole line of "NEXT QUESTION IS ..." by start flag
    # and start_flag can be used to separate different questions
    pattern = "^NEXT.*$"
    str_doc = re.sub(pattern, "%>%\n\nstart_flag", str_doc, flags=re.MULTILINE)
    return str_doc



def prune_doc(doc:str) -> str:
    """Prune doc, replace and delete some string.
    Delete "xx min xx seconds", delete "most voted".
    Replace the whole line of "Next question is " by start flag.

            Parameters:
                    doc (str): Each question+choice+answer between two %>%.

            Returns:
                    doc (str): Pruned doc.
    """
    # replace the whole line of "NEXT QUESTION IS ..." by start flag
    pattern = "^NEXT.*$"
    doc = re.sub(pattern, "start_flag", doc, flags=re.MULTILINE)
    # i no longer need "xx min xx seconds"
    pattern = "^.*min.*seconds$"
    doc = re.sub(pattern, "", doc, flags=re.MULTILINE | re.IGNORECASE)
    # Replace "CORRECT ANSWER IS ..." by answer flag
    pattern = "correct answer is"
    doc = re.sub(pattern, "answer_flag", doc, flags=re.IGNORECASE)
    # Delete "most voted"
    pattern = "most voted"
    doc = re.sub(pattern, "", doc, flags=re.IGNORECASE)   
    return doc



def retrieve_label(doc:str) -> str:
    """Retrieve label (the question body) from doc.

            Parameters:
                    doc (str): Each question+choice+answer between two %>%.

            Returns:
                    (str): The label. Return "error" if nothing was found.
    """
    # match the question label
    # From start flag until r"A.", it can contain any character including new line
    pattern = "start_flag(?:\n|\r|.)*A\."
    match = re.search(pattern, doc, re.MULTILINE)
    if match:
        str_label = match[0]
        # slice the heading "start_flag" and the tailing "A."
        str_label = str_label[len("start_flag") : -2]
        # replace newline by space then strip
        str_label = str_label.replace("\n", " ").replace("\r", " ").strip()
        # sometimes there are "\n+ A.", now you can find them by " +"
        str_label = str_label.replace(" +", "").strip()
        return str_label
    else:
        print("label not found")
        return "error"

        

def retrieve_question_choice(doc:str) -> list:
    """Retrieve question choices from doc.
    Number of question choice can vary from 3 to 8.

            Parameters:
                    doc (str): Each question+choice+answer between two %>%.

            Returns:
                    list_result (list): List of question choices. 
                    The first element is "A", the last is "H".
                    If the question choice does not exist, it will be "empty".
    """
    list_choice = ["A.", "B.", "C.", "D.", "E.", "F.", "G.", "H."]
    list_result = []
    flag_last_choice = False
    for i in range(len(list_choice)-1):
        # If the last iteration has already the last answer
        if flag_last_choice:
            # Fill list_result until "H."
            list_result += ["empty" for i in range(len(list_choice)-i-1)]
            break
        # if there is still next choice
        if list_choice[i+1] in doc:
            # Sorry i don't know how to use regex here, i fail to put single backslash in pattern
            str_question_choice = doc[doc.find(list_choice[i])+len(list_choice[i]) : doc.find(list_choice[i+1])]
        # if not, then there must be answer_flag
        else:
            str_question_choice = doc[doc.find(list_choice[i])+len(list_choice[i]) : doc.find("answer_flag")]
            # answer_flag is used
            flag_last_choice = True
        # replace newline by space then strip
        str_question_choice = str_question_choice.replace("\n", " ").replace("\r", " ").strip()
        list_result.append(str_question_choice)
    # It's rare but in case there's "H."
    if list_choice[len(list_choice)-1] in doc:
        str_question_choice = doc[doc.find(list_choice[i])+len(list_choice[i]) : doc.find("answer_flag")]
        str_question_choice = str_question_choice.replace("\n", " ").replace("\r", " ").strip()
        list_result.append(str_question_choice)
    else:
        list_result.append("empty")
    return list_result



def retrieving(str_doc:str):
    str_doc = prune_whole_doc(str_doc)
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
        # Operation on doc, delete and replace some string
        doc = prune_doc(doc)
        # Retrieve question label
        list_label.append(retrieve_label(doc))

        # Retrieve each choice. We assume that there are at least A and B
        list_result = retrieve_question_choice(doc)
        list_choice_1.append(list_result[0]) # A
        list_choice_2.append(list_result[1]) # B
        list_choice_3.append(list_result[2]) # C
        list_choice_4.append(list_result[3]) # D
        list_choice_5.append(list_result[4]) # E
        list_choice_6.append(list_result[5]) # F
        list_choice_7.append(list_result[6]) # G
        list_choice_8.append(list_result[7]) # H
        breakpoint()



def main():
    path_text = "../out/doc_cad0_truncated.txt"
    str_doc = read_text(path_text)
    retrieving(str_doc)



if __name__ == "__main__":
    main()


