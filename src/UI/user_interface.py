"""
This module is used to manage the user interface and to query the users and the keywords associated
"""

import tkinter as tk
from tkinter import ttk
import os

NUM_OF_CEL=1 #Number of celebrities chose by the user
PATH='' #The path to the directory of credentials.py
PEOPLES=[] #List of People to study and the keywords to use with

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
        global PATH
        PATH=my_text_field_var.get().strip()
        window.destroy()
        input_celebrity_number()


    window = tk.Tk()
    window.title("Fame to Blame")
    my_label = ttk.Label(window, text="Please enter the path to the directory of credentials.py")
    my_text_field_var = tk.StringVar("")
    my_text_field = ttk.Entry(window, textvariable=my_text_field_var)
    my_message = ttk.Label(window, text="Please be sure the path doesn't have '\\' but '/' instead")
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
        global NUM_OF_CEL
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

    def check_empty(*args):
        """
        Checks if the @ field is empty.
        """
        field=my_text_field_var.get().strip()
        if field=='':
            my_button.configure(state="disabled")
        else :
            my_button.configure(state="!disabled")

    def click_enter():
        global PEOPLES
        PEOPLES.append('')
        PEOPLES[i]+=my_text_field_var.get().strip()+', '
        PEOPLES[i]+=my_text_field_var_2.get().strip()
        window.destroy()

    number=str(i+1)
    window = tk.Tk()
    window.title("Fame to Blame")
    my_label_1 = ttk.Label(window, text="Please enter the twitter @ of the people number "+number)
    my_label_2 = ttk.Label(window, text="Enter some keywords associated to this people")
    my_label_3 = ttk.Label(window, text="Please respect the format : keyword 1, keyword 2, ...")
    my_text_field_var = tk.StringVar("")
    my_text_field = ttk.Entry(window, textvariable=my_text_field_var)
    my_button = ttk.Button(window, text="Enter", state="disabled", command=click_enter)
    my_text_field_var_2 = tk.StringVar("")
    my_text_field_2 = ttk.Entry(window, textvariable=my_text_field_var_2)
    my_label_1.pack()
    my_text_field.pack()
    my_label_2.pack()
    my_text_field_2.pack()
    my_label_3.pack()
    my_button.pack()
    my_text_field_var.trace("w", check_empty)
    window.mainloop()
