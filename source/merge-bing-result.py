import pickle

fileNames = ["cache-bing-sentence-1000.p", "cache-bing-sentence-200.p", "cache-bing-sentence-400.p", "cache-bing-sentence-600.p", "cache-bing-sentence-800.p"]


d = {}

for file in fileNames:
    d.update(pickle.load(open(file, 'rb')))

pickle.dump(d, open('data/cache-bing-sentence.p', 'wb'))
print('Dumped successfully')
