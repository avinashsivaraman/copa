import re
import requests
import json


def getObjectsFromAPI(sentence):
    sentence = re.sub(r'(?<!\d)\.(?!\d)', ' .', sentence)
    text = '+'.join(sentence.split(' '))
    url = 'http://bioai8core.fulton.asu.edu/kparser/ParserServlet?text='+text+'&useCoreference=false'
    r1 = requests.get(url)
    try:
        result = json.loads(r1.text)
        return result
    except Exception as e:
        print('Parsing Error removing the sentence')
        return None



if __name__ == '__main__':
    d = getObjectsFromAPI('John loves mia');
    print(d)

