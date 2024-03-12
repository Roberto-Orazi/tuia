texto='the car Chair in the room, and the. chair chair room'

import re
from gensim.parsing.preprocessing import remove_stopwords
import numpy as np
import pandas as pd

text=re.sub(r"[^\w\s]", "", texto.lower())

new_text=remove_stopwords(text)

for word in new_text:
    print(word)

split_text=new_text.split()

for word in split_text:
    print(word)

df=pd.value_counts(np.array(split_text))

print('Words:', df.index)