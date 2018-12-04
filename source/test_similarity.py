from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
import gensim
import pandas as pd

from gensim.test.utils import common_texts
from gensim.models import Word2Vec
model = Word2Vec(common_texts, size=10000, window=5, min_count=1, workers=4)
word_vectors = model.wv

from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors
fname = get_tmpfile("vectors.kv")
word_vectors.save(fname)
word_vectors = KeyedVectors.load(fname, mmap='r')

from gensim.test.utils import datapath
wv_from_text = KeyedVectors.load_word2vec_format(datapath('word2vec_pre_kv_c'), binary=False)
wv_from_bin = KeyedVectors.load_word2vec_format(datapath("euclidean_vectors.bin"), binary=True)

import gensim.downloader as api
word_vectors = api.load("glove-wiki-gigaword-100")

import os
from nltk.tag import StanfordPOSTagger

path_to_jar = 'stanford-postagger-2018-10-16/stanford-postagger.jar'
english_model = 'stanford-postagger-2018-10-16/models/english-left3words-distsim.tagger'
java_path = "C:/Program Files/Java/jdk-9.0.1/bin/java.exe"
os.environ['JAVAHOME'] = java_path

def remove_punc(my_str):

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in my_str:
        if char not in punctuations:
            no_punct = no_punct + char

# display the unpunctuated string
    return no_punct

tagger = StanfordPOSTagger(english_model, path_to_jar, encoding='utf-8')

removePOSTag = ['DT', 'IN', 'PRP$', 'CD', 'EX', 'LS', 'PRP']
#text1 = "sushi shop"
#text2 = "restaurant"
#text1 = "bad singer"
#text1 = "Scholar pet actions with cast times can now be canceled when ordered to use a different pet action. * Information previously published stated that changes were made to arcanist, summoner, and scholar pet actions."
#text1 = "Original American Gods art by Hugo-winner Julie Dillon. PERFUME OIL BLENDS ... and the thing staring at him wore a buffalo’s head, rank and furry with huge wet eyes. Its body was a man’s body, oiled and slick. ... There was a woman sitting on the grass, under a tree, with a paper tablecloth spread in front of her, and a variety of ..."
#text1 = "mark the shadow cast at first light. To get an accurate read on your direction using shadows, you'll need to first wait for sun to set. When the sun rises in the morning, mark the spot your sun rod casts its first shadow"
#text1 = "Anywhere in the world that is north of the Tropic of Cancer, and that includes all of Europe and the US, the sun will be due south at midday. The tip of the shortest shadow cast by a stick during the course of a day, or any other object like a tree, will point north in the UK, the base of the stick will point south."
#text1 = "The other index card is held in the shadow of the first card. An image of the Sun will appear on the second card. Results. 1. Students observe the Sun as projected on the index card. They describe the appearance of the Sun on the card by writing in their Science Journals. 2."
#text1 = "A transparent body casts no shadow; neither does it reflect light-waves - that is, the perfectly transparent does not. So, avoiding high lights, not only will such a body cast no shadow, but, since it reflects no light, it will also be invisible."
#text1 = "Reinforce the cast shadow shape noticing – the darkest part that sits directly under the apple, the mid tone that makes up the majority of the cast shadow shape whilst keeping a lighter line as you get towards the lightest, softest tail of the cast shadow. Lightly draw the shadow line, it has a slight curve to it."

text1 = "Let seed be grass, and grass turn into hay:” “(I measure time by how a body sways).” “These old bones live to learn her wanton ways:” “I swear she cast a shadow white as stone Ask for details"

text1 = text1.lower()
text1 = remove_punc(text1)

#0.8914
#0.8551
#0.8178
#0.8500
#0.8778

tagged_sent = tagger.tag(text1.split())
df = pd.DataFrame(tagged_sent,columns=['token','pt'])

for i in removePOSTag:
    df = df[df.pt != i]

print(list(df['token']))
a1_list = list(df['token'])

#text2 = "my body cast a shadow over the grass. because The sun was rising."

text2 = "My body cast a shadow over the grass. because The grass was cut."
text2 = text2.lower()
text2 = remove_punc(text2)

tagged_sent = tagger.tag(text2.split())
df = pd.DataFrame(tagged_sent,columns=['token','pt'])

for i in removePOSTag:
    df = df[df.pt != i]

print(list(df['token']))
a2_list = list(df['token'])

sentence1 = a1_list
sentence2 = a2_list
sim = word_vectors.n_similarity(a1_list, a2_list)
print("{:.4f}".format(sim))