from typing import Optional
from BST import BST


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class AVL(BST):
    def bf(self, node):
        return self.getHeight(node.left) - self.getHeight(node.right)

    @staticmethod
    def rightRotate(node):
        y = node.left
        node.left.right, node.left = node, node.left.right
        return y

    @staticmethod
    def leftRotate(node):
        y = node.right
        node.right.left, node.right = node, node.right.left
        return y

    def __insert(self, node, val) -> Node:
        if not node:
            return Node(val)
        if node.val < val:
            node.right = AVL.__insert(self, node.right, val)
        else:
            node.left = AVL.__insert(self, node.left, val)

        factor = AVL.bf(self, node)
        if factor > 1:
            if val > node.left.val:
                node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        elif factor <= -1:
            if val < node.right.val:
                node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

    def __delete(self, node, val) -> Node:
        if val < node.val:
            node.left = self.__delete(node.left, val)
        elif val > node.val:
            node.right = self.__delete(node.right, val)
        else:
            if node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            else:
                cur = node.right
                while cur.left:
                    cur = cur.left
                node.val = cur.val
                node.right = self.__delete(node.right, node.val)

        factor = self.bf(node)
        if factor > 1:
            if self.bf(node.left) < 0:
                node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        elif factor < 0:
            if self.bf(node.right) > 0:
                node.right = self.rightRotate(node.right)
            return node.leftRotate(node)
        return node