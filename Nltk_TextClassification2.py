#%%
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#%%
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

"""documents = []
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append((list(movie_reviews.words(fileid)), category))"""

random.shuffle(documents)

print(documents[1])
#%%
stop_words=set(stopwords.words("English"))
x1 = {',','.','-',"'",'"',')','(','?'}
stop_words2=stop_words|x1
print(stop_words2)
#%%
all_words = []

for w in movie_reviews.words():
    if w not in stop_words2:
        all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))
print(all_words["stupid"])  
