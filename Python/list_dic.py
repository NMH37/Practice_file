name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "rabbit","llamas"]

def make_dict(list1, list2):
  new_dict = {}
  new_dict = zip(list1,list2)
  return new_dict

arr = make_dict(name,favorite_animal)

#print arr

#i dont understand how it works !
def making_dictionaires(list1, list2):
    the_dict = {}
    for i in range(0, len(list1)):
        the_dict[list1[i]] = list2[i]
    return the_dict
new_dic = making_dictionaires(name,favorite_animal)
print(new_dic)
