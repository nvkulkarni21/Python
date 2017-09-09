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

sentires=""
comp_cntV=0
pos_cntV=0
neg_cntV=0
neu_cntV=0
sentcnt=0

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
                        sentcnt = sentcnt + 1                            
                        print ( strippedString )
                        #vaderres = vader( line )
                        sentires = sentiment(strippedString)
                        if sentires == "pos":
                            pos_cnt=pos_cnt+1
                        if sentires == "neg":
                            neg_cnt=neg_cnt+1


                        ss = (sid.polarity_scores(strippedString))    
                        for k in sorted(ss):
                            print (k, ss[k])
                            if k == "compound":
                                comp_cntV=ss[k]+comp_cntV
                            if k == "neg":
                                neg_cntV=ss[k]+neg_cntV
                            if k == "pos":
                                pos_cntV=ss[k]+pos_cntV
                            if k == "neu":
                                neu_cntV=ss[k]+neu_cntV
                        

    print ( "**************************************************************************************************************************************************" )
    print ( "Output for Vader statistics " )
    print ( "Avg Compound occurrence : " + str( comp_cntV /sentcnt )   )
    print ( "Avg Negative occurrence : " + str( neg_cntV / sentcnt)   )
    print ( "Avg Positive occurrence : " + str( pos_cntV /sentcnt )   )
    print ( "Avg Neutral occurrence : "  + str( neu_cntV / sentcnt )   )   
    print ( "**************************************************************************************************************************************************" )

    
    print ( "**************************************************************************************************************************************************" )
    print ( "Output for Naive bayes statistical machine learning statistical algorithm " )
    print ( "Positive occurrence : " + str( pos_cnt )   )
    print ( "Negative occurrence : " + str( neg_cnt )   )       
    print ( "As per Naive bayes statistical machine learning statistical algorithm postive to negative sentiment ratio is : " + str( pos_cnt / neg_cnt ) )           
    print ( "**************************************************************************************************************************************************" )
