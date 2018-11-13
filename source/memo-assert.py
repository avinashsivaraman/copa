import pickle



with open('memo-sentence-full.p', 'rb') as f:
    correct = pickle.load(f)



print(type(correct))
for k, v in correct.items():
    print(v["result"])

