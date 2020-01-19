from tkinter import filedialog, Tk, StringVar, Label, Button
from image_fixer import walk_folder

def browse_button():
    global folder_path
    filename = filedialog.askdirectory() # make so this starts off in a Darkest Hour folder
    folder_path.set(filename)
       
window = Tk()
folder_path = StringVar()

confirm = Button(text="Select", command=lambda: walk_folder(folder_path.get()))
confirm.grid(row=0, column=1)
browser = Button(text="Browse", command=browse_button)
browser.grid(row=0,column=2)
lbl = Label(master=window, textvariable=folder_path)
lbl.grid(row=0, column=3)

window.title("Pick your image folder")

window.mainloop()

