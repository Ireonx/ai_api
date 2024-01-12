import re
import copy
def is_an_image_prompt(message):
    backup = copy.copy(message)
    verbs = ["generate ", "create ", "make ", "draw" ]
    nouns = ["picture ", "image", "drawing", "photo "]
    prepositions = ["of ", "with "]
    verb_in_message = ""
    noun_in_message = ""
    preposition_in_message = ""
    for verb in verbs:
        if verb in message:
            verb_in_message = verb
            message = re.split(f'({verb})', message)[2]
    for noun in nouns:
        if noun in message[:9]:
            noun_in_message = noun
            message = re.split(f'({noun})', message)[2]
    for prep in prepositions:
        if prep in message[:5]:
            preposition_in_message = prep
            message = re.split(f'({prep})', message)[2]
    
    if any(len(x) == 0 for x in [verb_in_message, noun_in_message, preposition_in_message]):
        return False, backup
    else: 
        return True, message

if __name__ == "__main__":
    msg = "Please draw an image of elven mage fighting her enemies"
    print(is_an_image_prompt(msg))