from WebScrapping.CustomSearch import searchBing
import pickle
import time

start = 800
end = 1000
with open('data/queryWordsWithTag.p', 'rb') as f:
    queryWords = pickle.load(f)

try:
    with open('cache-bing-sentence-'+str(end)+'.p', 'rb') as f:
        memo = pickle.load(f)
except FileNotFoundError:
    memo = {}

try:
    for i in range(start, end):
        print('sentence number', i+1)
        temp = []
        alternative1 = queryWords[i]['sentence_query_word_1']
        alternative2 = queryWords[i]['sentence_query_word_2']

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

        print(len(sentences1), len(sentences2))
        if len(sentences1) > len(sentences2):
            temp = [1, -1]
            print('Plausible alternative is 1')
        elif len(sentences1) < len(sentences2):
            temp = [-1, 1]
            print('Plausible alternative is 2')
        else:
            temp = [0, 0]
            print('Equal')

        memo[i]['result'] = temp
        memo[i]['queryparameter1'] = queryWords[i]["sentence1"]
        memo[i]['queryparameter2'] = queryWords[i]["sentence2"]
    pickle.dump(memo, open('cache-bing-sentence-'+str(end)+'.p', "wb"))
except Exception as e:
    print(str(e))
    pickle.dump(memo, open('cache-bing-sentence-'+str(end)+'.p', "wb"))
except KeyboardInterrupt:
    pickle.dump(memo, open('cache-bing-sentence-'+str(end)+'.p', "wb"))
# for i in sentences:
#     print(i, end='\n\n')


