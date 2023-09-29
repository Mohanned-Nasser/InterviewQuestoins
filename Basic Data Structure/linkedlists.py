# start by defing a node class
class node :
    def __init__(self, val ):
        self.val = val 
        self.next = None
# now we will define a link list 
class SingleLinkedList:

    def __init__ (self):
        self.length = 0 
        self.head = None
        self.tail = None
    # the function show is to print out all the linked list 
    def show(self ):
        temp = self.head
        if (temp != None):
            while (temp != None):
                print(temp.val , end=" -> ")
                temp = temp.next

    #the pop function will return the last value in the linked list and then set the tail to the previous node
    def pop (self):
        temp = self.head
        newTail = temp
        #if the linked list is empty
        if (self.head == None):
            print("the list is empty")
            return
        #if the linked list has only one value
        elif (self.tail == self.head):
            retValue = self.head.val 
            self.head = None
            self.tail = None
            self.length -=1 
            return retValue
        #travel through the linked list and get the tail and the prevous node to the tail
        while (temp.next != None):
            newTail = temp
            temp = temp.next
        retValue = temp.val
        self.tail = newTail
        newTail.next = None
        self.length -=1
        return retValue

    # push function will add to the linked list at the end
    def push(self , newValue ):
        # create a new node with the new value 
        newNode = node(newValue)
        # if the link list is empty 
        if(self.length == 0 ):
            self.head = newNode
            self.tail = newNode
            self.length +=1 
        else :
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = None
            self.length += 1
    # shift functoin will return the head value and then assigning a new head (the next node)
    def shift(self):
        current = self.head
        if (self.head == None):
            print("the list is empty ")
            return 
        elif(self.head == self.tail):
            retValue = current.val 
            self.head = None
            self.tail = None
            self.length -=1 
        else:
            retValue = current.val 
            self.head = current.next 
            self.length -=1 
            return retValue
    # unshift function will add a new node to the start of the linked list
    def unshift(self , newVal):
        newNode = node(newVal)
        current = self.head 
        if (self.length == 0 ):
            self.haed = newNode 
            self.tail = newNode 
            self.length += 1 
        else :
            newNode.next = current
            self.head = newNode
            self.length +=1 
    # the get function will accept one number , and retrun the value that the index correspond
    def get (self , index):
        if i <0 : 
            print("the idnex can not be negative number ")
            return 
        elif (i > self.length -1 ):
            print("the index provided is out of range for the list")
            return
        else :
            current = self.head 
            for j in range ( index ):
                current = current.next 
            return current.val
    # the function set will accepts 2 variables , the variable  value will be the new value we want to add, and the next variable will be the position 
    # works like update 
    def set (self , index , value):
        if index <0 : 
            print("the idnex can not be negative number ")
            return 
        elif (index > self.length -1 ):
            print("the index provided is out of range for the list")
            return
        
        else : 
            current = self.head
            for i in range( index):
                current = current.next 
            current.val = value
    # insert is for inserting a new node  but not the start or the end of the list but in specific index 
    def insert (self , newValue , index ):
        if index <0 : 
            print("the idnex can not be negative number ")
            return 
        elif (index > self.length  ):
            print("the index provided is out of range for the list")
        elif(index == 0 ):
            self.unshift(newValue)
            return 
        elif (index == self.length):
            self.push(newValue)
        else :
            current = self.head
            previous = current 
            for i in range(index):
                previous = current
                current = current.next
            newNode = node(newValue)
            previous.next = newNode
            newNode.next = current
            self.length += 1 
    # remove function takes the index of the node that we want to delete 
    def remove(self , index):
        if index <0 : 
            print("the idnex can not be negative number ")
            return 
        elif (index > self.length -1 ):
            print("the index provided is out of range for the list")
            return
        elif (index == 0 ):
            self.shift()
        elif (index == self.length):
            self.pop()
        else:
            current = self.head
            previous = current
            for i in range(index):
                previous = current 
                current = current.next  
                self.length
            previous.next = current.next 
            return current.val
    #this function will reverse the linked list with out making a copy
    def reverse (self ):
        # we will need to keep track of 3 nodes here : one the current two the previous  three the next node 
        h = self.head 
        self.head = self.tail
        self.tail = h
        preivious = None
        n = None
        for i in range(self.length):
            n = h.next 
            h.next = preivious
            preivious = h
            h = n 


        
