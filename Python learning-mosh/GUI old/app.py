import tkinter as tk

# create window option
app = tk.Tk()


# add components

part_text = tk.StringVar()
part_label = tk.Label(app, text='part name',
                      font=('bold', 14), pady=20, padx=20)
part_label.grid(row=0, column=0, sticky=tk.W)

part_entry = tk.Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# add components

part_text = tk.StringVar()
part_label = tk.Label(app, text='part name',
                      font=('bold', 14), pady=20, padx=20)
part_label.grid(row=0, column=0, sticky=tk.W)

part_entry = tk.Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# add components

part_text = tk.StringVar()
part_label = tk.Label(app, text='part name',
                      font=('bold', 14), pady=20, padx=20)
part_label.grid(row=0, column=0, sticky=tk.W)

part_entry = tk.Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# add components

part_text = tk.StringVar()
part_label = tk.Label(app, text='part name',
                      font=('bold', 14), pady=20, padx=20)
part_label.grid(row=0, column=0, sticky=tk.W)

part_entry = tk.Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)


app.title('Store')
app.geometry('700x350')

# start programe
app.mainloop()
