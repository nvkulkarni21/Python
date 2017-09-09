import nltk
import random
from nltk.corpus import movie_reviews
import pickle


classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()
classifier.show_most_informative_features(15)



def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features



def sentiment(text):
    feats = find_features(text)
    return classifier.classify(feats)



print(s.sentiment("This movie was awesome! The acting was great, plot was wonderful, and there were pythons...so yea!"))
print(s.sentiment("This movie was utter junk. There were absolutely 0 pythons. I don't see what the point was at all. Horrible movie, 0/10"))
print(s.sentiment("It was stupid movie. Just waste of time! "))
