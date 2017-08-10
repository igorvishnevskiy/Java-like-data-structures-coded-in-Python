



class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
        self.edges = []

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def addEdge(self, edge):
        self.edges.append(edge)

    def getEdges(self):
        return self.edges

    def getSelf(self):
        return self




class Graph():

    def __init__(self):
        self.root = None


    def addNode(self, value):
        if self.root == None:
            print "Im insodeeee"
            self.root = Node(value)
        else:
            self.__findLastNode(self.root, value)


    def __findLastNode(self, node, value):
        if node.getNext() != None:
            self.__findLastNode(node.getNext(), value)
        else:
            print node.getData()
            return node.setNext(Node(value))
    def addEdge(self, valueOfStartNode, valueOfEndNode):
        startNode = self.__findNode(self.root, valueOfStartNode)
        endNode = self.__findNode(self.root, valueOfEndNode)
        self.foundNode = None
        if startNode != Node and endNode != None:
            startNode.addEdge(endNode)
            return True
        else:
            return False


    def __findNode(self, node, value):
        self.foundNode = None
        if node.getNext() != None:
            if str(node.getData()).lower() == str(value).lower():
                self.foundNode = node
            else:
                self.parentNode = node
                self.__findNode(node.getNext(), value)
        return self.foundNode


    def printConnectionsOfALlNodes(self):
        if self.root == None:
            print "Nothing to print, first add Root Node"
        else:
            self.__itterateNodes(self.root)


    def __itterateNodes(self, node):
        if node.getNext() != None:
            print str(node.getData()) + str(node.getEdges())
            self.__itterateNodes(node.getNext())


    def isReachable(self, valueOfStartNode, valueOfEndNode):
        self.numOfEdges = 0
        self.isReachableBool = False
        self.lookedAt = []
        startNode = self.__findNode(self.root, valueOfStartNode)
        endNode = self.__findNode(self.root, valueOfEndNode)
        if startNode != None:
            print "\nstartNode: "+startNode.getData()
            print "endNode: "+endNode.getData()
            self.__findTheEdgeConnection(startNode, endNode)
            print "isReachable: "+str(self.isReachableBool)
            if self.isReachableBool is True:
                print "Took "+str(self.numOfEdges) + " edge(s) to reach endNode"
            return self.isReachableBool
        else:
            return self.isReachableBool


    def __findTheEdgeConnection(self, startNode, endNode):
        listOfEdges = startNode.getEdges()
        if endNode in startNode.getEdges():
            self.isReachableBool = True
        else:
            for item in listOfEdges:
                subListOfEdges = item.getEdges()
                if len(item.getEdges()) > 0:
                    for subItem in subListOfEdges:
                            self.__findTheEdgeConnection(subItem, endNode)
        self.numOfEdges += 1


    def delete(self, value):
        nodeObj = self.__findNode(self.root, value)
        print nodeObj.getData()
        print self.parentNode.getData()
        self.parentNode.setNext(nodeObj.getNext())


    def __itterateAndDeleteEdges(self, currentNode, nodeToDelete):
        if currentNode.getNext() != None:
            if nodeToDelete in currentNode.getEdges():
                currentNode.getEdges().remove(nodeToDelete)
            self.__itterateAndDeleteEdges(currentNode.getNext(), nodeToDelete)
