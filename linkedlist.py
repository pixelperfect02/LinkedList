# Singly Linked List By Archie Verma
# Adding before-between-after, Removing before-between-after and Traversal of a Linked List

class Node:

    # Step 1: Just Create invidual nodes
    # init is a special method class contructoor called when new instance of a class is created
    # Each node contains data and address, and self is itself which has data and some address
    def __init__(self, data): 
        # data written here
        self.data = data
        # ref/address written here (no links yet at this step thats why it is set to none)
        self.ref = None

# Can print a node and see -> will give address of node1
# (note node 1 ref is still empty coz it carries the address of the next node but since no links yet its still none)
# node1 = Node(10)
# print(node1)


# Now we link these nodes can created LinkedList class to do that 
class LinkedList:
    # Note only taking self parameter here
    def __init__(self):
        # We wrote head as none, head represents the first element and if its none that means linkedlist is empty
        # Can add, remove elements later but initially the linkedlist will be empty
        # Note for add and remove there are different scenarios like add first, last or in between the list and vice versa
        # We are doing traversal atm -> going through each node of a linked list 
        # To do traversal we also have steps and first is to check if linkedlist not empty or empty,
        # If empty print a message
        # If not empty go to the next node and access data, then continue till last node
        self.head = None 
    
    # To print the linked list
    def print_LinkedList(self):
        # Check if empty, print empty
        if self.head is None:
            print("Empty Linked List")
        # If not empty we need to traverse it
        else:
            # self.head is the address of the first node here 
            n = self.head
            # added while loop to check before or until n or 'self.head' which is the node address becomes none or null 
            print("Linked List is not empty: ", end=" ")

            while n is not None: 
             # print the data of thee current address node
             print(n.data, "-->", end=" ")
             # set the n as current node's reference(that is the address of the next node then do the whole thing again untill node address becomes null usually till the last node)
             n = n.ref

    # Inserting or adding we need data as parameter
    def add_begin(self, data) : 
        # Creating a node (we call it new_node) to insert which is an object from the Node class
        new_node = Node(data) # This creates a new node fron Node class but the reference is still none here coz of the node class
        # Now we need to change the reference from null to something because we need to insert elements
        # Making the new node reference the head here or the first element 
        new_node.ref = self.head
        # going to the next ref node and making it head 
        self.head = new_node
    
    def add_end(self, data) :
        # Creating a node (we call it new_node) to insert which is an object from the Node class
        new_node = Node(data)
        # First we check if the linked list is empty or not (why here for end?)
        if self.head is None:
             self.head = new_node
        else: 
             n = self.head
             # Helps us to get to the last node with reference null
             while n.ref is not None:
                    n = n.ref
             # This helps change the reference of the last node from null to the ref of the element we want to add
             n.ref = new_node
           
        
LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_end(50)
LL1.add_end(100)
LL1.add_begin(20)
LL1.print_LinkedList()
