class maxHeap:
    def __init__(self ):
        self.values = []
    def insert(self , val) :
        self.values.append(val)                                                                                                # Start with appending the value to the list
        self.bubbleUp()
    def bubbleUp(self ):
        idx = len(self.values) -1                                                                                              # Get the chlid index, it is the latest added value
        element = self.values[idx]                                                          
        while(idx > 0 ):
            parentIdx = int((idx - 1 ) / 2 )                                                                                   # Get the parent index and make sure its inside the loop to update it 
            parent = self.values[parentIdx]                                                                                    
            if(element <= parent ):                                                                                            # Break point for the loop, if the parent is larger then the heap is sorted and good to go 
                break
            self.values[parentIdx] = element                                                                                   # Here we swip the parent element and the child
            self.values[idx] = parent
            idx = parentIdx                                                                                                    # Then we update the child indx to the parent one (cuz we already swiped)

    def extract(self):
        if(len(self.values) ==  0) :
            print("The Heap is empty")
            return
        retValue = self.values[0]
        length = len(self.values) - 1 
        end = self.values.pop(length)
        if(len(self.values) > 0) :
            self.values[0] = end
            self.sinkDown()
        return retValue

    def sinkDown(self ):
        idx = 0 
        length = len(self.values)
        element = self.values[0]
        while(True):
            leftChildIdx = 2 * idx + 1 
            righChildIdx = 2 * idx + 2 
            swap = None 
            leftChild = None 
            rightChild = None
            if(leftChildIdx < length):
                leftChild = self.values[leftChildIdx]
                if (leftChild > element) :
                    swap = leftChildIdx
            if(righChildIdx < length ):
                rightChild = self.values[righChildIdx]
                if ((swap == None and rightChild > element ) or
                    (swap != None and rightChild > leftChild)):
                    swap = righChildIdx
            if(swap == None ):
                break 
            self.values[idx] =  self.values[swap]
            self.values[swap] = element
            idx = swap