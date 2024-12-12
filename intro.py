# example of variable
# let name- variable; JS var= varible
name ="Adrian" #string
age =38 #int
height = 1.86 #float
is_student =False #boolean
#type of varible can be change
#example
print(f"Name:{name}, age:{age}, height:{height}") #print(f"")concatenate
print("Type of age:", type(name))   #type()


#Example of an if statment
age=42 #it overwrite the previous variable
if age<13:
    print("Child")#indientation is imortant for python
elif age <20:
    print("Teenager")
else:
    print("Adult")


#forloop, for(let i=0; i<5; i++){let temp = current postion; }
for i in range(5):
    if i ==3:
        continue
    print(i)

# python list-->array[]
fruits=["Apple","Banana","Cherry"]
print(fruits[2])
fruits.append("Date")
print(fruits)
print(fruits[1:3])

# dictionary is {}
student = {
    "name":"Kit",
    "age":24,
    "course":["math", 107]
}
student["grade"]="A" #adding new element using dictrionary, direct assignment
student.update({"email":"arodriguez@sd.com"}) 
print(student)

#functions
def sayHello():
    print("Hello")

#call the functions
sayHello()

def sayGoodbye():
    print("Good Bye")

#concatenate, need convert num to str
print("Hello my name is "+ name +" and I have " + str(age) +" old") 

