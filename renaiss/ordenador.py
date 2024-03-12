'''
Links
Pasar a minusculas:
https://www.datacamp.com/tutorial/python-regular-expression-tutorial

gensim para sacar las stopwords:
https://pypi.org/project/gensim/
https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
'''

import re
from gensim.parsing.preprocessing import remove_stopwords
import numpy as np
import pandas as pd

def frecuency_appearance(text_file):
    '''
    This funcion will read a text
    - First of all lowercase every word
    - Clean the stopwords(i do it with a module name gensim)
    - Then will counter all the words
    - I have to show the words in decreassing order
    '''

    with open ('text.md', 'r') as f:
        text=f.read()

    text=re.sub(r"[^\w\s]", "", text.lower())

    new_text=remove_stopwords(text)

    split_text=new_text.split()

    df=pd.value_counts(np.array(split_text))

    print('Words:', df.index)

