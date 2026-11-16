marks =[94.5,85.5,76.5,65.5,55.5,45.5,35.5,25.5,15.5,5.5]

print("Marks:", marks)

print(type(marks))

print(marks[0])

print(marks[1])

print(marks[2:7])

print("Length of marks list:", len(marks))

marks.append(2.5)
print("Maks After append:", marks)

marks.sort()
print("Maks After sort:",marks)

marks.sort(reverse=True)
print("Maks After sort (reverse):",marks)

listOfAnything=["Hello", 1, 2.5]

print("List of anything:", listOfAnything)

listOfAnything[0]="World"

print("List of anything:", listOfAnything)  

listOfAnything.reverse()
print("List of anything after reverse:", listOfAnything)

listOfAnything.insert(1, "Python")
print("List of anything after insert:", listOfAnything)