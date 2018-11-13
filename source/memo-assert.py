import pickle

def splitquery(query):
    ind = 0
    for element in query:
        if '.' in element:
            return query[0:ind]+query[ind].split('.')+query[ind+1:]
        ind = ind+1

with open('memo-sentence-full-bing.p', 'rb') as f:
    correct = pickle.load(f)


for k, v in correct.items():
    every = v["sentences1"]
    queryParameter1 = splitquery(v["queryparameter1"])
    queryParameter2 = splitquery(v["queryparameter2"])
    i = 0
    for each in every:
        print(i+1, each)
        i+=1
    break