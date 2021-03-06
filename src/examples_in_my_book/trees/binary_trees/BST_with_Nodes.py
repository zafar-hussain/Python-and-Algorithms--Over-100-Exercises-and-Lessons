#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail



class Node(object):
    def __init__(self, value):
        self.value = value  
        self.left = None 
        self.right = None 

    def __repr__(self):
        return '{}'.format(self.value)
          

class BSTwithNodes(object):
    def __init__(self): 
        self.root = None


    def insert(self, value):  
        if self.root == None:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(value)
                        break;      

                elif value > current.value:               
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(value)
                        break;      
                else:
                    break 


def main():
    """
    BST
          4
       2     6
     1   3 5   7
    """
    tree = BSTwithNodes()
    l1 = [4, 2, 6, 1, 3, 7, 5]
    for i in l1: tree.insert(i)
    print(tree.root)
    print(tree.root.right)
    print(tree.root.right.left)
    print(tree.root.right.right)
    print(tree.root.left)
    print(tree.root.left.left)
    print(tree.root.left.right)


if __name__ == '__main__':
    main()

