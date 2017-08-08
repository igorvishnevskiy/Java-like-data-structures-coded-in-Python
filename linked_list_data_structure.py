__author__ = 'ivishnevskiy'


class Node():

    def __init__(self, data, next):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def setData(self, value):
        self.data = value

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext



class SinglyLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        self.currentSize = 0


    def add(self, value):
        if(self.isEmpty()):
            self.head = Node(value, None)
            self.tail = self.head
        else:
            self.tail.setNext(Node(value, None))
            self.tail = self.tail.getNext()
        self.currentSize += 1
        return True


    def isEmpty(self):
        return self.size() == 0


    def size(self):
        return self.currentSize


    def get(self, index):
        if index < 0 or index >= self.currentSize:
            raise IndexError

        if index < self.currentSize - 1:
            current = self.head
            for i in xrange(index):
                current = current.getNext()
            return current.getData()
        return self.tail.getData()


    def clear(self):
        self.head = None
        self.tail = None
        self.currentSize = 0


    def removeByIndex(self, index):
        if index < 0 or index >= self.currentSize:
            raise IndexError

        current = self.head
        for i in xrange(0, self.size()-1):
            last = current
            current = current.getNext()
            if i >= index and i < self.size():
                last.setData(current.getData())
        self.tail = last
        self.currentSize -= 1
        return True


    # Will delete element if part of it
    # contains the provided value.
    def removeValueContains(self, value):
        current = self.head
        for i in xrange(0, self.size()-1):
            last = current
            current = current.getNext()
            if str(last.getData()).lower().__contains__(str(value).lower()):
                for j in xrange(i, self.size()-1):
                    last.setData(current.getData())
                    last = current
                    current = current.getNext()
                self.tail = last
                self.currentSize -= 1
                return True
        raise ValueNotFound
        return False


    # Will delete element if it equals
    # to the provided value. Exact match.
    def removeValueEquals(self, value):
        current = self.head
        for i in xrange(0, self.size()-1):
            last = current
            current = current.getNext()
            if last.getData() == value:
                for j in xrange(i, self.size()-1):
                    last.setData(current.getData())
                    last = current
                    current = current.getNext()
                self.tail = last
                self.currentSize -= 1
                return True
        raise ValueNotFound
        return False


    # Will return True if element in the Linked List
    # equals to the provided value. Exact match.
    def containsExactMatch(self, value):
        current = self.head
        for i in xrange(0, self.size()-1):
            last = current
            current = current.getNext()
            if last.getData() == value:
                return True
        return False


    # Will return True if part of some element in the Linked List
    # contains the provided value.
    def containsWithin(self, value):
        current = self.head
        for i in xrange(0, self.size()-1):
            last = current
            current = current.getNext()
            if str(last.getData()).lower().__contains__(str(value).lower()):
                return True
        return False


    def toArray(self):
        list = []
        current = self.head
        for i in xrange(self.size()):
            last = current
            current = current.getNext()
            list.append(last.getData())
        return list


    # To preserve the Pythonic way to iterate through collections,
    # iterate basically converts linked list to array, which you
    # can iterate through using Python's for loop.
    # Example:
    # "for item in myList.iterate():
    #       print item"
    def iterate(self):
        return self.toArray()


    def indexOf(self, value):
        current = self.head
        for i in xrange(self.size()):
            last = current
            current = current.getNext()
            if last.getData() == value:
                return i
        raise ValueNotFound


    def lastIndexOf(self, value):
        current = self.head
        toReturn = -1
        for i in xrange(self.size()):
            last = current
            current = current.getNext()
            if last.getData() == value:
                toReturn = i
        if toReturn >= 0:
            return toReturn
        else:
            raise ValueNotFound


    def set(self, index, value):
        if index < 0 or index > self.currentSize:
            raise IndexError
        if index == self.currentSize:
            self.add(value)
            return
        current = self.head
        for i in xrange(self.size()):
            last = current
            current = current.getNext()
            if i == index:
                last.setData(value)


class ValueNotFound(Exception):
    pass

