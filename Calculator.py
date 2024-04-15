#calculator
def calculator():
    
    #Make the operations functions
    #The Add Function
    def Add(x,y):
        return x+y
    #The Subtract Function
    def Subtract(x,y):
        return x-y
    #The Multiply Function
    def Multiply(x,y):
        return x*y
    #The Divide Function
    def Divide(x,y):
        return x/y
    def Sqr(x):
        for i in range(0,x):
            if i*i==x:
                return i
            else:
                continue
    def The_Cube_Root(x):
        for i in range(0,x):
            if i*i*i==x:
                return i
            else:
                continue
            

    #print a welcome message to the user
    print("Welcome to the Calculator!")
    #Print the operations to the user
    print("Please Sellect the operation: ")
    print("1-Add")
    print("2-Subtract")
    print("3-Multiply")
    print("4-Divide")
    print("5-Sqr")
    print("6-The Cube Root")

    while True:
        #Take the operation input from the user
        Operation=int(input("Please choose number from(1,2,3,4,5,6):"))
        if Operation in [1,2,3,4]:
            num1 =float(input("Enter The First Number: "))
            num2 =float(input("Enter The Second Number: "))
            #Call the function based on the users choice
            if Operation==1:
                print("The Answer is: " , Add(num1,num2))
            elif Operation==2:
                print("The Answer is: " , Subtract(num1,num2))
            elif Operation==3: 
                print("The Answe is: " , Multiply(num1,num2))
            elif Operation==4:
                print("The Answer is: ", Divide(num1,num2))
            else:
                print("Invaild input,Please try again!")
                continue
        elif Operation==5:
            num=int(input("Enter The Number: "))
            #Check if the number is positive otherwise it
            if num>0:
                print("The Answer is: ",Sqr(num))
            elif num<0:
                print("Invaild input,Please Enter a positive number!")
                continue
            else:
                print("Invaild input,please enter numbers only!")
                continue
        elif Operation==6:
            num=int(input("Enter The Number: "))
            print("The Answer is: ",The_Cube_Root(num))

            #Ask the user if he want to does another calculation?
        next_calculation=input("Do you want to do another calculation?(Yes or No): ")
        #Continue if The answer is yes
        
        if next_calculation=="yes" :
            continue
        elif next_calculation=="no":
            print("Ok , Good Bye")
            break

        #If the operation input isn't in (1:4) try again
        else:
            print("Invaild input,Please choose from 1:6")
            continue

#Call the calculator function
calculator()

