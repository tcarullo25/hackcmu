class Graph:
    def createGraph(self, numNodes):
        adjList = {}
        for i in range(numNodes):
            adjList[i] = []
        return adjList

    def __init__(self, numNodes):
        self.adjList = self.createGraph(numNodes)
        self.numNodes = numNodes

    def addEdge(self, node1, node2, weight):
        if node1 not in self.adjList or node2 not in self.adjList:
            return False
        self.adjList[node1].append((node2, weight))
        self.adjList[node2].append((node1, weight))
        return True

    def addNode(self, node):
        if node in self.adjList: 
            return False
        
        self.adjList[node] = []
        return True
    
    def removeEdge(self, node1, node2):
        if node1 not in self.adjList or node2 not in self.adjList:
            return False
        
        self.adjList[node1] = [(n, w) for n, w in self.adjList[node1] if n != node2]
        self.adjList[node2] = [(n, w) for n, w in self.adjList[node2] if n != node1]

        return True 
    
    def getNeighbors(self, node):
        return [n for n, _ in self.graph[node]]

    
g = Graph(10)


