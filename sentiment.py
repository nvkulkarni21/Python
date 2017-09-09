#File: sentiment_mod.py

import nltk
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle

from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
#import nltk.sentiment.vader
from nltk.corpus import stopwords


documents_f = open("documents.pickle", "rb")
documents = pickle.load(documents_f)
documents_f.close()




word_features5k_f = open("word_features5k.pickle", "rb")
word_features = pickle.load(word_features5k_f)
word_features5k_f.close()


def find_features(document):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(document)
    filtered_sentence = [w for w in words if not w in stop_words]
    features = {}
    for w in word_features:
        features[w] = (w in filtered_sentence)

    return features


"""
featuresets_f = open("featuresets.pickle", "rb")
featuresets = pickle.load(featuresets_f)
featuresets_f.close()
"""

featuresets = [(find_features(rev), category) for (rev, category) in documents]

random.shuffle(featuresets)
print(len(featuresets))

testing_set = featuresets[10000:]
training_set = featuresets[:10000]



open_file = open("originalnaivebayes5k.pickle", "rb")
classifier = pickle.load(open_file)
open_file.close()



def sentiment(text):
    feats = find_features(text.lower())
    return classifier.classify(feats)


print(sentiment("This movie was awesome! The acting was great, plot was wonderful, and there were pythons...so yea!"))
print(sentiment("This movie was utter junk. There were absolutely 0 pythons. I don't see what the point was at all. Horrible movie, 0/10"))
print(sentiment("Stupid movie !"))
print(sentiment("Boaring movie !"))
print(sentiment("Just pathatic !"))
print(sentiment("Not a great movie"))
print(sentiment("Wonderful movie"))
print(sentiment("This movie was awesome! The acting was great, plot was wonderful, and there were pythons...so yea!"))
print(sentiment("Super movie but songs were boring"))
print(sentiment("The Bahubali movie was  too good. Songs were catchy. Acting by prabhas was too good.. !"))
print(sentiment("The content was awesome"))
print(sentiment("excellent"))








