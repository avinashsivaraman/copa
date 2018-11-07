import pickle

with open('memo-sentence.p', 'rb') as f:
    d = pickle.load(f)

print(d.keys())

for k in d:
    print(d[k]['result'])