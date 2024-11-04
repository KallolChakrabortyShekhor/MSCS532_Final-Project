class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, start, end, weight):
        self.adjacency_list[start].append((end, weight))


import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, cost, node):
        heapq.heappush(self.heap, (cost, node))

    def pop(self):
        return heapq.heappop(self.heap)


class AVLNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key, data):
        if not root:
            return AVLNode(key, data)
        elif key < root.key:
            root.left = self.insert(root.left, key, data)
        else:
            root.right = self.insert(root.right, key, data)
        # Update height and balance
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return self.balance(root)
