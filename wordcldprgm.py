from wordcloud import WordCloud ,STOPWORDS#pip install wordcloud 
import matplotlib.pyplot as plt 
import csv 
import pandas as pd
stopwords =  set(STOPWORDS)# at a time stopword or stopwordlist will be used

reader_ob=open(r"C:\Users\user\Documents\Taral\AI\NLP\movie_review.txt",'r')
  
reader_contents = list(reader_ob) 
  
text = "" 
  
for row in reader_contents :  
    for word in row : 
        text = text + "" + word 
  
wordcloud = WordCloud(width=800, height=480, max_words=30,stopwords={'two','t',
 'about',
 'above',
 'after',
 'again',
 'against',
 'all',
 'also',
 'am',
 'an',
 'and',
 'any',
 'are',
 "aren't",
 'as',
 'at',
 'be',
 'because',
 'been',
 'before',
 'being',
 'below',
 'between',
 'both',
 'but',
 'by',
 'can',
 "can't",
 'cannot',
 'com',
 'could',
 "couldn't",
 'did',
 "didn't",
 'do',
 'does',
 "doesn't",
 'doing',
 "don't",
 'down',
 'during',
 'each',
 'else',
 'ever',
 'few',
 'for',
 'from',
 'further',
 'get',
 'had',
 "hadn't",
 'has',
 "hasn't",
 'have',
 "haven't",
 'having',
 'he',
 "he'd",
 "he'll",
 "he's",
 'hence',
 'her',
 'here',
 "here's",
 'hers',
 'herself',
 'him',
 'himself',
 'his',
 'how',
 "how's",
 'however',
 'http',
 'i',
 "i'd",
 "i'll",
 "i'm",
 "i've",
 'if',
 'in',
 'into',
 'is',
 "isn't",
 'it',
 "it's",
 'its',
 'itself',
 'just',
 'k',
 "let's",
 'like',
 'me',
 'more',
 'most',
 "mustn't",
 'my',
 'myself',
 'no',
 'nor',
 'not',
 'of',
 'off',
 'on',
 'once',
 'only',
 'or',
 'other',
 'otherwise',
 'ought',
 'our',
 'ours',
 'ourselves',
 'out',
 'over',
 'own',
 'r',
 'same',
 'shall',
 "shan't",
 'she',
 "she'd",
 "she'll",
 "she's",
 'should',
 "shouldn't",
 'since',
 'so',
 'some',
 'such',
 'than',
 'that',
 "that's",
 'the',
 'their',
 'theirs',
 'them',
 'themselves',
 'then',
 'there',
 "there's",
 'therefore',
 'these',
 'they',
 "they'd",
 "they'll",
 "they're",
 "they've",
 'this',
 'those',
 'through',
 'to',
 'too',
 'under',
 'until',
 'up',
 'very',
 'was',
 "wasn't",
 'we',
 "we'd",
 "we'll",
 "we're",
 "we've",
 'were',
 "weren't",
 'what',
 "what's",
 'when',
 "when's",
 'where',
 "where's",
 'which',
 'while',
 'who',
 "who's",
 'whom',
 'why',
 "why's",
 'with',
 "won't",
 'would',
 "wouldn't",
 'www',
 'you',
 "you'd",
 "you'll",
 "you're",
 "you've",
 'your',
 'yours',
 'yourself',
 'yourselves','S',"Drishyam"}).generate(text)
  
# plot the WordCl oud image  
plt.figure() 
plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis("off") 
plt.margins(x=0, y=0) 
plt.show()   
    
# --------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"C:\Users\user\Downloads\archive\superstore.xls")
df    
    
# 1. (Visual Method) Create a histogram.
# If the histogram is roughly “bell-shaped”, 
# then the data is assumed to be normally distributed.

import math
import numpy as np
from scipy.stats import lognorm
import matplotlib.pyplot as plt
    
plt.hist(df.Profit, edgecolor='black', bins=10)
plt.hist(df.Sales, edgecolor='black', bins=10)
    
#******************************************************
# 2. (Visual Method) Create a Q-Q plot.
import math
import numpy as np
from scipy.stats import lognorm
import statsmodels.api as sm
import matplotlib.pyplot as plt

#create Q-Q plot with 45-degree line added to plot
fig = sm.qqplot(df.Sales, line='45')
fig = sm.qqplot(df.Profit, line='45')


#******************************************************
# 3. (Formal Statistical Test) Perform a Shapiro-Wilk Test.
# If the p-value of the test is greater than α = .05, 
# then the data is assumed to be normally distributed.

import math
import numpy as np
from scipy.stats import shapiro 
from scipy.stats import lognorm



#perform Shapiro-Wilk test for normality
shapiro(df.Profit)
shapiro(df.Sales)


#******************************************************

# 4. (Formal Statistical Test) Perform a Kolmogorov-Smirnov Test.
# If the p-value of the test is greater than α = .05, 
# then the data is assumed to be normally distributed.


import math
import numpy as np
from scipy.stats import kstest
from scipy.stats import lognorm
   

#perform Kolmogorov-Smirnov test for normality
kstest(df.Profit, 'norm')
kstest(df.Sales, 'norm')

#****************** Convert into normal distribution***************

#1. Log Transformation in Python  
import numpy as np
import matplotlib.pyplot as plt

#make this example reproducible

#create beta distributed random variable with 200 values
data=df.Sales
#create log-transformed data
data_log = np.log(df.Sales)
  
#define grid of plots
fig, axs = plt.subplots(nrows=1, ncols=2)    

#create histograms
axs[0].hist(data, edgecolor='black')
axs[1].hist(data_log, edgecolor='black')

#add title to each histogram
axs[0].set_title('Original Data')
axs[1].set_title('Log-Transformed Data')















