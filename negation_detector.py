
def negation_flip(line):

        neg_array =(
        "doesn't" ,
        "isn't" ,
        "wasn't" ,
        "shouldn't" ,
        "wouldn't" ,
        "couldn't" ,
        "won't" ,
        "can't" ,
        "don't" ,
        "doesnt" ,
        "isnt" ,
        "wasnt" ,
        "shouldnt" ,
        "wouldnt" ,
        "Couldnt" ,
        "wont" ,
        "cant" ,
        "dont" ,
        "hardly" ,
        "scarcely" ,
        "barely" ,
        "no " ,
        "not " ,
        "none" ,
        "noone" ,
        "nobody" ,
        "nothing" ,
        "neither" ,
        "nowhere" ,
        "never" ,
        "in vain"
        )

        

        s =line
        

        mystring=s.lower()

        
        var=0

        for neg in neg_array:
            if mystring.find(neg) == -1:
                var = var + 0
            else:
                var = var + 1

        #print var 
        flip_flag = var % 2

        return flip_flag




#print negation_flip("There is hardly any situation where trainer performed well.")
#print negation_flip("Trainer is good for nothing")

