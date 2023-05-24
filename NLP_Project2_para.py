# -*- coding: utf-8 -*-
"""
Created on Wed May 24 12:32:50 2023

@author: Livewire
"""

# =============================================================================
# Lecture Outline
data cleaning -- good GOOD Good    "   good "
reading text
removing numbers, punctuations, case senstativity, whitespace,..
## nltk
get frequency
use of nltk
tokenization
stemmer
lamitization
stopwords

## wordCloud
wordcloud

##beautiful soup, request
web scrapping -- plain
web scrapping -- tagbased
# =============================================================================

text = '''         Human rights              are moral principles or norms[1] 
for certain standards of ????????  human behaviour and are regularly protected 
in municipal and international law.[2] @ They are commonly understood 
as inalienable,[3]                            fundamental rights 
"to which a person is inherently entitled simply because she or 
he is a human being"[4] and which are\n "inherent in all human beings",
[5] regardless of their age, ethnic origin, location, language, religion, 
ethnicity, or any other status.[3] They are ##### applicable everywhere and 
at every time in the sense of being universal,[1] and they are egalitarian 
in the sense of being the same for everyone.[3] They are regarded as 
requiring empathy and the rule of law[6] \nand imposing an obligation on persons to 
respect the human rights of         others,[1][3] and it is generally considered that they 
should not be taken away except as a result of due process based on specific 
circumstances.[3]          " '''



text =""" JioMart has reportedly laid off over 1,000 employees as part of its efforts to streamline operations 
after its acquisition of Metro Cash and Carry. In the coming weeks, 
the online wholesale format of Reliance Industries plans to implement a larger cost-cutting initiative, 
which includes reducing its wholesale division's workforce by two-thirds.
 These measures aim to improve margins and reduce losses after JioMart initiated a price war in the grocery B2B space.
 
 JioMart has asked over 1,000 employees, including 500 executives from its corporate office,
 to resign, sources familiar with the matter revealed to The Economic Times.
 Additionally, hundreds of employees have been placed on a performance improvement plan,
 and the remaining sales staff have been shifted to a variable pay structure, reducing their fixed salaries.
 LiveMint could not independently verify the claim. 
 """
text
text=text.lower()
text
text=text.strip()
text

data=text.split()
data
data.count('jiomart')
data.count('human')

# =============================================================================
# remove decimal
# =============================================================================
num =[0,1,2,3,4,5,6,7,8,9]
for a in text:
    if a not in str(num):
        print(a,end="")
# regular expression
import re
text = re.sub('\d+'," ",text)
text
text.replace("    ","")
text.replace("?", "")
['?',"   ",","]
# =============================================================================
# punctuations
# =============================================================================
import string
a=text.maketrans(" "," ",string.punctuation)
text=text.translate(a)
text
data=text.split()
for i in range(len(data)):
    print(data[i],data.count(data[i]))

# =============================================================================
# tokenization -- spliting the word, 
# =============================================================================
import nltk

from nltk.tokenize import word_tokenize
wt=word_tokenize(text)

from nltk.tokenize import blankline_tokenize
b=blankline_tokenize(text)
b

from nltk.probability import FreqDist
fd=FreqDist(wt)
fd
# =============================================================================
# bigrams, tribrams
# =============================================================================
from nltk.util import bigrams
bn = list(nltk.bigrams(wt))
bn

list(nltk.trigrams(wt))
list(nltk.ngrams(wt,5))

# =============================================================================
# stopwords
# =============================================================================
from nltk.corpus import stopwords
stwd=stopwords.words('english')

filtered_data=[]
for word in wt:
    if word not in stwd:
        filtered_data.append(word)
    
fd_filtered=FreqDist(filtered_data)

# =============================================================================
# steming(doesnt maintain proper word), 
# lemmitaztion(maintain proper word) --- root word
# =============================================================================
from nltk.stem import PorterStemmer
ps = PorterStemmer()
ps.stem('calculating')

from nltk.stem import wordnet,WordNetLemmatizer
wlm = WordNetLemmatizer()
wlm.lemmatize('giving')

# =============================================================================
# Word Cloud
# =============================================================================
from matplotlib import pyplot as plt
from wordcloud import WordCloud
# pip install wordcloud

cloud = WordCloud(background_color="white")
c = cloud.generate(text)
plt.imshow(c)
plt.axis("off")
