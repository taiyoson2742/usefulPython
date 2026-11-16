#written 11.16.26
#@title Implementing a Binary Search Tree
class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insertLeft(self, node):
        if self.left == None:
            self.left = node
        else:
            node.left = self.left
            self.left = node

    def insertRight(self, node):
        if self.right == None:
            self.right = node
        else:
            node.right = self.right
            self.right = node

    def __repr__(self):
        s = f'{self.data}'
        s += '('
        if self.left != None:
            s += repr(self.left)
        s += ')('
        if self.right != None:
            s += repr(self.right)
        s += ')'
        return s


class BST(BinaryTree):
    def find(tree, key):
        '''Returns the value associated with a given key.'''
        ### YOUR SOLUTION HERE
        if tree is None:
            return None
        if tree.data[0] == key:
            return tree.data[1]
        elif key < tree.data[0]:
            return BST.find(tree.left, key)
        else:
            return BST.find(tree.right, key)

r = BST((4, 'Reimu'))
r.insertLeft(BST((2, 'Marisa')))
r.insertRight(BST((6, 'Cirno')))
r.left.insertLeft(BST((1, 'Koakuma')))
r.left.insertRight(BST((3, 'Yukari')))
r.right.insertLeft(BST((5, 'Yuyuko')))
print(r)
print(BST.find(r,5))