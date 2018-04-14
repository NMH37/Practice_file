def making_tupes(the_dict):
    the_list = []
    
    for key,value in the_dict.iteritems():
        the_list.append((key,value))
    return the_list

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

arr = making_tupes(my_dict)  
print arr