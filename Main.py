import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sentiment import sentiment
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
import re
import os
import warnings

warnings.filterwarnings("ignore")


sid = SentimentIntensityAnalyzer()

    
vaderarray = []

def vader(sent):
    #print ("In Vader function.. ")
    sentvader= sent
    sid = SentimentIntensityAnalyzer()
    ss = (sid.polarity_scores(sentvader))
    
    for k in sorted(ss):
         #print ( k )
         #print  ( ss[k] )
         #print  (k, ss[k])
         vaderarray.append([k, ss[k]])
    #print (*vaderarray)
    return(vaderarray)


vaderres=""
sentires=""

pos_cnt=0
neg_cnt=0
strippedString=""

indir = './candidate_feedback/'
for root, dirs, filenames in os.walk(indir):
    #print ( filenames )

    for f in filenames:
        #print( f )
        file_to_read = indir + f
        with open(file_to_read) as o:
                    text = o.read()
                    #print ( text )
                    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
                    #print ( sentences )
                    for line in sentences:

                        strippedString = line.strip()
                        if strippedString == "":
                            break
                                                    
                        print ( strippedString )
                        #vaderres = vader( line )
                        sentires = sentiment(strippedString)
                        if sentires == "pos":
                            pos_cnt=pos_cnt+1
                        if sentires == "neg":
                            neg_cnt=neg_cnt+1


                        ss = (sid.polarity_scores(strippedString))    
                        for k in sorted(ss):
                             print  ( k , ss[k] )
 
    print ( "**************************************************************************************************************************************************" )
    print ( "Output for Naive bayes statistical machine learning statistical algorithm " )
    print ( "Positive occurrence : " + str( pos_cnt )   )
    print ( "Negative occurrence : " + str( neg_cnt )   )       
    print ( "As per Naive bayes statistical machine learning statistical algorithm postive to negative sentiment ratio is : " + str( pos_cnt / neg_cnt ) )           
    print ( "**************************************************************************************************************************************************" )














                        





    
