#%%
import spacy

#%%
nlp = spacy.load("es_core_news_sm")
#nlp = spacy.load("en_core_web_sm")

# %%
sample=("Este es un texto rápido de prueba para usar la librería spacy, sin embargo esperamos que no sea un fracaso el uso del mismo, DNP, PRESIDENCIA DE LA REPUBLICA")
print(sample)

# %%
from spacy import displacy
from spacy.lang.es.stop_words import STOP_WORDS

# %%
nlp = spacy.load("es_core_news_sm")
doc = nlp(sample)
print(doc)

# %%
for token in doc:
    print(token)

# %%
for word in doc:
    if not word.is_stop == True:
        print(word)

# %%
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)

# %%
<<<<<<< HEAD
displacy.render(doc, style='dep', jupyter=True, options={'distance': 70})

=======

displacy.render(doc, style='dep', jupyter=True, options={'distance': 70})

print(displacy.render(doc, style='dep', jupyter=True, options={'distance': 70}))


>>>>>>> master
# %%
# Print out named entities
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
print(ent)

# %%
<<<<<<< HEAD
=======

displacy.render(doc, style='ent', jupyter=True)

>>>>>>> master
displacy.render(doc, style='ent', jupyter=True)
