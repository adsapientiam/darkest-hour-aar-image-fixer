from PIL import Image
import os, sys
#from os import listdir, path

def cut_image():
    pass

def sort_date(d:list)->str:
    pass

def get_date(file:str)->list:
    cur_img = Image.open(file).tobytes()
    temp_img = cur_img  # holds image value but gets minimized  

    def iterate_chars(char_folder:str)->list:
        nonlocal cur_img
        date = [] # HH MM Month Day:int Year, max: 2, 2, 1, 2, 4
        cur_char_folder = r"darkesthouraarimagefixer\%s" % char_folder
        
        for charname in os.listdir(cur_char_folder):  # maybe make months into own folder so it goes faster
            cur_char = Image.open(cur_char_folder + charname).tobytes()
            index_img = cur_img.index(cur_char)
            try: 
                date.append((charname.split(".")[0], index_img))
                temp_img[index_img:]
                continue
            except ValueError:  # if no index is found
                temp_img = cur_img

            if len(date) == 11: break  # early break out if maxed out stats
        return date
   
    try:
        return (iterate_chars("dhlite_chars") if cur_img.convert("RGB").getpixel((826,55)) != (126, 126, 126)  # Checks if the bar's color of upper dot of comma is grey, as in DH Full
               else iterate_chars("dhfull_chars"))
    except ValueError: # whenever file lacks both dhfull and dhlite characthers, return nothing
        return 
    
    # check color over menubar around date pause 

def walk_folder(folder): 
    for filename in os.listdir(folder):
        
        sort_date(get_date(filename))
        infilename = os.path.join(folder,filename)
        if not os.path.isfile(infilename): continue
        oldbase = os.path.splitext(filename)
        newname = infilename.replace('.bmp', '.jpg')
        output = os.rename(infilename, newname)


