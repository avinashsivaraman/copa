from WebScrapping.search import searchWord
import csv
import pandas as pd
import pickle

with open('save1.p', 'rb') as f:
    data_1 = pickle.load(f)

with open('save2.p', 'rb') as f:
    data_2 = pickle.load(f)

n = int(input('Enter the sentence : '))

alternative1 = data_1[n-1]

alternative2 = data_2[n-1]
print(alternative1, alternative2)
sentences1 = searchWord(alternative1)
sentences2 = searchWord(alternative2)

print(len(sentences1))
print('************************')
print(len(sentences2))

if(len(sentences1) > len(sentences2)):
    print('Plausible alternative is 1')
elif len(sentences1) < len(sentences2):
    print('Plausible alternative is 2')
else:
    print('Equal')


# for i in sentences:
#     print(i, end='\n\n')





