marks=[]
while True:
    mark=int(input("enter your marks: " ))
    if mark<0:
        print("OOPS,invalid marks")
        mark=input("enter your marks: " )
    marks.append(mark)
    if len(marks)==5:
        break
average=sum(marks)/len(marks)
if average>=80:
    grade="A"
elif average>=69:
    grade="B"
elif average>=59:
    grade="C"
elif average>=49:
    grade="D"
else:
    grade="You Failed"
print("Your Grade: ",grade)
