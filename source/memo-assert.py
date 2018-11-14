import pickle
from source.POSTaggingFilter import runFilterSentence

def splitquery(query):
    ind = 0
    for element in query:
        if '.' in element:
            return query[0:ind] + query[ind].split('.') + query[ind + 1:]
        ind = ind + 1

def isValidSentence(actual, current):
    # TODO: We have to filter the sentence based on the POS Tag and word
    print(actual)
    print(current)


with open('memo-sentence-full-bing.p', 'rb') as f:
    correct = pickle.load(f)

filteredSentence1 = []
filteredSentence2 = []

for k, v in correct.items():
    sentence1 = v["sentences1"]
    queryParameter1 = v["queryparameter1"]
    queryParameter2 = v["queryparameter2"]
    i = 0
    for each in sentence1:
        currentIndex = 0
        sentenceList = each.split('.')
        temp = []
        for sentence in sentenceList:
            if(isValidSentence(queryParameter1,runFilterSentence(sentence))):
                temp.append(sentence)
        filteredSentence1.append(temp)
        i += 1
        break
    break
