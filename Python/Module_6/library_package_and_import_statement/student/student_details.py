
import os # it provide functionality to interact with operating system
import sys # provide access to system specific parameters and function such as path
from os.path import dirname, join, abspath

print("the path script is :",__file__) #c:\Users\Naman\Desktop\Data Science\Python\Module_6\library_package_and_import_statement\student\student_details.py
# __file__ >> gives you path to current script 

print("the dir name : ", dirname(__file__)) # c:\Users\Naman\Desktop\Data Science\Python\Module_6\library_package_and_import_statement\student

print("the dir of script :",join(dirname(__file__), ".."))  #c:\Users\Naman\Desktop\Data Science\Python\Module_6\library_package_and_import_statement\student\..
# join : combine two or more path components, inserting '/' as needed 
#join(dirname(__file__), "..") >> move one directory up form the cuurent script directory 

print("absolute path ",abspath(dirname(__file__)))

parent_dir_path = abspath(join(dirname(__file__), ".."))

sys.path.insert(0, parent_dir_path)
# at index 0 , add this directory to the beignning of the module search/system path
# it allow to search modules and packages 




# now it's safe to import teacher
from teacher import teacher_details


def student():
    print("this is student details \n")

student()
teacher_details.teacher()
