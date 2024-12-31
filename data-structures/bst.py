class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def inOrderHelper(self, node):
        if node is not None:
            self.inOrderHelper(node.left)
            print(node.data, end= " ")
            self.inOrderHelper(node.right)

    def preOrderHelper(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preOrderHelper(node.left)
            self.preOrderHelper(node.right)

    def postOrderHelper(self, node):
        if node is not None:
            self.postOrderHelper(node.left)
            self.postOrderHelper(node.right)
            print(node.data, end=" ")

    def findMin(self, node):
        if node.left is None:
            return node
        # recursively call findMin until there is no left child node (indicating this is the minimum)
        return self.findMin(node)

    def deleteNode(self, root, value):
        if root is None:
            return root
        
        if value < root.data:
            root.left = self.deleteNode(root.left, value)
        elif value > root.data:
            root.right = self.deleteNode(root.right, value)

        # if we are on the node to delete
        else:
            # if node has one child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # if node has two children
            # find in-order successor (min node in right subtree)
            temp = self.findMin(root.right)

            # assign the value of the node to delete as the in-order successor
            root.data = temp.data

            # delete the in-order successor through recursive call of deleteNode
            # with the right node as the root
            root.right = self.deleteNode(root.right, temp.data)
        
        return root
    
    def deleteMethod(self, value):
        self.root = self.deleteNode(self.root, value)

    def insert(self, value):
        new_node = Node(value)

        # if no root node (first node to be inserted)
        # set as root node of this BST obj
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            parent = None

            while current is not None:
                parent = current
                if value < current.data:
                    current = current.left
                else:
                    current = current.right

            if value < parent.data:
                parent.left = new_node
            else:
                parent.right = new_node

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.data:
                return True
            elif value < current.data:
                current = current.left
            else:
                current = current.right
        return False

    # in-order traversal - left subtree > current node > right subtree
    def inOrder(self):
        self.inOrderHelper(self.root)
        print()

    # pre-order traversal - current node > left subtree > right subtree
    def preOrder(self):
        self.preOrderHelper(self.root)
        print()

    # post-order traveresal - left subtree > right subtree > current node
    def postOrder(self):
        self.postOrderHelper(self.root)
        print()