import os
import string

def rename_files():
    file_list = os.listdir(r"C:\Users\sanja\OneDrive\Desktop\Udacity Python\Intro to Python\prank")
    #print(file_list)
    path= os.getcwd()
    print (path)
    os.chdir(r"C:\Users\sanja\OneDrive\Desktop\Udacity Python\Intro to Python\prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
rename_files()   
        
        


    
