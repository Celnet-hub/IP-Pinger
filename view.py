"""A simple desktop application that takes user input and print on the screen.

Task:
    - Create an input field
    - Create a button to process the user input
    - Print user input to create.

Algorithm:
    - Create the input widget(Entry)
    - Create a button widget that processes the user input when the button is clicked.
    - Create a function that processes the button when it's clicked.
    -
"""

from tkinter import *
import main
from tkinter import filedialog
import glob
import os

# create the root widget
root = Tk()
root.geometry("400x400")

# get file to ping
def start_process():
    file_name = filedialog.askopenfilename()
    
    # run the main function to process the file
    main.run(file_name)

    # display the result
    display_result()
    

def display_result():
    # open the result file
    list_of_files = glob.glob('Result/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    result_file = open(latest_file , "r")
    result_text = result_file.read()
    result_file.close()
    result_Label = Label(
    root, 
    text=result_text,
    )
    # result_Label.grid(row=7, column=7, padx=10)
    result_Label.place(relx = 0.5, rely = 0.5,anchor = 'center')
    print(result_Label)


file_label = Label(
    root, 
    text='Upload a CSV file '
    )
file_label.grid(row=0, column=0, padx=10)

get_fileBtn = Button(
    root, 
    text ='Choose File',
    command = lambda: start_process()
    ) 
get_fileBtn.grid(row=0, column=1)

# result_label = Label(root, text='Result')
# result_label.grid(row=1, column=0, padx=10)

# create a loop that constantly run to keep the window open.
root.mainloop()
