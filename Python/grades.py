import random 

def grade(repeat):
    print "Grades and Scores"
    for i in range (0,repeat):
    
        your_score = random.randint(60,100)

        if (your_score < 69 and your_score > 60):
             print " score is :" ,your_score, " your grade is : D"
        elif (your_score < 79 and your_score > 70):
             print " score is :" ,your_score, " your grade is : C"
        elif (your_score < 89  and your_score > 80):
            print " score is :" ,your_score, " your grade is : B"
        elif (your_score < 100 and your_score > 90):
            print " score is :" ,your_score, " your grade is : A"
        else:
            print " you failed"
    print " End of Program"
grade(10)