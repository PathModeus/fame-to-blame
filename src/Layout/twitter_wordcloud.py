import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_gradient_magnitude
from wordcloud import WordCloud, ImageColorGenerator
from textblob import TextBlob
from textblob import Word
import json

from insult_detection.csv_to_list import convert_database


PATH='data/swear_words_database.csv'
swear_words_data=convert_database(PATH)

'''Fonction qui filtre les mots qui n'ont pas trop d'occurences'''
'''Valeur du filtre à ajuster'''


def antibrouillard(text):
    d = {}
    mots = text.split(' ')
    u = []
    for x in mots:
        var_convert = TextBlob(x)
        y = var_convert
        y = Word(y).lemmatize()
        y = str(y)
        if y in swear_words_data : 
            u.append(y)
    v = "".join(u)
    return v


# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# load wikipedia text on rainbow
text = open(os.path.join(d, 'c:/Users/Ludov/Documents/CW/MIST/Layout/Text.txt'),
            encoding="utf-8").read()

# load image. This has been modified in gimp to be brighter and have more saturation.
bird_color = np.array(Image.open(os.path.join(d, "bluetwitter.jpg")))


# create mask  white is "masked out"
bird_mask = bird_color.copy()
bird_mask[bird_mask.sum(axis=2) > 200] = 255

# create wordcloud. A bit sluggish, you can subsample more strongly for quicker rendering
# relative_scaling=0 means the frequencies in the data are reflected less
# acurately but it makes a better picture
wc = WordCloud(max_words=2000, mask=bird_mask,
               max_font_size=40, random_state=42, relative_scaling=0)

# generate word cloud
wc.generate(antibrouillard(text))
plt.imshow(wc)

# create coloring from image


plt.show()
