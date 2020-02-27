#%%
# ENGLISH - ENGLISH - ENGLISH - ENGLISH - ENGLISH - ENGLISH - ENGLISH
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# %%
example_sentence = "This is an example showing off stop word filtration."
stop_words=set(stopwords.words("English"))

words=word_tokenize(example_sentence)

filtered_sentence=[]

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)


# %%
# SPANISH - SPANISH - SPANISH - SPANISH - SPANISH - SPANISH - SPANISH - SPANISH
ejemplo_oracion= "el presidente de Colombia es Ivan Duque"
palabras_comunes=set(stopwords.words("Spanish"))
palabras=word_tokenize(ejemplo_oracion)
oracion_final=[]
for w in palabras:
    if w not in palabras_comunes:
        oracion_final.append(w)
print(oracion_final)
 
# %%
ejemplo_oracion= "el presidente de Colombia es Ivan Duque"
palabras_comunes=set(stopwords.words("Spanish"))
palabras=word_tokenize(ejemplo_oracion)
oracion_final=[w for w in palabras if not w in palabras_comunes]
<<<<<<< HEAD
print(oracion_final)

# %%
=======

print(oracion_final)

>>>>>>> master
