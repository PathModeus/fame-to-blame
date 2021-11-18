"""
This module is used to manage the user interface and to query the users and the keywords associated
"""

import tkinter as tk
from tkinter import ttk
import os

PATH='' #The path to the directory of credentials.py
NUM_OF_CEL=1 #Number of celebrities chose by the user
PEOPLES=[] #List of People to study and the keywords to use with
LANGUAGE='en'



def start():
    """
    This is the first function to be executed.
    It allows the user to chose the language of the UI.
    """


    def click_enter():
        """
        This function manages the event when the user clicks on Enter.
        """
        
        window.destroy()
        path_window()

    def change_language(*args):
        global LANGUAGE
        LANGUAGE=my_text_field_var.get()
    

    window = tk.Tk()
    window.title("Fame to Blame")
    my_label = ttk.Label(window, text=TEXTS[LANGUAGE]['language_label'])
    my_text_field_var = tk.StringVar()
    my_text_field_var.set(LANGUAGES[0])
    my_button = ttk.Button(window, text=TEXTS[LANGUAGE]['enter'], state="enabled", command=click_enter)
    opt=tk.OptionMenu(window, my_text_field_var, *LANGUAGES, command=change_language)
    my_label.pack()
    opt.pack()
    my_button.pack()
    window.mainloop()

def path_window():
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
    my_label = ttk.Label(window, text=TEXTS[LANGUAGE]['path_msg'])
    my_text_field_var = tk.StringVar("")
    my_text_field = ttk.Entry(window, textvariable=my_text_field_var)
    my_message = ttk.Label(window, text=TEXTS[LANGUAGE]['path_advise'])
    my_button = ttk.Button(window, text=TEXTS[LANGUAGE]['enter'], state="disabled", command=click_enter)
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
    my_label = ttk.Label(window, text=TEXTS[LANGUAGE]['celebrity_label'])
    my_text_field_var = tk.StringVar("")
    my_text_field = ttk.Entry(window, textvariable=my_text_field_var)
    my_button = ttk.Button(window, text=TEXTS[LANGUAGE]['enter'], state="disabled", command=click_enter)
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
    my_label_1 = ttk.Label(window, text=TEXTS[LANGUAGE]['@label']+number)
    my_label_2 = ttk.Label(window, text=TEXTS[LANGUAGE]['celebrity_advice'])
    my_label_3 = ttk.Label(window, text=TEXTS[LANGUAGE]['keywords_format'])
    my_text_field_var = tk.StringVar("")
    my_text_field = ttk.Entry(window, textvariable=my_text_field_var)
    my_button = ttk.Button(window, text=TEXTS[LANGUAGE]["enter"], state="disabled", command=click_enter)
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


TEXTS={
<<<<<<< HEAD
    "En": {
        "language_label":"Please select your language.",
=======
    "en": {
        "language_label":"Please select your language.", 
>>>>>>> bd039e3fbfd065d8b7a6c350e2cd07a1e6e3f334
        "path_advise":"Be sure the path doesn't have '\\' but '/' instead",
        "enter":"Enter", "path_msg": "Please enter the path to the directory of credentials.py",
        "keywords_format": "Please respect the format : keyword 1, keyword 2, ...",
        "celebrity_label": "Please enter the number of people you want to study.",
        "@label": "Please enter the twitter @ of the people number ",
        "celebrity_advice": "Enter some keywords associated to this people"},

    "fr": {
        "language_label":"Merci de sélectionner votre langue.",
        "path_advise": "Assurez-vous que le chemin d'accès ne contient pas de '\\' mais des '/' à la place.",
        "enter":"Entrer","path_msg":"Merci d'entrer le chemin d'accès vers le répertoire de credentials.py",
        "keywords_format": "N'entrez des mots-clefs que sous le format : mot clef 1, mot clef 2, ...",
        "@label": "Merci d'entrer le @ Twitter de la personne numéro ",
        "celebrity_label": "Merci d'entrer le nombre de personnes que vous souhaitez étudier",
        "celebrity_advice": "Entrez quelques mots clefs associés à cette personne."}
        }

LANGUAGES=['en','fr']
