from PIL import Image
import os
from char_values import chars_lite, chars_full

def get_date(cur_img:Image)->list:
    color = cur_img.convert("RGB").getpixel((0, 48)) # color of first pixel under the upper black seperator line above the bar
    if color == (96, 96, 88): 
        cur_img_data = list(cur_img.crop(821,53, 946, 63).getdata()) # everything but date bar is cut out
        return iterate_chars(1) 
    elif color == (184, 180, 152): 
        cur_img_data = list(cur_img.crop(800, 53, 925, 63).getdata())  # not sure if this adequately cuts out all of the needed information
        return iterate_chars()
    else: return None  
    
    def iterate_chars(is_full:bool=False)->list:  
        nonlocal cur_img
        nonlocal cur_img_data
        
        temp_img = cur_img_data  # editable copy
        
        date = [] 
        cur_chars = chars_full if is_full else chars_lite

        for i, cur_char in enumerate(cur_chars):
            while cur_char in temp_img: 
                img_index = temp_img.index(cur_char)
                date.append(([0,1,2,3,4,5,6,7,8,9, "January", "February", "Mars", "April", "May", "June", "July", "August", "September", "October", "November", "December"][i], img_index))  
                temp_img = temp_img[img_index:]
            temp_img = cur_img_data

            if len(date) == 11: break  # early break out if maxed out on data
        cur_img = cur_img.crop((259, 76, cur_img.width, 667))  # cuts out everything except map
        return date        

def walk_folder(folder): 
    for filename in os.listdir(folder):
        cur_img = Image.open(folder+filename)
        infilename = os.path.join(folder,filename)
        os.rename(infilename, infilename.split(".")[0]+".jpg")  # so that each pixel will only have a length of 3
        new_filename = "".join([x[0] for x in sorted((get_date(cur_img)), key=lambda d: d[1])])  # sorts date as: HH MM Month Day Year; currently just mashes sorted list
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
