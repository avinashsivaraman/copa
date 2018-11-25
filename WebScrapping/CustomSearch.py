import json
import time
import requests


def BingSearch(searchTerm1, searchTerm2):
    subscriptionKey = "****APIKEY*******"

    customConfigId = "bcdd3b33-18f9-4487-b313-c526b76484a1"
    i = 0
    request1 = []
    request2 = []
    while True:
        try:
            url = 'https://api.cognitive.microsoft.com/bingcustomsearch/v7.0/search?q=' + searchTerm1 + '&customConfig=' + customConfigId + '&count=50&offset=' + str(i)
            time.sleep(2)
            r1 = requests.get(url, headers={'Ocp-Apim-Subscription-Key': subscriptionKey})
            time.sleep(2)
            url = 'https://api.cognitive.microsoft.com/bingcustomsearch/v7.0/search?q=' + searchTerm2 + '&customConfig=' + customConfigId + '&count=50&offset=' + str(i)
            time.sleep(2)
            r2 = requests.get(url, headers={'Ocp-Apim-Subscription-Key': subscriptionKey})
            r1Parse = json.loads(r1.text)["webPages"]["value"]
            r2Parse = json.loads(r2.text)["webPages"]["value"]
            request1.extend(list(map(lambda x: x["snippet"], r1Parse)))
            request2.extend(list(map(lambda x: x["snippet"], r2Parse)))
            if len(r1Parse) < 50 or len(r2Parse) < 50:
                break
            if i == 200:
                break
            i = i + 50
        except Exception as e:
            raise Exception(r1.text + r2.text)
    return request1, request2

'''
    value = ["descipt":  1, "snippet": "asdkdjsljdlkafjl]
'''


def searchBing(search1, search2):
    return BingSearch(' '.join(search1), ' '.join(search2))

if __name__ == "__main__":
    one, two = searchBing(["hello", "I", "am", "old"],["hello", "I", "am", "young"])
    print(len(one), len(two))
    print(one, two)