class Graph:

    def createGraph(self, numNodes):
        adjList = {}
        for i in range(numNodes):
            adjList[i] = []
        return adjList

    def __init__(self, numNodes):
        self.adjList = self.createGraph(numNodes)
        self.numNodes = numNodes

    def addNode(self, node1, node2, weight):
        if node1 not in self.adjList or node2 not in self.adjList:
            return False
        self.adjList[node1].append((node2, weight))
        self.adjList[node2].append((node1, weight))
        return True

    def removeNode(self, node1, node2):
        if node1 not in self.adjList or node2 not in self.adjList:
            return False
        for i in range(len(self.adjList[node1])):
            if node2 == self.adjList[node1][i]:
                self.adjList[node1][i].remove()

        for i in range(len(self.adjList[node2])):
            if node1 == self.adjList[node2][i]:
                self.adjList[node2][i].remove()

        return True 
    
g = Graph(10)
g.addNode(2,3)

