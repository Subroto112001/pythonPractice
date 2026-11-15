str = "i am learnign Python programming."


capitalizestr = str.capitalize()

print(str)


print(str.endswith("ing."))

print(capitalizestr)

# comitted

wordReplacer = str.replace("Python", "JavaScript")

print(wordReplacer)

wordFinder = str.find("Python")

print(wordFinder)

stringCounter= str.count("a")

print(stringCounter)

fristname = "John"

print(len(fristname))
print(fristname.find("J"))

name=input("Enter your name: ")

print("Length of you nameis:", len(name))
print("Length of you nameis:", name.count("S"))

Age = int(input("Enter your age: "))

if(Age>=18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

Light = input("Enter the light color you have seen: ")

if(Light== "red"):
    print("You should stop.")
elif(Light=="yellow"):
    print("You should wait.")
elif(Light=="green"):
    print("You should go.")



# Grading system of a student

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks!")

elif marks >= 90:
    print("Your grade is A+.")

elif marks >= 80:
    print("Your grade is A.")

elif marks >= 70:
    print("Your grade is B.")

elif marks >= 60:
    print("Your grade is C.")

elif marks >= 50:
    print("Your grade is D.")

elif marks >= 40:
    print("Your grade is F.")

else:
    print("Your grade is Out of world.")