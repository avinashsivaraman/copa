# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:30:49 2018

@author: Vaidhehi
"""

from nltk.tag import StanfordPOSTagger
import os
import pandas as pd
import csv
import pickle

path_to_jar = 'D:/NLP/Project/stanford-postagger-2018-10-16/stanford-postagger.jar'
english_model = 'D:/NLP/Project/stanford-postagger-2018-10-16/models/english-left3words-distsim.tagger'
java_path = "C:/Program Files/Java/jdk1.8.0_192/bin/java.exe"
os.environ['JAVAHOME'] = java_path

tagger = StanfordPOSTagger(english_model, path_to_jar, encoding='utf-8')
xl = pd.read_excel('sentence.xlsx', header=None)

print('Running')
alternative1 = []
for row in xl.iterrows():
    text = row[1][0]
    tagged_sent = tagger.tag(text.split())
    df = pd.DataFrame(tagged_sent,columns=['token','Pos-Tag'])
    alternative1.append(df)

pickle.dump( alternative1, open( "save.p", "wb" ) )
print('Dumped the first pickle')
alternative2 = []
for row in xl.iterrows():
    text = row[1][1]
    tagged_sent = tagger.tag(text.split())
    df1 = pd.DataFrame(tagged_sent, columns=['token', 'Pos-Tag'])
    alternative2.append(df1)

pickle.dump ( alternative2, open( "save1.p", "wb") )

print('Dumped the first pickle')
with open('save.p', 'rb') as f:
    data = pickle.load(f)
    print(data)

with open('save1.p', 'rb') as f:
    data = pickle.load(f)
    print(data)
print('Dumped the first pickle')