import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle

from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
#from nltk.sentiment.vader import SentimentIntensityAnalyzer


 
paragraph = "Super movie but songs were boring"
#print(sentiment("Just waste of time"))
#lines_list = tokenize.sent_tokenize(paragraph)
#sentences.extend(lines_list)

sid = SentimentIntensityAnalyzer()



ss = (sid.polarity_scores(paragraph))


for k in sorted(ss):
         print ( k )
         print  ( ss[k] )


