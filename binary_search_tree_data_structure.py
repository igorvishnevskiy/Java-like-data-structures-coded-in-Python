



class Node():
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = None

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getData(self):
        return self.data

    def getParent(self):
        return self.parent

    def setLeftChild(self, newLeftChild):
        self.leftChild = newLeftChild

    def setRightChild(self, newRightChild):
        self.rightChild = newRightChild

    def setData(self, data):
        self.data = data

    def setParent(self, parent):
        self.parent = parent


class Tree():
    def __init__(self):
        self.root = None
        self.__containsBool = False
        self.__findNodeObj = None
        self.__listObj = []


    def add(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.__traverseAndAdd(self.root, Node(data))


    def __traverseAndAdd(self, node, nodeToAdd):
        if node.getData() >= nodeToAdd.getData():
            if node.getLeftChild() == None:
                node.setLeftChild(nodeToAdd)
                node.getLeftChild().setParent(node)
            else:
                self.__traverseAndAdd(node.getLeftChild(), nodeToAdd)

        if node.getData() < nodeToAdd.getData():
            if node.getRightChild() == None:
                node.setRightChild(nodeToAdd)
                node.getRightChild().setParent(node)
            else:
                self.__traverseAndAdd(node.getRightChild(), nodeToAdd)


    def remove(self, value):
        if self.root != None:
            node = self.findNode(value)
        else:
            return None
        parentNode = node.getParent()
        if node.getLeftChild() != None and node.getRightChild() != None:
            if node.getData() < parentNode.getData():
                parentNode.setLeftChild(node.getRightChild())
                self.__traverseAndAdd(self.root, node.getLeftChild())
            else:
                parentNode.setRightChild(node.getLeftChild())
                self.__traverseAndAdd(self.root, node.getRightChild())
        elif node.getLeftChild() != None and node.getRightChild() == None:
            if node.getData() < parentNode.getData():
                parentNode.setLeftChild(node.getLeftChild())
            else:
                parentNode.setRightChild(node.getLeftChild())
        elif node.getLeftChild() == None and node.getRightChild() != None:
            if node.getData() < parentNode.getData():
                parentNode.setLeftChild(node.getRightChild())
            else:
                parentNode.setRightChild(node.getRightChild())
        elif node.getLeftChild() == None and node.getRightChild() == None:
            if node.getData() < parentNode.getData():
                parentNode.setLeftChild(None)
            else:
                parentNode.setRightChild(None)


    def findNode(self, value):
        if self.root != None:
            self.__getNodeTraversal(self.root, value)
        else:
            return None
        returnNodeObj = self.__findNodeObj
        self.__findNodeObj = None
        print returnNodeObj.getData()
        return returnNodeObj


    def __getNodeTraversal(self, node, value):
        if node != None:
            if node.getData() == value:
                self.__findNodeObj = node
            self.__getNodeTraversal(node.getLeftChild(), value)
            self.__getNodeTraversal(node.getRightChild(), value)


    def contains(self, value):
        if self.root != None:
            self.__containsTraversal(self.root, value)
        returnBool = self.containsBool
        self.__containsBool = False
        print returnBool
        return returnBool


    def __containsTraversal(self, node, value):
        if node != None:
            if node.getData() == value:
                self.containsBool = True
            self.__containsTraversal(node.getLeftChild(), value)
            self.__containsTraversal(node.getRightChild(), value)


    def traverse(self, traversalType):
        if self.root != None:
            if traversalType.replace(" ","").lower() == "preorder":
                self.__preOrderTraverse(self.root)
            elif traversalType.replace(" ","").lower() == "inorder":
                self.__inOrderTraverse(self.root)
            elif traversalType.replace(" ","").lower() == "postorder":
                self.__postOrderTraverse(self.root)


    def __preOrderTraverse(self, node):
        if node != None:
            print node.getData()
            self.__preOrderTraverse(node.getLeftChild())
            self.__preOrderTraverse(node.getRightChild())


    def __inOrderTraverse(self, node):
        if node != None:
            self.__inOrderTraverse(node.getLeftChild())
            print node.getData()
            self.__inOrderTraverse(node.getRightChild())


    def __postOrderTraverse(self, node):
        if node != None:
            self.__postOrderTraverse(node.getLeftChild())
            self.__postOrderTraverse(node.getRightChild())
            print node.getData()


    def toList(self):
        if self.root != None:
            self.__toListTraversal(self.root)
        returnObj = self.__listObj
        self.__listObj = []
        return returnObj


    def __toListTraversal(self, node):
        if node != None:
            self.__toListTraversal(node.getLeftChild())
            self.__listObj.append(node.getData())
            self.__toListTraversal(node.getRightChild())


    def listToTree(self, list):
        for item in list:
            self.add(item)
