# Fuente: https://pythonprogramming.net/

#%%
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words=("python","pythoner","pythoning","pythoned", "pythonly")

for w in example_words:
    print(ps.stem(w))


# %%
new_text="It is very important to be pythonly while wou are pythoning with python. All pythoners have pythoned poorly at least once."

words= word_tokenize(new_text)

for w in words:
    print(ps.stem(w))

# %%
# ejemplo en español
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

ps = SnowballStemmer('spanish')

example_words=("correr","corriendo","corretear","corrida", "corrán")

for w in example_words:
    print(ps.stem(w))


# %%
new_text="El perro fue llamado a comer. Sin embargo, el simvergüenza no apareció. Quizás no tenía ganas de estar comiendo todo el día, porque ayer comió mucho. Y si no estoy mal, creo que se ha comido el pollo de la mesa."

words= word_tokenize(new_text)

lista=[]

for w in words:
    lista.append(ps.stem(w))

print(set(lista))

# %%
raw = """DENNIS: Listen, strange women lying in ponds distributing swords
... is no basis for a system of government.  Supreme executive power derives from
... a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = word_tokenize(raw)
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()

print([porter.stem(t) for t in tokens])
print([lancaster.stem(t) for t in tokens])

# %%
