class node():
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list():
    def __init__(self):
        node1=node(2)
        node2=node(33)
        node3=node(90)

        node1.next=node2
        node2.next=node3

        self.head=node1
                

    def add_at_beginning(self):
        num = int(input("Enter the value you want to add: "))
        new_node = node(num)
        new_node.next = self.head
        self.head = new_node



    def add_at_end(self):
        num = int(input("Enter the value you want to add: "))
        new_node = node(num)
    
    # If the list is empty
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next  # move to next node until last
        current.next = new_node    # now current is the last node


    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

choice=int(input("Enter your choice 1.\n Display Linkedlist \n2.Add node at the abeginning \n3.Add node at the end\n:"))
ll = linked_list()
if choice==1:
    ll.display()
if choice==2:                # show initial list
    ll.add_at_beginning()
    ll.display()   
if choice==3:
    ll.add_at_end()  
    ll.display()     