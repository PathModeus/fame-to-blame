"""
This is the main module of our app, execute in your shell to run it!
"""
import tkinter as tk
from tkinter import ttk
import os

PATH='' #The path to the directory of credentials.py
NUM_OF_CEL=1 #Number of celebrities chose by the user

def start():
    """
    This is the first function to be executed.
    It allows the user to enter a Path to credentials.py and submit it.
    """
    
    def check_path(*args):
        """
        This function verifies if the path to credentials exists.
        If it does, it enables the button.
        """
        pathstr=my_text_field_var.get().strip()
        if os.path.exists(pathstr + '/credentials.py') and pathstr != "" and ('\\' not in pathstr) :
            my_button.configure(state="!disabled")
        else :
            my_button.configure(state="disabled")
    def click_enter():
        """
        This function manages the event when the user clicks on Enter.
        """
        PATH=my_text_field_var.get().strip()
        window.destroy()
        input_celebrity_number()



    
    window = tk.Tk()
    window.title("Fame to Blame")
    my_label = ttk.Label(window, text="Please enter the path to the directory of credentials.py")
    my_text_field_var = tk.StringVar("")
    my_text_field = ttk.Entry(window, textvariable=my_text_field_var)
    my_message = ttk.Label(window, text="Please be sure that the path doesn't contain '\\' but '/' instead")
    my_button = ttk.Button(window, text="Enter", state="disabled", command=click_enter)
    my_label.pack()
    my_text_field.pack()
    my_button.pack()
    my_message.pack()
    my_text_field_var.trace("w", check_path)
    window.mainloop()
    

def input_celebrity_number():
    """
    Manages the number of celebrities to follow by the user.
    """
    def check_number(*args):
        """
        Checks if the field contains an int and enables the button if yes.
        """
        num=my_text_field_var.get().strip()
        if num.isdigit() and num!='0':
            my_button.configure(state="!disabled")
        else :
            my_button.configure(state="disabled")



    def click_enter():
        """
        Manages the event : the user clicked on enter.
        """
        NUM_OF_CEL=int(my_text_field_var.get().strip())
        window.destroy()
        for i in range(NUM_OF_CEL):
            query_keyword(i)

    window = tk.Tk()
    window.title("Fame to Blame")
    my_label = ttk.Label(window, text="Please enter the number of people you want to study.")
    my_text_field_var = tk.StringVar("")
    my_text_field = ttk.Entry(window, textvariable=my_text_field_var)
    my_button = ttk.Button(window, text="Enter", state="disabled", command=click_enter)
    my_label.pack()
    my_text_field.pack()
    my_button.pack()
    my_text_field_var.trace("w", check_number)
    window.mainloop()

def query_keyword(i):
    """
    Requests the @ of the user to study and the keywords associated.
    """

start()
