# Fame To Blame

**CODING WEEKS 2021-2022**

Fame to Blame is a python program to collect tweets about celebrities chosen by the user with the twitter API and to analyze them by detecting whether they are offensive or not. The user is then able to see a ranking of the celebrities he submitted ordered by the frequency of tweets insulting them.


## Installation 

### Installing the program

Simply pull the git repository on your computer.

### Requirements 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the necessary python modules, listed below.

```bash
pip install name_of_the_module
```

The necessary modules are: 
* carbonai  
* dash  
* dash_bootstrap_components  
* matplotlib.pyplot  
* pandas  
* PIL  
* pytest  
* python-Levenshtein  
* scipy  
* textblob  
* tkinter  
* tweepy  
* wordcloud  

Also to install :  
* [Visual Studio Installer](https://docs.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2022) and by using it install the workload to handle C++ in order to use the wordcloud package  
* [Intel Power Gadget](https://www.intel.com/content/www/us/en/developer/articles/tool/power-gadget.html?wapkw=intel%20power%20gadget) to use carbonai

Before using the program, make sure to have a file named credentials.py, containing your access keys as strings, named exactly like this : CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN and ACCESS_SECRET and run the intel power gadget to gather the data for carbonAI.

Finally, have a stable internet connection in order to collect the tweets and show the results.

## Usage

Once you completed the prerequisite, you can open the file \_\_main__.py from fame-to-blame and execute it.  
A window will open, where you must select your language, enter the absolute path to the folder containing the file credentials.py (be careful to respect the format : no backslashes, only slashes). You can then enter the twitter usernames (you must enter a valid twitter username : someone's twitter @) of the celebrities whom you want to run the program with, as well as optional keywords to search about this celebrity, like his family name (once again, respect the format : separate the keywords with ", ").  
Finally, a window will open in your web browser in which you can see the results.

Enjoy! =)

If you want to use carbonAI, uncomment the commented block of powermeter in \_\_main__ and comment the line 57 using appli().

## Contact

If you have any question, feel free to contact one of the creators of the project named below.  
Tom Bray : tom.bray@student-cs.fr  
Mathilde Jacquotot : mathilde.jacquotot@student-cs.fr  
Ludovic Mulat : ludovic.mulat@student-cs.fr  
Siméon Boyer : simeon.boyer@student-cs.fr  
Matthieu Neau : matthieu.neau@student-cs.fr  
Gaspard Debiais : gaspard.debiais@student-cs.fr   

## Roadmap

More languages could be implemented and different alphabets.  
A self-learning AI could be developped in order to detect better whether a tweet is insulting or not, according to the context.

## Contributing
This program is open source, you can do whatever you want with it.

If you wish to contribute, you are free to manipulate the code. The names of folders and files are self-explanatory, describe what they do.

## Versions
1.0 First and last version

Made with :  
* Python  
* git  
* gitlab  
* twitter api  
* handbook cs_codingweek_twitteranalysis_2021

## Link to the gitlab

https://gitlab-ovh-02.cloud.centralesupelec.fr/tom.bray/fame-to-blame/