import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def transalte(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input(f"Did you mean {get_close_matches(word, data.keys())[0]} ? If yes enter Y or N if no: ")
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist,Please double check it"
        else:
            return "sorry,did not got any match"
    else:
        return "spelling Error,please Double check it."


word = input("Enter Word->")
output = transalte(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
