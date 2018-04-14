
def print_star(arr):
    for i in range (0,len(arr)):
        j= arr[i]
        if isinstance(j,int):
            print "*" * j
        else:
            letter = j[0].lower()
            print letter *len(arr[i]) # rpelace "a" with the function

arr=[2,4,"micheal",7,9,"laura",4,5,3]
print_star(arr)