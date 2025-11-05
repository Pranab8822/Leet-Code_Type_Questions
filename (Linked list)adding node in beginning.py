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


    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = linked_list()
ll.display()            # show initial list
ll.add_at_beginning()   # add new node
ll.display()    