# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:30:49 2018

@author: Vaidhehi

"""

from nltk.tag import StanfordPOSTagger
import os
import pandas as pd
import pickle

path_to_jar = 'stanford-postagger-2018-10-16/stanford-postagger.jar'
english_model = 'stanford-postagger-2018-10-16/models/english-left3words-distsim.tagger'
java_path = "C:/Program Files/Java/jdk1.8.0_192/bin/java.exe"
os.environ['JAVAHOME'] = java_path

tagger = StanfordPOSTagger(english_model, path_to_jar, encoding='utf-8')
xl = pd.read_excel('sentence.xlsx', header=None)

removePOSTag = ['DT', 'IN', 'PRP$', 'CD', 'EX', 'LS', 'PRP']

print('Running')
query_1 = []
for row in xl.iterrows():
    text = row[1][0]
    tagged_sent = tagger.tag(text.split())
    df = pd.DataFrame(tagged_sent,columns=['token','pt'])

    for i in removePOSTag:
        df = df[df.pt != i]

    print(list(df['token']))
    a1_list = list(df['token'])
    query_1.append(a1_list)
    print()

pickle.dump ( query_1, open( "save1.p", "wb"))
query_2 = []
for row in xl.iterrows():
    text = row[1][1]
    tagged_sent = tagger.tag(text.split())
    df1 = pd.DataFrame(tagged_sent, columns=['token', 'pt'])

    for i in removePOSTag:
        df1 = df1[df1.pt != i]

    print(list(df1['token']))
    a2_list = list(df1['token'])
    query_2.append(a2_list)
    print()



pickle.dump ( query_2, open( "save2.p", "wb"))
