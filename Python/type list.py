
l = ['magical unicorns',19,'hello',98.98,'world']
lI = [2,3,1,7,4,12]
lS= ['magical','unicorns']

def list_type(obj):
    final_sum = 0
    new_str = ""
    
    for element in obj:
        if isinstance(element,int) or isinstance(element,float):
            final_sum = final_sum + element
            
        elif isinstance(element,str):
            new_str = new_str +" "  + element

    if new_str  and final_sum:
        print " you entered a mixed list"
        print " Final sum is", final_sum
        print " The string is ", new_str 
        
        
    elif new_str :
        print " all string" ,new_str
    else:
        print " all number" , final_sum

           
            
            
list_type(l)
#list_type(lI)
#list_type(lS)

