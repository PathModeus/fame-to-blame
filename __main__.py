"""
This is the main module of our app, execute in your shell to run it! 
"""
import tkinter as tk
from tkinter import ttk
import os


def start():
    """
    This is the first function to be executed, it allows the user to enter a Path to credentials.py and submit it.
    """
    
    def check_path(*args):
        """
        This function verifies if the path to credentials exists. If not, it activates the error message.

        Parameters
        -----------
        path : VarStr

        """
        pathstr=my_text_field_var.get().strip()
        if os.path.exists(pathstr + '/credentials.py') and pathstr != "" and ('\\' not in pathstr) :
            my_button.configure(state="!disabled")
        else :
            my_button.configure(state="disabled")

    
    window = tk.Tk()
    window.title("Fame to Blame")
    my_label = ttk.Label(window, text="Please enter the path to the directory of credentials.py")
    my_text_field_var = tk.StringVar("")
    my_text_field = ttk.Entry(window, textvariable=my_text_field_var)
    my_message = ttk.Label(window, text="Please be sure that the path doesn't contain '\\' but '/' instead")
    my_button = ttk.Button(window, text="Enter", state="disabled")
    my_label.pack()
    my_text_field.pack()
    my_button.pack()
    my_message.pack()
    my_text_field_var.trace("w", check_path)
    window.mainloop()
    



start()
