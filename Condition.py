#if (Condition)
age=25
if(age>=18):
    print("can vote")

#elif (Condition)
light="red"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")


#else(Condition)
age=15
if(age>=18):
    print("can vote")

else:
    print("Can't Vote")


#Conditional Statements

marks= int(input("Enter student marks: "))
if(marks>=90):
    Grade="A"

elif( marks>=80 and marks<90):
    Grade="B"

elif( marks>=70 and marks<80):
    Grade="C"

else:
    Grade="D"

print("Grade of the student->",Grade)


