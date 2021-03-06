#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


class BT(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None       

    
    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def is_leaf(self):
        return self.left is None and self.right is None

    def set_root(self, obj):
        self.value = obj
    
    def get_root(self):
        return self.value
        
    def insert_left(self, new_node):
        if self.left == None:
            self.left = BT(new_node)
        else:
            t = BT(self.left)
            t.left = new_node
            self.left = t
    
    def insert_right(self, new_node):
        if self.right == None:
            self.right = BT(new_node)
        else:
            t = BT(self.right)
            t.right = new_node
            self.right = t
            
    def __repr__(self):
        return '{}'.format(self.value)



def tests_BT():
    """
            1 
       2       3
    4   5     6    7
    """  
    tree = BT(1)
    tree.insert_left(2)
    tree.insert_right(3)
    tree.get_left().insert_left(4)
    tree.get_left().insert_right(5)
    tree.get_right().insert_left(6)
    tree.get_right().insert_right(7)
    print(tree.get_right().get_right())
    tree.get_right().get_right().set_root(8)
    print(tree.get_right().get_right())
    assert(tree.get_right().is_leaf() == False)
    assert(tree.get_right().get_right().is_leaf() ==  True)
    print("Tests Passed!")
    

if __name__ == '__main__':
    tests_BT()
    
