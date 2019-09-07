#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 13:43:20 2019
@author: Yesser H. Nasser 
"""
" ============Traversal in Binary Tree ====================="""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    #create a pre-order print function which will be respnsible for printing out the nodes in pre-order fashion    
    #take self since its a member of the calss start is the node that is going to be updated on every recursive call

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type =="inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type =="postorder":
            return self.postorder_print(tree.root, "")
        else:
            print("traversal type" + str(traversal_type) + "is not supported")
    def preorder_print(self, start, traversal):
        """ root - >left subtree -> right subtree """
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def inorder_print(self, start, traversal):
        """ left -> Root -> Right """
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    
    def postorder_print(self, start, traversal):
        """left->right->root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
    
#          1
#      /       \        
#     2        3
#   /  \      / \
#  4   5     6  7
#                \
        #         8
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))