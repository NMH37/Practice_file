
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']


def filter_type(obj):
    if isinstance(obj,int):
        if (obj >= 100):
            print obj,"is a big number"
        else:
            print obj," is a small number"   

    if isinstance(obj,str):
           #check length
        if (len(obj) > 50):
            print "it is a big string"
        else:
            print "it is a small string"
    if isinstance(obj,list):
        if (len(obj)>100):
            print "it is a big list"
        elif (len(obj)<10):
            print " it is a small list"


filter_type (sI)  
filter_type(mI)  
filter_type(bI)      
filter_type(spI) 
filter_type(sS)
filter_type(bS)
filter_type(eS)
filter_type(aL)
filter_type(mL)
filter_type(lL)
filter_type(eL)
filter_type(spL)
