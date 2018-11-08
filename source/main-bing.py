from WebScrapping.CustomSearch import searchBing
import csv
import pandas as pd
import pickle
import time

with open('save1.p', 'rb') as f:
    data_1 = pickle.load(f)

with open('save2.p', 'rb') as f:
    data_2 = pickle.load(f)


try:
    with open('memo-sentence-bing-334.p', 'rb') as f:
        memo = pickle.load(f)
except FileNotFoundError:
    memo = {}

result = []

try:
    for i in range(334, 400):
        print('sentence number', i+1)
        alternative1 = data_1[i]
        alternative2 = data_2[i]
        # print(alternative1, alternative2)

        if i not in memo:
            sentences1, sentences2 = searchBing(alternative1, alternative2)
            time.sleep(10)
            memo[i] = {
                'sentences1': sentences1,
                'sentences2': sentences2
            }

        else:
            sentences1 = memo[i]['sentences1']
            sentences2 = memo[i]['sentences2']

        if(len(sentences1) > len(sentences2)):
            a = 1
            print('Plausible alternative is 1')
        elif len(sentences1) < len(sentences2):
            a = 2
            print('Plausible alternative is 2')
        else:
            a = 3
            print('Equal')
        result.append(a)
        memo[i]['result'] = a
    pickle.dump ( a, open("save3.p", "wb"))
    pickle.dump(memo, open('memo-sentence-bing-334.p', "wb"))
except Exception as e:
    print(str(e))
    pickle.dump(a, open("save3.p", "wb"))
    pickle.dump(memo, open('memo-sentence-bing-334.p', "wb"))
except KeyboardInterrupt:
    pickle.dump(a, open("save3.p", "wb"))
    pickle.dump(memo, open('memo-sentence-bing-334.p', "wb"))
# for i in sentences:
#     print(i, end='\n\n')


