from WebScrapping.CustomSearch import searchBing
import pickle
import time

with open('save1.p', 'rb') as f:
    data_1 = pickle.load(f)

with open('save2.p', 'rb') as f:
    data_2 = pickle.load(f)


try:
    with open('memo-sentence-full-bing.p', 'rb') as f:
        memo = pickle.load(f)
except FileNotFoundError:
    memo = {}

try:
    for i in range(1001):
        print('sentence number', i+1)
        temp = []
        alternative1 = data_1[i]
        alternative2 = data_2[i]

        if i not in memo:
            sentences1, sentences2 = searchBing(alternative1, alternative2)
            time.sleep(10)
            memo[i] = {
                'sentences1': sentences1,
                'sentences2': sentences2,
            }

        else:
            sentences1 = memo[i]['sentences1']
            sentences2 = memo[i]['sentences2']


        if len(sentences1) > len(sentences2):
            a = 1
            temp = [1, -1]
            print('Plausible alternative is 1')
        elif len(sentences1) < len(sentences2):
            a = 2
            temp = [-1, 1]
            print('Plausible alternative is 2')
        else:
            a = 3
            temp = [0, 0]
            print('Equal')

        memo[i]['result'] = temp
        memo[i]['queryparameter1'] = alternative1
        memo[i]['queryparameter2'] = alternative2
    pickle.dump(memo, open('memo-sentence-full-bing.p', "wb"))
except Exception as e:
    print(str(e))
    pickle.dump(memo, open('memo-sentence-full-bing.p', "wb"))
except KeyboardInterrupt:
    pickle.dump(memo, open('memo-sentence-full-bing.p', "wb"))
# for i in sentences:
#     print(i, end='\n\n')


