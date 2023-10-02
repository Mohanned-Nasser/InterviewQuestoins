class UndirectedGraph:
    def __init__(self):
        self.adjacencyList = {}
    def addVertex(self , Name):
        if Name in self.adjacencyList:
            print("This node is already in the graph")
            return
        self.adjacencyList[Name] = []
    def addEdge(self ,vertex1 , vertex2 ):
        if vertex1 in self.adjacencyList and vertex2 in self.adjacencyList: 
            self.adjacencyList[vertex1].append(vertex2)
            self.adjacencyList[vertex2].append(vertex1)
        else :
            print("vertex not found")
    
    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.adjacencyList[vertex2] and vertex2 in self.adjacencyList[vertex1]:
            self.adjacencyList[vertex1].remove(vertex2)
            self.adjacencyList[vertex2].remove(vertex1)
        else:
            print(vertex1)
            print(vertex2)
            print("could not find the edge ")
    
    def removeVertex (self, vertex):
        if vertex in self.adjacencyList:
            while(len(self.adjacencyList[vertex])):
                remo = self.adjacencyList[vertex][-1]
                print(remo)
                self.removeEdge(vertex , remo)
            del self.adjacencyList[vertex]
            
        else :
            print("the node could not be found ")

