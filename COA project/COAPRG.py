from tkinter import *


'''
from tkinter.filedialog import askopenfilename
#askopenfilename()

import matplotlib.pyplot as plt
im = plt.imread(askopenfilename())

'''


def draw(arr, size=10):
    master = Tk()
    w = Canvas(master,
               width=500,
               height=300)
    w.pack()

    COLOR = ['#FF0000', '#FF3333', '#FF6666', '#FF9999', '#FFCCCC',
             '#CCE5FF', '#99CCFF', '#66B2FF', '#3399FF', '#0080FF']

    X = 0
    Y = 0

    for i in range(len(arr)):

        for j in range(len(arr[0])):
            w.create_rectangle(X, Y, X+size, Y+size,
                               fill=COLOR[arr[i][j]], outline=COLOR[arr[i][j]])
            X += size

        X = 0
        Y += size

    mainloop()


if __name__ == "__main__":
    arr = [
        [0, 1, 2, 4, 5, 5, 6],
        [1, 2, 4, 6, 7, 8, 8],
        [2, 3, 5, 7, 8, 8, 9],
        [4, 3, 5, 7, 8, 9, 9]
    ]
    draw(arr, 35)
