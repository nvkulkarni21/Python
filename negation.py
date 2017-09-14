

def negate_sequence(text):

    delims = "?.,!:;"
    words = text.split()

    for word in words:

        stripped = word.strip(delims).lower()

        if negation:
            print "neg word detected"   


        if any(neg in word for neg in ["not", "n't", "no"]):
            negation = not negation

        if any(c in word for c in delims):
            negation = False





print( negate_sequence( "This is not good" ) )
