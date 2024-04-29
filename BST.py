from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self) -> None:
        self.root = None
        self.arr = []
        self.__predecessor = None
        self.__successor = None

    def in_order_traversal(self, node, target=None) -> Optional[Node]:
        if not node:
            return
        self.in_order_traversal(node.left)
        if self.arr:
            if self.arr[-1] == target:
                self.__successor = node
            if node == target:
                self.__predecessor = self.arr[-1]
        self.arr.append(node)
        self.in_order_traversal(node.right)

    def getPredecessor(self, node) -> Optional[Node]:
        self.__predecessor = None  # Just in case there's a value stored in it
        self.in_order_traversal(self.root, node)
        return self.__predecessor

    def getSuccessor(self, node) -> Optional[Node]:
        self.__predecessor = None
        self.in_order_traversal(self.root, node)
        return self.__successor

    def iterative_search(self, val) -> bool:
        current = self.root
        while current:
            if current.val == val:
                return True
            elif val < current.val:
                current = current.left
            else:
                current = current.right

    def search(self, val) -> bool:
        if self.root:
            return BST.__search(self.root, val)
        else:
            return False

    @staticmethod
    def __search(node, val) -> bool:
        if not node:
            return False
        if node.val == val:
            return True
        elif node.val < val:
            return BST.__search(node.right, val)
        else:
            return BST.__search(node.left, val)

    def insert(self, val) -> None:
        if not self.root:
            self.root = Node(val)
        else:
            self.__insert(self.root, val)

    @staticmethod
    def __insert(node, val) -> None:
        if not node:
            return node(val)
        elif node.val < val:
            node.right = BST.__insert(node.right, val)
        else:
            node.left = BST.__insert(node.left, val)
        return node

    def getMin(self) -> Optional[Node]:
        node = self.root
        while node.left:
            node = node.left
        return node

    def getMax(self) -> Optional[Node]:
        node = self.root
        while node.right:
            node = node.right
        return node

    def delete(self, val) -> None:
        if not self.root:
            return
        self.__delete(self.root, val)

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
        return node

    def getHeight(self, node) -> int:
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        return max(left, right) + 1

