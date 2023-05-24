# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 13:46:38 2022

@author: user
"""
# 1. Raw data processing (Data cleaning)
# 2. Tokenization and StopWords
# 3. Feature Extraction techniques
# 4. Topic Modelling and LDA
# 5.Word2Vec (word embedding)
# 6. Continuous Bag-of-words(CBOW)
# 7. Global Vectors for Word Representation (GloVe)
# 8. text Generation,
# 9. Transfer Learning
#*****************************************************************************
            #how to check data using NLP
#*****************************************************************************

# conda install nltk on cmd prompt 
import nltk
# nltk.download() #download all library
import os
import nltk.corpus  # corpus means collections of words

#By runnig this line wewill get numbe rof zip file
print(os.listdir(nltk.data.find("corpora")))

nltk.corpus.webtext.fileids()

print(nltk.corpus.webtext.words('firefox.txt'))

data = nltk.corpus.webtext.words('firefox.txt')
print(data)

print(len(data))

print(data[0])
print(data[10])
print(data[100])
print(data[1000])
print(data[0:10])

list1 =[]
for x in data[0:100]:
    list1.append(x)
    print(x,end =" ")

print(list1)

#This is the way to convert array or list into string data
v =" ".join(list1)
print(v)

#This is the way to convert string data into array or list
w = v.split()
print(w)
#*****************************************************************************
        #word_tokenize - convert string into tokens(list/array)  
#*****************************************************************************

sample_data = "This is dummy NLP data. I'm Taral Mehta from livetechindia NLP. Here we will learn NLP from livetechindia"
print(sample_data)

#convert string into tokens(list/array)
from nltk.tokenize import word_tokenize as wt
token =wt(sample_data)
print(token)
print(len(token))

#how to find frequency of any data
from nltk.probability import FreqDist #it will give number of repeating word
b1 =FreqDist(sample_data) #it will divide text into letter and then count
b1

b2 =FreqDist(token)#here it will count number of word who is repeating
b2
print(b2)
print(type(b2))

print(b2["."])
b2["from"]
b2["this"]
b2["This"]

          
cmn =b2.most_common(5)
cmn
#*****************************************************************************
        #Blankline_Tokenize - How many number of paragrah you have   
#*****************************************************************************
sample_data ="""About 1,07,00,000 results (0.63 seconds) 

Naive Bayes Classifier in Machine Learning - Javatpointhttps://www.javatpoint.com › machine-learning-naive-b...
Naïve Bayes algorithm is a supervised learning algorithm, which is based on Bayes theorem and used for solving classification problems. · Naïve: It is called ...


      Naive Bayes Classifiers - GeeksforGeekshttps://www.geeksforgeeks.org › naive-bayes-classifiers
24-Aug-2022 — Naive Bayes classifiers are a collection of classification algorithms based on Bayes' Theorem. It is not a single algorithm but a family of ...

Naïve Bayes Algorithm: Everything You Need to Knowhttps://www.kdnuggets.com › 2020/06 › naive-bayes-al...
08-Apr-2022 — Naïve Bayes is a probabilistic machine learning algorithm based on the Bayes Theorem, used in a wide variety of classification tasks."""

from nltk.tokenize import blankline_tokenize
para =blankline_tokenize(sample_data)
print(para)

#*****************************************************************************
     #bigrams -if you are making token of two words then it will be bigrams 
     #Trigram -if you are making token of three words then it will be bigrams 
     #ngrams - if you are making token of words then it will be bigrams 
#*****************************************************************************

sample_data = "This is dummy NLP data. I'm Taral Mehta from livetechindia NLP. Here we will learn NLP from livetechindia"
print(sample_data)

from nltk.util import bigrams,trigrams,ngrams
bi =list(bigrams(sample_data))
bi

ti =list(trigrams(sample_data))
ti

ni =list(ngrams(sample_data,6))
ni

#*****************************************************************************
               #Stemmer -  removes prefixes and suffixes to identify unique words
#*****************************************************************************

from nltk.stem import PorterStemmer as ps
list_words = ['take','took','taken',"taking"]
list_words = ['go','gone',"going"]
list_words = ['ring','rung',"rang","ringing"]
list_words = ["eat","ate","eaten","eating"]

obj = ps()
for i in range(len(list_words)):
    print(obj.stem(list_words[i]))
    
    
from nltk.stem import LancasterStemmer as ps
list_words = ['take','took','taken',"taking"]
list_words = ['go','gone',"going"]
list_words = ['ring','rung',"rang","ringing"]
list_words = ["eat","ate","eaten","eating"]

obj = ps()
for i in range(len(list_words)):
    print(obj.stem(list_words[i]))


#*****************************************************************************
               #Lemantization - Retain meaning
#*****************************************************************************
import nltk
from nltk.stem import WordNetLemmatizer as wt
list_words = ['take','took','taken',"taking"]
list_words = ['go','gone',"going"]
list_words = ['ring','rung',"rang","ringing"]
list_words = ["eat","ate","eaten","eating"]

obj= wt()
for i in range(len(list_words)):
    print(obj.lemmatize(list_words[i]))


#*****************************************************************************
               #Lemantization - 
#*****************************************************************************

from nltk.corpus import stopwords
print(stopwords.words("English"))
print(stopwords.words("english"))

a =stopwords.words("english")
print(a)



#*****************************************************************************
               #Punchuation - 
#*****************************************************************************

import re #regular extraction   #regex

a ="In, Edgar Allen Poe’s () Edgar Allen Poe describes a m.a.n with a guilty conscience."
a =re.sub(r"[^\w]"," ",a) 
a =re.sub(r"[^\w]$"," ",a) 
a =re.sub(r"[^\w]"," ",a) 
a =re.sub(r"[^\w]","#",a) 
       
a
#r"[^\w]  ---> will match a string consisting of a single character, 
# where that character is alphanumeric (letters, numbers) an underscore (_) or an asterisk (*).

# The "\w" means "any word character" which usually means alphanumeric (letters, numbers, regardless of case) plus 
# underscore (_)

# The "^" "anchors" to the beginning of a string, and the "$" "anchors" To the end of a string, 
# which means that, in this case, the match must start at the beginning of a string and end at the end of the string.

# The [] means a character class, which means "match any character contained in the character class".

print(a)


import string 

pun =  string.punctuation
print(pun)


import re

# Example text
text = "Hello, world! How are you?"
a ="In, Edgar Allen Poe’s () Edgar Allen Poe describes a m.a.n with a guilty conscience."

# Remove punctuation using regular expressions
clean_text = re.sub(r'[^\w\s]', '', text)
clean_text = re.sub(r'[^\w\s]', '', a)

# Print the cleaned text
print(clean_text)
#*****************************************************************************
               #Parts of speech - pos_tag passes diffrent types of tag.
               #which word is verb ,adjective..etc
#*****************************************************************************


a = "this is a good movie. we are using parts of speech here."
from nltk.tokenize import word_tokenize as wt #its like split function
list_word = wt(a)
print(list_word)
tag =nltk.pos_tag(list_word)
print(tag)


sample_data = "This is dummy NLP data. I'm Taral Mehta from livetechindia NLP. Here we will learn NLP from livetechindia"
print(sample_data)
list_word = wt(sample_data)
print(list_word)
tag =nltk.pos_tag(list_word)
print(tag)

from nltk import ne_chunk as nc  #picking individual entity and grouping into bigger pieces.that bigger pieces known as chunk

sample_data = "This is dummy NLP data. I'm Taral Mehta from livetechindia NLP. Here we will learn NLP from livetechindia"
print(sample_data)
list_word = wt(sample_data)
print(list_word)

tag =nltk.pos_tag(list_word)
print(tag)
print(len(tag))

chunk = nc(tag)
print(chunk)
print(len(chunk))
#*****************************************************************************
               #Parts of speech - pos_tag passes diffrent types of tag.
               #which word is verb ,adjective..etc
#*****************************************************************************
from nltk import ne_chunk as nc  #picking individual entity and grouping into bigger pieces.that bigger pieces known as chunk

sample_data = "This is dummy NLP data. I'm Taral Mehta from livetechindia NLP. Here we will learn NLP from livetechindia"
print(sample_data)
list_word = wt(sample_data)
print(list_word)

g=r"NP:{<DT>?<JJ>*<NN>}"

tag =nltk.pos_tag(list_word)
print(tag)
print(len(tag))

obj =nltk.RegexpParser(g)
print(obj)
v =obj.parse(tag)
print(v)
len(v)


#********************************************************
                #NLP PROJECT
#********************************************************


# conda install nltk on cmd prompt 
import nltk
# nltk.download() #download all library
import os
from sklearn.feature_extraction.text import CountVectorizer
print(os.listdir(nltk.data.find("corpora")))
from nltk.corpus import movie_reviews

print(movie_reviews.categories())
print(movie_reviews.fileids('pos'))
print(movie_reviews.fileids('neg'))

#*******************************************************
filename_pos  = nltk.corpus.movie_reviews.words("pos/cv999_13106.txt")
filename_pos
filename_pos[-1]
filename_pos[:11]

y =nltk.corpus.movie_reviews.fileids('pos')
y

listEmpty =[]
for x in y:
    rev_text =nltk.corpus.movie_reviews.words(x)
    # print(rev_text)
    rev_one =" ".join(rev_text)
    rev_one =rev_one.replace(" ,", ",")
    rev_one =rev_one.replace(" .", ".")
    rev_one =rev_one.replace("\'", "'")
    rev_one =rev_one.replace(" \'", "'")
    listEmpty.append(rev_one)

listEmpty
#*******************************************************
filename_neg  = nltk.corpus.movie_reviews.words("neg/cv999_14636.txt")
filename_neg

z =nltk.corpus.movie_reviews.fileids('neg')
z

for x in z:
    rev_text =nltk.corpus.movie_reviews.words(x)
    # print(rev_text)
    rev_one =" ".join(rev_text)
    rev_one =rev_one.replace(" ,", ",")
    rev_one =rev_one.replace(" .", ".")
    rev_one =rev_one.replace("\'", "'")
    rev_one =rev_one.replace(" \'", "'")
    listEmpty.append(rev_one)

listEmpty

# What is CountVectorizer In NLP?
# CountVectorizer means breaking down a sentence or 
# any text into words by performing preprocessing tasks 
# like converting all words to lowercase, 
# thus removing special characters  



#******************************************************************************


import pandas as pd 
text = ["This is the NLP TASKS ARTICLE written by ABhishek Jaiswal  !!!","IN this article I'll be explaining various DATA-CLEANING techniques",'So stay tuned for FURther More &&','Nah I dont think he goes to usf'," he lives around"]
text
len(text)

temp = []
for x in text:
    temp.append(x.lower())
temp 


import string
from nltk.corpus import stopwords
print(stopwords.words("English"))

pun =  string.punctuation
pun

filterd_data = []
removal_data = []
from nltk.tokenize import word_tokenize 

for x in nltk.word_tokenize(temp):
    if x not in pun:
        filterd_data.append(x)
    else:
        removal_data.append(x)
        
        
filterd_data
removal_data
# The apply() method allows you to apply a function along one of the axis of the DataFrame, 
# default 0, which is the index (row) axis.
df = pd.DataFrame({"text":text})   
df



