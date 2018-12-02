import pickle
import pandas as pd
from WebScrapping.KparserAPI import getObjectsFromAPI
# from nltk import word_tokenize
# from nltk.corpus import stopwords

# Loading the data and it is accessed by all the functions

# print(stopwords.words('english'))
# # Add the words or pattern which we should remove from the sentence
# remove_list = stopwords.words('english')
# remove_list.extend(["..."])
#
#
# def remove_stopwords(sentence):
#     token = [token for token in word_tokenize(sentence) if token.lower() not in remove_list]
#     return ' '.join(token)


def get_similarity_score(alternative, query):
    similarity_array = []
    for o in alternative:
        currmax = 0
        for e in query:
            root_data_o = o['data']['word'].split('-')[1]
            root_data_e = e['data']['word'].split('-')[1]
            if root_data_e == root_data_o:
                #Question: How to parse ?
                print('valid root')
    return sum(similarity_array) / len(similarity_array) if len(similarity_array) else 0


with open('data/cache-bing-sentence.p', 'rb') as f:
    correct = pickle.load(f)

xl = pd.read_excel('sentence.xlsx', header=None)

try:
    result = pickle.load('data/kparserresults.p', 'rb')
except Exception:
    result = {}


for i, row in xl.iterrows():
    searchedResult1, searchedResult2 = correct[i]['sentences1'], correct[i]['sentences2']
    alternative1, alternative2 = row[0], row[1]
    score1, score2 = 0, 0
    i = 0
    for each in searchedResult1:
        # each = remove_stopwords(each)
        print('Processing the sentence', i+1)
        kObjectForQuery = getObjectsFromAPI(each)
        kObjectForAlternative = getObjectsFromAPI(alternative1)
        # Skipping the sentence which can't be parsed by kparser.
        if kObjectForQuery == None:
            continue
        print(get_similarity_score(kObjectForAlternative, kObjectForQuery))
        i+=1
        # score1 = max(score1, get_similarity_score(kObjectForQuery, kObjectForAlternative))
        # break
    # for each in searchedResult2:
    #     each = remove_stopwords(each)
    #     kObjectForQuery = getObjectsFromAPI(each)
    #     kObjectForAlternative = getObjectsFromAPI(alternative2)
    #     # TODO: Implement the algorithm here
    #     score2 = max(score2, get_similarity_score(kObjectForQuery, kObjectForAlternative))
    # if score1 > score2:
    #     result[i] = [1, 0]
    # elif score2 > score1:
    #     result[i] = [0, 1]
    # else:
    #     result[i] = [0, 0]
    break

pickle.dump(result, open('data/kparserresults.p', 'wb'))
print('results dumped successfully')
