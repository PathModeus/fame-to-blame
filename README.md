# Fame To Blame

**CODING WEEKS 2021-2022**

Fame to Blame is a python program to collect tweets about celebrities chosen by the user with the twitter API and to analyze them by detecting whether they are offensive or not. The user is then able to see a ranking of the celebrities he submitted ordered by the frequency of tweets insulting them. This is a project taking part in the second week of the CentraleSupélec Coding Weeks


## Setup 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary python modules, listed below.

```bash
pip install name_of_the_module
```

The necessary modules are:  
* csv  
* dash  
* json  
* matplotlib.pyplot  
* numpy  
* os  
* pandas  
* PIL  
* pytest  
* scipy  
* sys  
* textblob  
* time  
* tkinter  
* tweepy  
* wordcloud

Before using the program, make sure to have a file named credentials.py, containing your access keys as strings, named exactly like this : CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN and ACCESS_SECRET.

Finally, have a stable internet connection in order to collect the tweets and show the results.

## Using the program

Once you completed the prerequisite, you can open the file \_\_main.py__ from fame-to-blame and execute it.  
A window will open, where you must select your language, enter the absolute path to the folder containing the file credentials.py (be careful to respect the format : no backslashes, only slashes). You can then enter the twitter usernames of the celebrities whom you want to run the program with, as well as keywords to search about this celebrity.  
Finally, a window will open in your web browser in which you can see the results.

Enjoy! =)

## Contact

If you have any question, feel free to contact one of the creators of the project named below.  
Tom Bray :          tom.bray@student-cs.fr  
Mathilde Jacquotot :  mathilde.jacquotot@student-cs.fr  
Ludovic Mulat :     ludovic.mulat@student-cs.fr  
Siméon Boyer        simeon.boyer@student-cs.fr  
Matthieu Neau       matthieu.neau@student-cs.fr  
Gaspard Debiais     gaspard.debiais@student-cs.fr   

## Contributing
This program is open source, you can do whatever you want with it.
If you wish to contribute, you are free to manipulate the code. The names of folders and files are self-explanatory, describe what they do.


## Versions
1.0 First and last version

GitLab : https://gitlab-ovh-02.cloud.centralesupelec.fr/tom.bray/fame-to-blame/

Made with :  
* Python  
* git  
* gitlab  
* handbook cs_codingweek_twitteranalysis_2021 