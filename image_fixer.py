from PIL import Image
import os
#from os import listdir, path

def cut_img (img:Image)->Image:
    width, height = img.size
    return img.crop((259, 76, width, height))  # cuts out everything except map

def get_date(cur_img:Image)->list:
    color = cur_img.convert("RGB").getpixel((0, 48)) # color of first pixel under the upper black seperator line above the bar
    if color == (96, 96, 88): 
        cur_img_bytes = cur_img.tobytes()
        return iterate_chars("dhfull_chars") 
    elif color == (184, 180, 152): 
        cur_img_bytes = cur_img.tobytes()
        return iterate_chars("dhlite_chars")
    else: return None  
    
    def iterate_chars(char_folder:str)->list:
        nonlocal cur_img_bytes
        nonlocal cur_img

        temp_img = cur_img_bytes  # holds image value which gets minimized  
        date = [] 
        cur_char_folder = r"darkesthouraarimagefixer\%s" % char_folder
        
        for charname in os.listdir(cur_char_folder):  # maybe make months into own folder so it goes faster; actually just save the HEX values
            cur_char = Image.open(cur_char_folder + charname).tobytes()
            index_img = cur_img_bytes.index(cur_char)
            while cur_char in temp_img: 
                date.append((charname.split(".")[0], index_img))  
                temp_img[index_img:]
            temp_img = cur_img_bytes

            if len(date) == 11: break  # early break out if maxed out on data
        cur_img = cut_img(cur_img) 
        return date
   

def walk_folder(folder): 
    for filename in os.listdir(folder):
        cur_img = Image.open(folder+filename)
        new_filename = "".join([x[0] for x in sorted((get_date(cur_img)), key=lambda d: d[1])])  # sorts date as: HH MM Month Day Year; currently just mashes sorted list
        infilename = os.path.join(folder,filename)
        if not os.path.isfile(infilename): continue
        newname = new_filename + ".jpg" 
        os.rename(infilename, newname)
        
""" StackOverFlow answer 
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.grf', '.las')
       output = os.rename(infilename, newname)
"""
