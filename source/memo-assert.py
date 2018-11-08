import pickle



with open('memo-sentence.p', 'rb') as f:
    correct = pickle.load(f)

print(correct.keys())