class node :
    def __init__(self, val ):
        self.value = val 
        self.next = None

class Queue () :
    def __init__ ( self ):
        self.length = 0 
        self.head = None 
        self.tail = None  
    def enqueue(self , val ):                                                      # the enqueue function on a queue will always add to the head 
        newNode = node(val)                                                        # notice that when we add to queue we will add it tail 
        if (self.length == 0 ): 
            self.head = newNode
            self.tail = newNode 
            self.length += 1
            return 
        else : 
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1 
            return
    def show(self) : 
        current = self.head 
        while (current != None):
            print(current.value ,end="-> ")
            current = current.next 
        print()
    def dequeue (self) : 
        if (self.length == 0 ) :
            print("The queue is empty ")
            return 
        retValue = self.head.value
        if (self.head == self.tail):
            self.tail = None 
        
        self.head = self.head.next
        self.length  -= 1 
        return retValue

