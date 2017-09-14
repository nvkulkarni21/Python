import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
import re
import os
import warnings
from sentiment_pkg import sentiment
from negation_detector import negation_flip
import sys
import matplotlib.pyplot as plt

try:
    shell = sys.stdout.shell
except AttributeError:
    raise RuntimeError("you must run this program in IDLE")


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
                    #text=re.sub(" and ", ".", text ) #replace and with .
                    text=re.sub(" so, ", ".", text ) #replace and with .                    
                    text=re.sub(" but ", ".", text ) #replace and with .
                    text=re.sub(" hence ", ".", text ) #replace and with .
                    text=re.sub(" though ", ".", text ) #replace and with .
                    text=re.sub(" although ", ".", text ) #replace although with .
                    text=re.sub(" however ", ".", text ) #replace however with .
                    text=re.sub(" still ", ".", text ) #replace still with .
                    text=re.sub(" as well as ", ".", text ) #replace and with .
                    #text=re.sub("\\n", ".", text ) #replace and with .

                    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
                    
                    #print ( sentences )
                    for line in sentences:
                        
                        strippedString = line.strip()
                        if strippedString == "":
                            break
                        sentcnt = sentcnt + 1
                        print ("----------------------------------------------------------------------------")
                        print ( strippedString )
                        
                        #vaderres = vader( line )
                        sentires = sentiment(strippedString)
                        flip_flag=negation_flip( strippedString )
                        #print ("Flip flag is : " + str( flip_flag ))

                        #print (sentires + " original sentiment in this sentence")
                        
                        if ( ( flip_flag == 1 ) and ( sentires=="pos" ) ):
                            sentires="neg"
                            flip_flag = 0

                        if ( ( flip_flag == 1 ) and ( sentires=="neg" ) ):
                            sentires="pos"

                        if (sentires=="pos" ):
                            shell.write("Sentiment : " ,"KEYWORD")
                            shell.write("POSITIVE" ,"STRING")
                            print()
                            #print ( "Sentiment : POSITIVE" )
                        if (sentires=="neg" ):
                            shell.write("Sentiment : " ,"KEYWORD")
                            shell.write("NEGATIVE" ,"COMMENT")
                            #print ( "Sentiment : NEGATIVE" )
                            print()                     
                               
                        if sentires == "pos":
                            pos_cnt=pos_cnt+1
                        if sentires == "neg":
                            neg_cnt=neg_cnt+1


                        ss = (sid.polarity_scores(strippedString))    
                        for k in sorted(ss):
                            #print (k, ss[k])
                            if k == "compound":
                                comp_cntV=ss[k]+comp_cntV
                            if k == "neg":
                                neg_cntV=ss[k]+neg_cntV
                            if k == "pos":
                                pos_cntV=ss[k]+pos_cntV
                            if k == "neu":
                                neu_cntV=ss[k]+neu_cntV
                        
    print ()
    print ( "****************************************************************************" )
    shell.write ( "              OUTPUT FOR VADER STATISTICS                  ", "KEYWORD" )
    print()
    print ( "****************************************************************************" )
    print ()    
    shell.write ( "Avg NEGATIVE  : ", "DEFINITION" )
    shell.write (str( neg_cntV / sentcnt) , "COMMENT"   )
    print()
    shell.write ( "Avg POSITIVE  : ", "DEFINITION" )
    shell.write ( str( pos_cntV /sentcnt ), "STRING"   )
    print()
    shell.write ( "Avg NEUTRAL   : ", "DEFINITION" )
    shell.write ( str( neu_cntV / sentcnt ), "KEYWORD"  )
    print()
    print ("-----------------------------------------------------------")
    shell.write ( "Avg COMPOUND  : ", "DEFINITION" )
    shell.write (  str( comp_cntV /sentcnt ) , "KEYWORD"   )
    print()
    print()


    
    print ( "*******************************************************************************" )
    shell.write ( "OUTPUT FOR NAIVE BAYES STATISTICAL MACHINE LEARNING STATISTICAL ALGORITHM", "KEYWORD" )
    print()
    print ( "*******************************************************************************" )
    print ()
    shell.write ( "POSITIVE   :  " , "DEFINITION")
    shell.write ( str( pos_cnt ) , "STRING"  )
    print()
    shell.write ( "NEGATIVE   :  ", "DEFINITION" )
    shell.write ( str( neg_cnt ) , "COMMENT"  )
    print()
    #print ( "FINAL RATIO:  " + str( pos_cnt )  + ":" + str( neg_cnt ) )
    print ()
    print ( "*******************************************************************************" )

  # Pie Chart
    print (" PIE CHART FOR NAIVE BAYES ")
    labels = 'Positive', 'Negative' 
    sizes = [ pos_cnt, neg_cnt ]
    colors = ['yellowgreen', 'orange']
    
    
    plt.pie(sizes,  labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    
    plt.axis('equal')
    plt.title ("Training feedback Sentiment Summary")
    plt.show()
    
