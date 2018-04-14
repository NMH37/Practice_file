# inputcopy
#word_list = ['hello','world','my','name','is','Anna']
#char = 'o'
# output
#new_list = ['hello','world']

def find_char(list1,char1):
    new_list = []
    for index in range(0,len(list1)):
        if (list1[index].find(char1) >= 0):   
            new_list.append(list1[index])
    print new_list    
word_list = ['hello','world','my','look','name','is','Anna']
char = 'o'

find_char(word_list,char)