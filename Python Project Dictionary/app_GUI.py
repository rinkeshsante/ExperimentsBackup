# python dictonary file

from difflib import get_close_matches
from json import load
#import tkinter as tk

from tkinter import *
# loading dictionary to memory
file = open('data.json', 'r')
data = load(file)
file.close()

# fuction declaration


def translate():
    output.delete(0, END)
    w = entry_key.get()
    w = w.lower()  # converting to lowercase
    try:
        write(data[w])
    except:

        # list of possible matches max lenghth 3
        match = get_close_matches(w, data.keys())

        if len(match) > 0:

            yes_btn['state'] = NORMAL
            no_btn['state'] = NORMAL

            # looping for each item in list
            for item in match:
                write(["Did you mean %s indtead ?" % item])
            else:
                return ["try othe word"]
        else:
            return ["word don't exist"]


def yes():
    print('yes')


def no():
    print('no')


def write(s):
    for y in s:
        output.insert(END, y)

# output / GUI


app = Tk()

# search space

search_key = StringVar()
entry_key = Entry(app, textvariable=search_key)
entry_key.grid(row=0, column=0, padx=20, pady=20)

# output
output = Listbox(app, height=8, width=50)
output.grid(row=1, column=0, columnspan=3, rowspan=10, pady=20, padx=20)
scrollbar = Scrollbar(app)
scrollbar.grid(row=1, column=3)
output.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=output.yview)

# buttons

search_btn = Button(app, text="Search", command=translate)
search_btn.grid(row=0, column=1)

yes_btn = Button(app, text="Yes", command=yes)
yes_btn.grid(row=11, column=0)
yes_btn['state'] = DISABLED

no_btn = Button(app, text="No", command=no)
no_btn.grid(row=11, column=1)
no_btn['state'] = DISABLED

app.title('Dictionary')
app.geometry('400x300')


app.mainloop()
