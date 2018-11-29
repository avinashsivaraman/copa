import pickle
import pandas as pd
from WebScrapping.KparserAPI import getObjectsFromAPI
from nltk import word_tokenize
from nltk.corpus import stopwords

# Loading the data and it is accessed by all the functions

print(stopwords.words('english'))
# Add the words or pattern which we should remove from the sentence
remove_list = stopwords.words('english')
remove_list.extend(["..."])


def remove_stopwords(sentence):
    token = [token for token in word_tokenize(sentence) if token.lower() not in remove_list]
    return ' '.join(token)


def get_similarity_score(o, e):
    pass


with open('data/cache-bing-sentence.p', 'rb') as f:
    correct = pickle.load(f)

xl = pd.read_excel('sentence.xlsx', header=None)
result = {}

for i, row in xl.iterrows():
    searchedResult1, searchedResult2 = correct[i]['sentences1'], correct[i]['sentences2']
    alternative1, alternative2 = remove_stopwords(row[1][0]), remove_stopwords(row[1][0])
    score1, score2 = 0, 0
    for each in searchedResult1:
        each = remove_stopwords(each)
        kObjectForQuery = getObjectsFromAPI(each)
        kObjectForAlternative = getObjectsFromAPI(alternative1)
        score1 = max(score1, get_similarity_score(kObjectForQuery, kObjectForAlternative))
    for each in searchedResult2:
        each = remove_stopwords(each)
        kObjectForQuery = getObjectsFromAPI(each)
        kObjectForAlternative = getObjectsFromAPI(alternative2)
        # TODO: Implement the algorithm here
        score2 = max(score2, get_similarity_score(kObjectForQuery, kObjectForAlternative))
    if score1 > score2:
        result[i] = [1, 0]
    elif score2 > score1:
        result[i] = [0, 1]
    else:
        result[i] = [0, 0]

pickle.dump(result, open('data/kparserresults.p', 'wb'))
print('results dumped successfully')
