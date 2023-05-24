# -*- coding: utf-8 -*-
"""
Created on Wed May 17 13:05:08 2023

@author: Livewire
"""
import nltk
# nltk.download() #download all library
import os
import nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer

from nltk.corpus import stopwords
import re
import string
            
from nltk import ne_chunk

story = """ 
'The Kerala Story', the latest directorial venture of Sudipto Sen starring Adah Sharma, 
Yogita Bihani, Sonia Balani, and Siddhi Idnani, hit the theatres on 05th May 2023. 
The film is based on the forceful conversion of 32,000 women in Kerala to Islam out of which many of them were taken to ISIS-ruled-Syria. 
Despite altering the YouTube trailer’s description to the true stories of three young girls from different parts of Kerala, 
Director Sen continues to preserve it as an unquestionable 'truth' at the movie’s climax."""

print(story)
print(len(story))

print(story[0:100])
print(story[10:100])
