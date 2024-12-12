def print_menu():
    print("====================================")
    print("1) sum")
    print("2) substract")
    print("3) multiply")
    print("4) divide")


print_menu()
opt =input("Select the option")

num1=float(input("Please provide a number"))
num2=float(input("Please provide a second number"))

#proceed witht the logic to calculate the total
if opt == "1":
    total=num1+num2
    print("the total is:" +str(total))
elif opt== "2":
    total=num1-num2
    print("the total is:" +str(total))
elif opt== "3":
    total=num1*num2
    print("the total is:" +str(total))
elif opt== "4":
    if num2==0:
        print("you are trying to divide by zero")
    else:
        total=num1/num2
        print("the total is:" +str(total))


