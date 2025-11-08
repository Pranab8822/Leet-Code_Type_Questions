class stack():
    def __init__(self):
        self.stack=[2,3,45,8]

    #function to push item in stack 
    def push(self):
        item=input("Enter here: ")
        self.stack.append(item)
        print(f"{item} pushed into the stack.")
        self.display()

    #function for poping item 
    def pop(self):
        if self.is_empty():
            print("Unable to pop — stack is empty")
        else:
            removed_item = self.stack.pop()
            print(f"Popped item: {removed_item}")
        
    #function for displaying items
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements (top to bottom):", self.stack[::-1])        


    def is_empty(self):
        return len(self.stack) == 0    
    
choice=int(input("Enter your choice:  "))
s=stack()
if choice==1:
    s.push()
if choice==2:    
    s.pop()
if choice==3:
    s.display
