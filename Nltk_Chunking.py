# -*- coding: utf-8 -*-

#%%
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
    ''' 
    PunktSentenceTokenizer: A sentence tokenizer which uses an unsupervised algorithm 
    to build a model for abbreviation words, collocations, and words that start
    sentences; and then uses that model to find sentence boundaries.
    This approach has been shown to work well for many European
    languages.
    '''

#%%
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

#%%
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)


#%%
def process_content():
    try:
        for i in tokenized[:1]:
            print(i)
            words = nltk.word_tokenize(i)
            '''word_tokenize: Return a tokenized copy of text, using NLTK's
            recommended word tokenizers.'''
            tagged = nltk.pos_tag(words)
            '''A part-of-speech tagger, or POS-tagger, processes a sequence of words,
            and attaches a part of speech tag to each word '''
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()     

    except Exception as e:
        print(str(e))

#%%
process_content()


# %%
# SIMPLE EXAMPLE
sentence= ("the little yellow dog barked at the cat")
tokenized = custom_sent_tokenizer.tokenize(sentence)

#%%
def process_content_simple_example():
    try:
        for i in tokenized[:1]:
            words = nltk.word_tokenize(i)
            '''word_tokenize: Return a tokenized copy of text, using NLTK's
            recommended word tokenizers.'''
            tagged = nltk.pos_tag(words)
            '''A part-of-speech tagger, or POS-tagger, processes a sequence of words,
            and attaches a part of speech tag to each word '''
            chunkGram = "NP: {<DT>?<JJ>*<NN><VBD>}" 
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()     

    except Exception as e:
        print(str(e))

process_content_simple_example()

# %%
