





def write_dic(name,age,country,lang):
    person_info = {}
    person_info["name"] = name
    person_info["age"] = age
    person_info["country"] = country
    person_info["lang"] = lang
    return person_info   
person = {}
person = write_dic("hana",12,"USA","JS")


def read_dic(person_info):
    print "My name is ",person_info["name"]
    print "I am ",person_info["age"],"year old"
    print"I was born in",person_info["country"]
    print"I like coding using",person_info["lang"]

read_dic(person)    
# solution from platform
def print_dictionary_values(dic):
    for some_key, some_value in dic.iteritems():
        print "My" + " " + some_key + " " + "is" + " " + str(some_value)
        
        # alternate method:
        # concatenating variables to strings commonly done with the .format() method (can be used on any string, or variable that
            # contains a string
        
        #print "My {} is {}".format(some_key, some_value)
