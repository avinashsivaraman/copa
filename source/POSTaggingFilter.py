from nltk.tag import StanfordPOSTagger
import pandas as pd
import pickle
import re

path_to_jar = 'stanford-postagger-2018-10-16/stanford-postagger.jar'
english_model = 'stanford-postagger-2018-10-16/models/english-left3words-distsim.tagger'

removePOSTag = ["CC", "CD", "DT", "EX", "FW", "LS", "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$", "RP", "SYM", "UH", "WDT", "WP", "WP$", "WRB"]
tagger = StanfordPOSTagger(english_model, path_to_jar, encoding='utf-8')


# java_path = "C:/Program Files/Java/jdk-9.0.1/bin/java.exe"
# os.environ['JAVAHOME'] = java_path

def runFilterSentence(sentence):
    sentence = re.sub(r'(?<!\d)\.(?!\d)', ' .', sentence)
    tagged_sent = tagger.tag(sentence.split())
    df = pd.DataFrame(tagged_sent, columns=['token', 'pt'])
    for i in removePOSTag:
        df = df[df.pt != i]
    return df.values


if __name__ == "__main__":
    xl = pd.read_excel('sentence.xlsx', header=None)

    print('Running')
    query_1 = []
    try:
        for row in xl.iterrows():
            text = re.sub(r'(?<!\d)\.(?!\d)', ' ', row[1][0])
            text1 = re.sub(r'(?<!\d)\.(?!\d)', ' ', row[1][1])
            print(text)
            print(text1)
            tagged_sent = tagger.tag(text.split())
            tagged_sent1 = tagger.tag(text1.split())
            df = pd.DataFrame(tagged_sent, columns=['token', 'pt'])
            df1 = pd.DataFrame(tagged_sent1, columns=['token', 'pt'])
            for i in removePOSTag:
                df = df[df.pt != i]
                df1 = df1[df1.pt != i]
            d = {
                'sentence_query_word_1': list(df['token']),
                'sentence_query_word_2': list(df1['token']),
                'sentence1': df.values,
                'sentence2': df1.values
            }
            query_1.append(d)
            print(len(query_1))

        pickle.dump(query_1, open("data/queryWordsWithTag.p", "wb"))
        print("Dumped successfully")
    except Exception as e:
        print(e)
        pickle.dump(query_1, open("data/queryWordsWithTag.p", "wb"))
    except KeyboardInterrupt:
        pickle.dump(query_1, open("data/queryWordsWithTag.p", "wb"))
        print("dumped before keyboard interrupt")

