import random
def head_tail(rpt):
    head = 0
    tail = 0
    for i in range(0,rpt):
        x = random.random()
        x = round(x)
        if x >0 :
            head = head +1
            print " Attempt # " , i , "It's a head..... got so far ", head  , "head(s) and ", tail ,  "tail(s)"
        else:
            tail = tail + 1
            print " Attempt # " , i , "It's a tail..... got so far ", head , "head(s) and ", tail ,  "tail(s)"
head_tail(5001)