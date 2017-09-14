import re
import os


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
                    print ( sentences )
                    for line in sentences:
                        print ( line )
                        
                        
                    

        
        
     
    


"""

import os
text = ' '.join(file_to_open.readlines())
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text) 


"""
