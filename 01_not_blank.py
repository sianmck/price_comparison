#import statements
from tkinter import*

#functions
def not_blank(question):
    error = "This can not be blank"

    valid = False
    while not valid:
        response =input(question)

        if response != "":
            return response

        else:
            print(error)

#MAIN ROUTINE
#inputs
name= not_blank("Name: ")



