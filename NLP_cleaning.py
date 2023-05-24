# -*- coding: utf-8 -*-
"""
Created on Tue May 16 19:18:28 2023

@author: Livewire
"""
-----------------------------------
a="taral.mehta@somaiya.edu"

match =  re.search("\.",a)
match

match1 =  re.search("[@]",a)
match1

match2 =  re.search("[#]",a)
match2

match3 =  re.search("[ta]",a)
match3
-------------------------------
match4 =  re.findall("[ta]",a)
match4

match5 =  re.findall("[T]",a)
match5

match6 =  re.findall("[edu]",a)
match6
-------------------------------
#replace 't' and 'a' with  blank string
match7 =  re.sub("[ta]","",a) 
match7

#replace '@' with  '#' 
match8 =  re.sub("[@]","#",a)
match8

#replace everything except edu
match9 =  re.sub("[^edu]"," ",a)
match9

#replace edu with space
match10 =  re.sub("[edu]"," ",a)
match10

match11 =  re.sub("[^a-zA-Z0-9]"," ",a)
match11

a1="     taral.mehta@somaiya.edu "

#remove special character including . @ 
match11 =  re.sub("[^\w]"," ",a1)
match11

#remove spaces
match12 =  re.sub("[\s]","",a1)
match12
------------------------------------

import pandas as pd
import re

# Example DataFrame
data = {
    'Text': ['   Hello, 123', 'World!  ', '  12345', 'Some text with special characters: @#$%']
}
df = pd.DataFrame(data)
df


df["clean_text"] =  df.Text.str.lower()
df["clean_text"]
df["clean_text_1"] = df.clean_text.str.strip()
df["clean_text_1"] 


text = []
for x in df.clean_text_1:
    a1  = re.sub("[^a-zA-Z0-9]"," ",x)
    a1 = a1.strip()
    text.append(a1)
    
text

df["clean_text_2"] = text
df

-------------------------------------------------
# Function to clean text using regular expressions
def clean_text(text):
    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Convert text to lowercase
    text = text.lower()
    # Remove leading and trailing whitespaces
    text = text.strip()
    return text

# Apply cleaning function to the 'Text' column
df['Cleaned Text'] = df['Text'].apply(clean_text)

# Display the cleaned DataFrame
print(df)
# -----------------   Search Text  --------------
import re

# Search for a pattern in a string
pattern = 'apple'
text = 'I have an apple and an orange'
result = re.search("I", text)
print(result.group())  # Output: 'apple'
# ---------------  Substitute Text  -------------
import re

# Replace a pattern in a string
pattern = r'an apple'
text = 'I have an apple and an orange'
new_text = re.sub(pattern, 'banana', text)
print(new_text)  # Output: 'I have a banana and an orange'

# -------------- Splitting a String -------------
import re

# Split a string based on a pattern
pattern = r'\s'  # Split on whitespace
text = 'Hello World! How are you?'
result = re.split(pattern, text)
print(result)  # Output: ['Hello', 'World!', 'How', 'are', 'you?']

# ------------- Extract Specific Group ------------
import re

# Extract specific groups from a pattern
pattern = r'(\d{2})-(\d{2})-(\d{4})'  # Matches DD-MM-YYYY date format
text = 'Date of birth: 15-05-1990'
result = re.search(pattern, text)
print(result.group(0))  # Output: '15-05-1990'
print(result.group(1))  # Output: '15'
print(result.group(2))  # Output: '05'
print(result.group(3))  # Output: '1990
# ------------- case insensitive ------------

import re

# Perform a case-insensitive search
pattern = r'apple'
text = 'I have an Apple and an orange'
result = re.search(pattern, text, re.IGNORECASE)
print(result.group())  # Output: 'Apple'
-----------------------------------------------

import re #regular extraction   #regex

a ="In, Edgar Allen Poe’s () Edgar Allen Poe describes a m.a.n with a guilty conscience."
a =re.sub(r"[^\w]\s"," ",a) 
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
