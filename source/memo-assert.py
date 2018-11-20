import pickle
from POSTaggingFilter import runFilterSentence
from nltk.stem import WordNetLemmatizer
import nltk
from threading import Thread

nltk.download('wordnet')
lemm = WordNetLemmatizer()


try:
    memoLem = pickle.load(open('data/memoLemmatize.p', 'rb'))
except FileNotFoundError:
    memoLem = {}

def splitquery(query):
    ind = 0
    for element in query:
        if '.' in element:
            return query[0:ind] + query[ind].split('.') + query[ind + 1:]
        ind = ind + 1


def lemmatize(word):
    if word in memoLem:
        return memoLem[word]
    else:
        lem = lemm.lemmatize(word)
        memoLem[word] = lem
        return lem


def isValidSentence(actual, current):
    parseLength = 0
    # for
    for every in current:
        e1, eTag = every
        if (parseLength < len(actual)):
            a1, aTag = actual[parseLength][0], actual[parseLength][1]
            e1 = lemmatize(e1)
            a1 = lemmatize(a1)
            if (e1 == a1):
                parseLength += 1
        else:
            break
    if (parseLength == len(actual)):
        return True
    return False


def extractValidSentence(sentences, queryParameter):
    sentenceList1 = sentences.split('.')
    result = []
    for sentence in sentenceList1:
        if sentence != '':
            if isValidSentence(queryParameter, runFilterSentence(sentence)):
                result.append(sentence)
    return result


with open('memo-sentence-full-bing.p', 'rb') as f:
    correct = pickle.load(f)


def filterSentenceWithKey(name,end, start = 0):
    try:
        filteredSentence1 = []
        filteredSentence2 = []
        for each in range(start, end):
            v = correct[each]
            sentence1 = v["sentences1"]
            sentence2 = v["sentences2"]
            queryParameter1 = v["queryparameter1"]
            queryParameter2 = v["queryparameter2"]
            i = 1
            print(name + 'Running the alternative', i)
            for each in sentence1:
                print(name + 'Running the sentence ', i)
                temp = extractValidSentence(each, queryParameter1)
                if (len(temp)):
                    print('Got a valid one', each, queryParameter1)
                i += 1
                filteredSentence1.append(temp)
            for each in sentence2:
                temp = extractValidSentence(each, queryParameter2)
                filteredSentence2.append(temp)
        return filteredSentence1, filteredSentence2
    except KeyboardInterrupt:
        pickle.dump(memoLem, open('data/memoLemmatize.p', 'a'))


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


step = 10
i = 0
for iternationCount in range(i, 10):
    start = iternationCount*step
    FilterThread = FilterSentenceWorker(name="{}".format(iternationCount), startIndex=start, endIndex=start+10)
    FilterThread.start()
    print('Threads are running')

