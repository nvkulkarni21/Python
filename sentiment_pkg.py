#File: sentiment_mod.py
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize

sentiarray = []

documents_f = open("documents.pickle", "rb")
documents = pickle.load(documents_f)
documents_f.close()




word_features5k_f = open("word_features5k.pickle", "rb")
word_features = pickle.load(word_features5k_f)
word_features5k_f.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


"""
featuresets_f = open("featuresets.pickle", "rb")
featuresets = pickle.load(featuresets_f)
featuresets_f.close()
"""

featuresets = [(find_features(rev), category) for (rev, category) in documents]

random.shuffle(featuresets)
#print(len(featuresets))

testing_set = featuresets[10000:]
training_set = featuresets[:10000]



open_file = open("originalnaivebayes5k.pickle", "rb")
classifier = pickle.load(open_file)
open_file.close()




def sentiment(text):
    feats = find_features(text.lower())
    #sentiarray.append(classifier.classify(feats))
    return classifier.classify(feats)

"""
print ( sentiment("Tainer is good") )
print ( sentiment("Tainer is best") )
print ( sentiment("Tainer is expert") )
print ( sentiment("Tainer is knowledgable") )
print ( sentiment("Tainer is interactive") )

print ( sentiment("This is stupid") )
print ( sentiment("Tainer is worst") )
print ( sentiment("Tainer is dull") )
"""



