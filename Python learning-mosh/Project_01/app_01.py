# python dictonary file

from difflib import get_close_matches
from json import load

file = open('data.json', 'r')
data = load(file)
file.close()

# output is list 
def translate(w):
    w = w.lower()  # converting to lowercase
    try:
        return data[w]
    except:
        # list of possible matches max lenghth 3
        match = get_close_matches(w, data.keys())
        if len(match) > 0:
            # looping for each item in list
            for item in match:
                ans = input("Did you mean %s indtead ? (y or n) : " % item)[0]
                if ans == 'y':
                    return data[item]
            else:
                return ["try othe word"]
        else:
            return ["word don't exist"]

if __name__ == "__main__":    
    word = input("enter word : ")

    for item in translate(word):  # output is list
        print(item)
