def add():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    add=a+b
    print(add)

def sub():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    sub=a-b
    print(sub)

def mul():
    a=int(input("Enter first number: ")) 
    b=int(input("Enter second number: "))
    mul=a*b
    print(mul)

def div():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    div=a/b
    print(div)     

def calculation():
    choice=int(input("1.Sum\n 2.Substraction\n 3.multiply\n 4.Division\n"))
    if choice==1:
        add()
    elif choice==2:    
        sub()
    elif choice==3:    
        mul()
    elif choice==4:
        div()
    elif choice>=5:
        print("Invalid choice")       

#logic for repeating calculation again and again
if (True):
    calculation()
    choice2=(input("Do you want to calculate again Y/N: "))
    if choice2.upper()=="Y":
        calculation()
    else:
        exit