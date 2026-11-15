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

