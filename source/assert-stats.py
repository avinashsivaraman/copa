# import pickle
#
# with open('correct_alt.p', 'rb') as f:
#     correct = pickle.load(f)
# # print(len(correct))
# print("Google and Bing")
# total = 0
# intersection = 0
# temp = []
# file = 'memo-sentence-full.p'
# with open(file, 'rb') as f:
#     memoCurrent = pickle.load(f)
#     for i in memoCurrent:
#         total += 1
#         if memoCurrent[i]["result"] == correct[i]:
#             intersection += 1
#         temp.append(memoCurrent[i]["result"])
#
#
# print("Correct stats")
# print(len(list(filter(lambda x: x == 1, correct))))
# print(len(list(filter(lambda x: x == 2, correct))))
# print()
# print("Actual stats")
# print(len(list(filter(lambda x: x == 1, temp))))
# print(len(list(filter(lambda x: x == 2, temp))))
# print(len(list(filter(lambda x: x == 3, temp))))
# print()
# print("No of correct result")
# print(intersection)
# # print(total)
# print()
# print("Accuracy", intersection / total)
#
# bing_results = {}
# with open('memo-sentence-bing-0.p', 'rb') as f:
#     bing_results.update(pickle.load(f))
# with open('memo-sentence-bing-60.p', 'rb') as f:
#     bing_results.update(pickle.load(f))
# with open('memo-sentence-bing-107.p', 'rb') as f:
#     bing_results.update(pickle.load(f))
# with open('memo-sentence-bing-200.p', 'rb') as f:
#     bing_results.update(pickle.load(f))
# with open('memo-sentence-bing-255.p', 'rb') as f:
#     bing_results.update(pickle.load(f))
# with open('memo-sentence-bing-300.p', 'rb') as f:
#     bing_results.update(pickle.load(f))
# with open('memo-sentence-bing-334-1000.p', 'rb') as f:
#     bing_results.update(pickle.load(f))
#
# pickle.dump(bing_results, open("memo-sentence-full-bing.p", "wb"))
#
# print("\nBing")
# total1 = 0
# intersection1 = 0
# temp1 = []
# file1 = 'memo-sentence-full-bing.p'
# with open(file1, 'rb') as f:
#     memoCurrent = pickle.load(f)
#     for i in memoCurrent:
#         total1 += 1
#         if memoCurrent[i]["result"] == correct[i]:
#             intersection1 += 1
#         temp1.append(memoCurrent[i]["result"])
#
#
# print("Correct stats")
# print(len(list(filter(lambda x: x == 1, correct))))
# print(len(list(filter(lambda x: x == 2, correct))))
# print()
# print("Actual stats")
# print(len(list(filter(lambda x: x == 1, temp1))))
# print(len(list(filter(lambda x: x == 2, temp1))))
# print(len(list(filter(lambda x: x == 3, temp1))))
# print()
# print("No of correct result")
# print(intersection1)
# # print(total)
# print()
# print("Accuracy", intersection1 / total1)


import pickle
d = pickle.load(open('data/filterSentence_10_20_attempt_1.p', 'rb'))
correct = pickle.load(open('correct_alt.p', 'rb'))

# print(correct[100])
for k, v in d.items():
    s1 = len(v['sentence1'])
    s2 = len(v['sentence2'])

    print(s1, s2, correct[k])