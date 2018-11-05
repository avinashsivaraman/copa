from WebScrapping.search import searchWord
import csv
import pandas as pd
import pickle

with open('save1.p', 'rb') as f:
    data_1 = pickle.load(f)

with open('save2.p', 'rb') as f:
    data_2 = pickle.load(f)

#n = int(input('Enter the sentence : '))

for i in range(1,1001):

    alternative1 = data_1[i-1]
    alternative2 = data_2[i-1]
    print(alternative1, alternative2)
    sentences1 = searchWord(alternative1)
    sentences2 = searchWord(alternative2)

    print(len(sentences1))
    print('************************')
    print(len(sentences2))

    if(len(sentences1) > len(sentences2)):
        a = 1
        print('Plausible alternative is 1')
    elif len(sentences1) < len(sentences2):
        a = 2
        print('Plausible alternative is 2')
    else:
        a = 3
        print('Equal')

    pickle.dump ( a, open("save3.p", "wb"))
# for i in sentences:
#     print(i, end='\n\n')





