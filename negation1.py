
def absolute_value(line):

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
        "in vein" ,
        "for nothing" 
        )

        

        s =line
        

        mystring=s.lower()

        
        var=0

        for neg in neg_array:
            if mystring.find(neg) == -1:
                var = var + 0
            else:
                var = var + 1
                print neg

        #print var 
        flip_flag = var % 2

        return flip_flag




print absolute_value("There is hardly any situation where trainer performed well.")

