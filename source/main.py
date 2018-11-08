from WebScrapping.search import searchWord
import csv
import pandas as pd
import pickle
import time

with open('save1.p', 'rb') as f:
    data_1 = pickle.load(f)

with open('save2.p', 'rb') as f:
    data_2 = pickle.load(f)

xl = pd.read_excel('sentence.xlsx', header=None)

p_alternative = []
for row in xl.iterrows():
    number = row[1][2]
    p_alternative.append(number)
    print()



try:
    with open('memo-sentence.p', 'rb') as f:
        memo = pickle.load(f)
except FileNotFoundError:
    memo = {}

result = []

try:
    for i in range(1001):
        print('sentence number', i+1)
        alternative1 = data_1[i]
        alternative2 = data_2[i]
        # print(alternative1, alternative2)

        if i not in memo:
            time.sleep(5)
            sentences1 = searchWord(alternative1)
            time.sleep(60)
            sentences2 = searchWord(alternative2)
            time.sleep(30)
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
    pickle.dump(memo, open('memo-sentence.p', "wb"))
    pickle.dump(p_alternative, open("correct_alt.p", "wb"))
except Exception:
    print(Exception)
    pickle.dump(a, open("save3.p", "wb"))
    pickle.dump(memo, open('memo-sentence.p', "wb"))
    pickle.dump(p_alternative, open("correct_alt.p", "wb"))
except KeyboardInterrupt:
    pickle.dump(a, open("save3.p", "wb"))
    pickle.dump(memo, open('memo-sentence.p', "wb"))
    pickle.dump(p_alternative, open("correct_alt.p", "wb"))
# for i in sentences:
#     print(i, end='\n\n')


