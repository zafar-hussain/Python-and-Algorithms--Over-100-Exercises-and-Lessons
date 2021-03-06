#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

from node import Node

class UnorderedList(object):
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


def test_UnorderedList(module_name='this module'):
    llist = UnorderedList()
    llist.add(31)
    llist.add(22)
    llist.add(10)
    assert(llist.search(22) == True)
    llist.remove(22)
    assert(llist.search(22) == False)   
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))


if __name__ == '__main__':
    test_UnorderedList()


