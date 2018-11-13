import pickle



with open('memo-sentence-full-bing.p', 'rb') as f:
    correct = pickle.load(f)


for k, v in correct.items():
    every = v["sentences1"]
    queryParameter = v["queryparameter1"]
    # TODO: Kaviya Implement the algo to split and join the array
    i = 0
    for each in every:
        print(i+1, each)
        i+=1
    break
