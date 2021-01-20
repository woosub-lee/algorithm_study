# 이진 탐색 트리 예제(공부 중)
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def size(self):
        left_size = self.left.size() if self.left else 0  # 재귀 (왼쪽노드가 존재하면 왼쪽의 size())
        print(left_size)
        right_size = self.right.size() if self.right else 0  # 재귀 (오른쪽노드가 존재하면 오른쪽의 size())
        print(right_size)
        return left_size + right_size + 1

    def depth(self):
        left_depth = self.left.depth() if self.left else 0  # 재귀 (왼쪽노드가 존재하면 왼쪽의 depth())
        print(left_depth)
        right_depth = self.right.depth() if self.right else 0  # 재귀 (오른쪽노드가 존재하면 오른쪽의 depth())
        print(right_depth)
        return left_depth + 1 if left_depth > right_depth else right_depth + 1  # 왼쪽깊이와 오른쪽깊이 중 큰 것


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)  # 재귀
                print('insert left', data)
            else:
                node.right = self._insert_value(node.right, data)  # 재귀
                print('insert right', data)
        return node

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is not None:
            print('finding:', key, 'at:', root.data)
        if root is None or root.data == key:
            print('finished!!!', root.data)
            return root is not None
        elif key < root.data and root.left is not None:
            print('finding... left', root.left.data)
            return self._find_value(root.left, key)
        elif key > root.data and root.right is not None:
            print('finding... right', root.right.data)
            return self._find_value(root.right, key)

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0


array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinaryTree()
for x in array:
    bst.insert(x)

# Find
bst.find(15)
bst.find(49)
print('size of bst:', bst.size())
print('depth of bst:', bst.depth())
