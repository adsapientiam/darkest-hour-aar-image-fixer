import pathlib
from tkinter import filedialog, Tk, StringVar, Label, Button
from image_hex_converter import convert_img

def browse_button():
    global folder_path
    filename = filedialog.askdirectory() 
    folder_path.set(filename)

def fix_imgs(folder):
    pass

window = Tk()
folder_path = StringVar()

confirm = Button(text="Select", command=lambda: fix_imgs(folder_path.get()))
confirm.grid(row=0, column=1)
browser = Button(text="Browse", command=browse_button)
browser.grid(row=0,column=2)
lbl = Label(master=window, textvariable=folder_path)
lbl.grid(row=0, column=3)

window.title("Pick your image folder")

window.mainloop()

