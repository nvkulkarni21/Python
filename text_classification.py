

import nltk
import random
from nltk.corpus import movie_reviews
import pickle

from nltk.classify.scikitlearn import SklearnClassifier
#from sklearn.naive_bayes import MultinomialNB,BernoulliNB
#from sklearn.linear_model import LogisticRegression,SGDClassifier
#from sklearn.svm import SVC, LinearSVC, NuSVC

from statistics import mode
from nltk.tokenize import word_tokenize

documents = [ ]

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append( [ list(movie_reviews.words(fileid)), category ] )
    

random.shuffle(documents)

#print(documents[1])





"""
print( movie_reviews.categories() )

print ( movie_reviews.fileids("neg") )

print ( movie_reviews.fileids("pos") )

print( movie_reviews.raw("pos/cv946_18658.txt") )
"""


all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
#print(all_words.most_common(15))
#print(all_words["stupid"])



word_features = list(all_words.keys())[:5000]


def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features



#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

#print( len( featuresets ))
print( featuresets[1500] )



# set that we'll train our classifier with
training_set = featuresets[:1500]


# set that we'll test against.
testing_set = featuresets[500:]

classifier = nltk.NaiveBayesClassifier.train(training_set)

print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

classifier.show_most_informative_features(15)

#print("Classification:", classifier.classify(testing_set[0][0]) )





"""

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)


BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

"""



save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()





def sentiment(text):
    feats = find_features(text)
    return classifier.classify(feats)


print( sentiment("Best movie ! This movie was awesome! The acting was great! Nice experiance !"))
print( sentiment("This movie was utter junk. There were absolutely 0 pythons. I don't see what the point was at all. Horrible movie, 0/10"))
print( sentiment("It was stupid movie. Just waste of time! "))
print( sentiment("Best  ! Excellent !  nice ! worth ! Superb ! "))


"""

import nltk
import random
from nltk.corpus import movie_reviews
import pickle
classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()
classifier.show_most_informative_features(15)
"""


