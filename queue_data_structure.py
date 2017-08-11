


class Queue():

    def __init__(self):
        self.__queue = []

    def isEmpty(self):
        return len(self.__queue) == 0

    def push(self, object):
        self.__queue.append(object)

    def pop(self):
        if self.isEmpty():
            return 0
        else:
            objectToReturn = self.__queue[0]
            self.__queue.pop(0)
            return objectToReturn

    def peek(self):
        return self.__queue[0]

    def search(self, object):
        return self.__queue.index(object)

    def size(self):
        return len(self.__queue)
