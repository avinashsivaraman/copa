import pickle
from source.POSTaggingFilter import runFilterSentence
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
import nltk
from threading import Thread
import re

nltk.download('wordnet')
lemm = WordNetLemmatizer()

#Loading the data and it is accessed by all the functions
with open('data/cache-bing-sentence.p', 'rb') as f:
    correct = pickle.load(f)

startIndex = 20
endIndex = 30
a = '1'
filename = 'data/filterSentence_'+str(startIndex)+'_'+str(endIndex)+'_attempt_'+a+'.p'
try:
    fOld = pickle.load(open(filename, 'rb'))
except Exception:
    fOld = {}


try:
    memoLem = pickle.load(open('data/memoLemmatize.p', 'rb'))
except FileNotFoundError:
    memoLem = {}

# includedPOS = ["IN", "JJ", "JJR", "JJS", "RB", "RBR", "RBS", "TO", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]

def getPOSTag(tag):
    if tag in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]:
        return wn.VERB
    elif tag in ["JJ", "JJR", "JJS"]:
        return wn.ADJ
    elif tag in ["RB", "RBR", "RBS"]:
        return wn.ADV
    elif tag is 'IN':
        return wn.IN
    else:
        return wn.ADV

def splitquery(query):
    ind = 0
    for element in query:
        if '.' in element:
            return query[0:ind] + query[ind].split('.') + query[ind + 1:]
        ind = ind + 1


def lemmatize(word, wtag):
    return lemm.lemmatize(word, pos=getPOSTag(wtag))

def isValidSentence(actual, current):
    parseLength = 0
    for every in current:
        e1, eTag = every
        if (parseLength < len(actual)):
            a1, aTag = actual[parseLength][0], actual[parseLength][1]
            e1 = lemmatize(e1, eTag)
            a1 = lemmatize(a1, aTag)
            if (e1 == a1):
                parseLength += 1
        else:
            break
    if (parseLength == len(actual)):
        return True
    return False

def extractValidSentence(sentence, queryParameter):
    result = []
    if sentence != '' and isValidSentence(queryParameter, runFilterSentence(sentence)):
        print('Valid one')
        result.append(sentence)
    return result

def filterTheSentence(sentNo, alternativeNo, sentences, queryparameter):
    filteredSentence = []
    print('Sentence number', sentNo)
    print('Processing the alternative ', alternativeNo)
    i = 1
    for each in sentences:
        # print('Processing the {}th sentence'.format(i))
        temp = extractValidSentence(each, queryparameter)
        if(len(temp) != 0):
            print('Valid sentence')
            print(temp)
            filteredSentence.append(temp)
        i+=1
    return filteredSentence

def filterSentenceWithKey(name,end, start = 0):
    try:
        d = {}
        for each in range(start, end):
            print('Processing the sentence ', each+1)
            if(each in fOld):
                continue
            v = correct[each]
            sentence1 = v["sentences1"]
            sentence2 = v["sentences2"]
            queryParameter1 = v["queryparameter1"]
            queryParameter2 = v["queryparameter2"]
            i = 1
            print(name + 'Running the alternative', i)
            d[each] = {
                'sentence1': filterTheSentence(each,1,sentence1, queryParameter1),
                'sentence2': filterTheSentence(each,2,sentence2, queryParameter2)
            }        
        return d
    except KeyboardInterrupt:
        pickle.dump(memoLem, open('data/memoLemmatize.p', 'a'))
        pickle.dump(d, open(filename, 'wb'))


class FilterSentenceWorker(Thread):
    def __init__(self, name, startIndex, endIndex):
        Thread.__init__(self)
        self.name = name
        self.startIndex = startIndex
        self.endIndex = endIndex

    def run(self):
        f1, f2 = filterSentenceWithKey(name=self.name,start=self.startIndex, end=self.endIndex)
        filename = 'data/filterSentence_'+str(self.startIndex)+'_'+str(self.endIndex)
        pickle.dump([f1, f2], open(filename, 'wb'))


if __name__ == '__main__':
    #Code for the running the thread
    # step = 10
    # i = 0
    # for iternationCount in range(i, 10):
    #     start = iternationCount*step
    #     FilterThread = FilterSentenceWorker(name="{}".format(iternationCount), startIndex=start, endIndex=start+10)
    #     FilterThread.start()
    #     print('Threads are running')

    f = filterSentenceWithKey(name='main-thread',start=startIndex, end=endIndex)
    pickle.dump(f, open(filename, 'wb'))

