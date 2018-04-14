
def even_odd(low,high):

    for i in range(low,high+1):
        if (i % 2 == 0):
            print i ," is even number"
        else:
            print i ," is odd number"

even_odd(10,20)            

def multiply_by(element,num):

    for i in range(0,len(element)):
       element[i] = element[i] * num
    return element   
arr = [2,4,6,0,9]
new_arr = multiply_by(arr,5)
print new_arr

def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply_by([2,4,5],3))
print x