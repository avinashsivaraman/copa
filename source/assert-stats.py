import pickle



with open('correct_alt.p', 'rb') as f:
    correct = pickle.load(f)
# print(len(correct))
total = 0
intersection = 0
temp = []
file = 'memo-sentence-full.p'
with open(file, 'rb') as f:
    memoCurrent = pickle.load(f)
    for i in memoCurrent:
        total += 1
        if memoCurrent[i]["result"] == correct[i]:
            intersection += 1
        temp.append(memoCurrent[i]["result"])


print("Correct stats")
print(len(list(filter(lambda x: x == 1, correct))))
print(len(list(filter(lambda x: x == 2, correct))))
print()
print("Actual stats")
print(len(list(filter(lambda x: x == 1, temp))))
print(len(list(filter(lambda x: x == 2, temp))))
print(len(list(filter(lambda x: x == 3, temp))))
print()
print("No of correct result")
print(intersection)
# print(total)
print()
print("Accuracy", intersection / total)