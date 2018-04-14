def compare_list(list1,list2):
    if list1 == list2:
        print " the list is same"
    else:
        print " list is different"
        
        
list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

compare_list(list_one,list_two)

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
compare_list(list_one,list_two)


list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
compare_list(list_one,list_two)



list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
compare_list(list_one,list_two)