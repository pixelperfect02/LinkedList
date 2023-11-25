# Singly Linked List By Archie Verma

# Adding before-between-after, Removing before-between-after and Traversal of a Linked List
#                  |                              |
#              between could be after node of before node 
#      in betweeen can be inserted either after node of before node

# We write separate code for after and before node:
# After node: This one can't be the first node coz inserted 'after' either last node or in the rest positions see steps below
# Before node: This one can become the first node coz inserted before  or can be in the rest postions 
class Node:

    # Step 1: Just Create invidual nodes
    # init is a special method class contructor called when new instance of a class is created
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


    ###########################################################################ADDING##########################################################################################
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


    # in betweeen can be inserted either after node of before node
    # After node code: 
    def add_after(self, data, x) : # x here is the node next to which we need to insert
        # Find x
         n = self.head # we take the first element as n 
         # if this is true then we found x so break
         while n is not None :
            if x == n.data : # comparing the data field of each node with x to find x
               break
            # else move to the next element and check again when using break don't have to write break
            n = n.ref # moving to next node to keep checking if its x
         if n is None :
                print("Node not present")
         else :
                new_node = Node(data) # initially reference is None for this new node, we need to point to to a node to insert it after a node
                new_node.ref = n.ref # changed the reference of new node to new node
                n.ref = new_node # now the previous n needs to point to the reference of new node
    # Before node
    def add_before(self, data, x) :
    # Checking if linked list not empty
      if self.head is None:
            print ("Linked List empty")
            return
    # Step 1: For before the first node (newnode becomes the first node)
    # checking if inserting element before the first element
      if self.head.data == x: # x here is the first node we need to insert new node before x
      # get code from above for add begin for inserting in the beginning
       new_node = Node(data)  
       new_node.ref = self.head
       self.head = new_node
       return
    # Step 2: Before the rest nodes: 
    # a)find previous node  of a given node to do it we need to:
    #   1. identify- to do this we will have to check that the next node data is equal to x (the given node) 
    #   2. go to the previous node - take first node as n and check if the data is equal to x till you get equal keep checking the whole list by moving using n = n.ref
    # b)new node after that previous node same as add_end to insert the node
      n = self.head
      while n.ref is not None :
       if n.ref.data == x:
            break
       n = n.ref

      if n.ref is None : 
        print("Node not found")
      else :
       # same as add_end to insert the node
       new_node = Node(data)
       new_node.ref = n.ref 
       n.ref = new_node
 ###########################################################################ADDING##########################################################################################

 ###########################################################################REMOVING########################################################################################
    # Delete a node from the beginning of a linked list 
    def delete_begin(self):
        # Check if the linkedlist is empty
        if self.head is None :
            print("LL is empty, no node to delete")
        else:
        # Else we need to point head to the seccond node, that is we need to store the reference of the second node in the head
         self.head = self.head.ref
    
    # Delete a node from the end of a linked list
    def delete_end(self):
        # Check if the linkedlist is empty
        if self.head is None :
            print("LL is empty, no node to delete")
        
        # We will get error in case linked list only contains 1 element and we delete it coz the ref will point to none therefore n.ref.ref won't work, so we add elif condition:
        elif self.head.ref is None : 
            self.head = None

        else:
        # Else we need to go to the 2nd last node and change its ref to none or null
        # To go to the 2nd last node we still need to start from the start of the linked list n is head to do that and we use while loop like we have been doing before
        # We can identify the 2nd last node by going to the last none whose ref is null and then go to the node next to it matching the last second nodes reference with last 
        # node's address=> x or n now coz loop is last second node and x.ref is address of next node within x and then x.ref.ref is reference of the next node can be last node so null here
            n = self.head
            while n.ref.ref is not None :
                n = n.ref
            n.ref = None

    # Delete a node from the middle or in between or any position of a linked list
    # User will give the value of the node to delete it  
    # In between can be deleted either after node of before node:  
    # Two conditions here:
    # 1. Check if its the first node that has to be deleted (before)
    # 2. Check if its other node or last node that has to be deleted (after)
    def delete_by_value(self,x):
        # Check if the linkedlist is empty
        if self.head is None :
           print("LL is empty, no node to delete")
           return
        
        # If linkedlist not empty then check if the user given node(x) is first node or not 
        # If it is true then the head needs to point at the second node
        if x==self.head.data :
            self.head = self.head.ref
            return
        
        # If it is not the first node, we have to go to the previous node of the given node and 
        # We need to change its reference to the next node
        # This is how we check that this particular node is the previous node(we go through the whole linked list), n is nothing but the first node
        n = self.head
        while n.ref is not None :
           if n.ref.data == x : 
              break 
           n = n.ref
           
        if n.ref is None :
            print("Node not present")
        else : 
            n.ref = n.ref.ref
 ###########################################################################REMOVING########################################################################################
 
LL1 = LinkedList()
LL1.add_begin(44)
LL1.delete_by_value(44)
LL1.add_begin(10)
LL1.delete_begin()
LL1.add_begin(20)
LL1.add_end(50)
LL1.delete_end()
LL1.add_end(100)
LL1.add_after(200,100) # data is 200 needs to be added after 100
# LL1.add_after(200,500) # case for 500 not present add 200 after 500, should give node not present
LL1.add_before(60, 20)
LL1.print_LinkedList()


# elif test
# LL1 = LinkedList()
# LL1.add_begin(10)
# LL1.delete_end()
# LL1.print_LinkedList()



    
