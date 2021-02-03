'''
큐
FIFO
Enqueue(input), Dequeue(output)으로 구성
'''

class Queue:
    def __init__(self):
        self.queue_list = []

    def enqueue(self, data):
        self.queue_list.append(data)

    def dequeue(self):
        if not self.queue_list:
            return False

        out = self.queue_list[0]
        self.queue_list.pop(0)
        return out


# queue = Queue()
#
# for i in range(10):
#     queue.enqueue(i)
# print(queue.queue_list)
#
# for i in range(9):
#     queue.dequeue()
# print(queue.queue_list)

'''
스택
LIFO
push(input), pop(output)
'''


class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, data):
        self.stack_list.append(data)

    def pop(self):
        if not self.stack_list:
            return False

        out = self.stack_list[-1]
        del self.stack_list[-1]
        return out


# stack = Stack()
#
# for i in range(10):
#     stack.push(i)
# print(stack.stack_list)
#
# for i in range(9):
#     stack.pop()
#
# print(stack.stack_list)


'''
Hash Table
open hashing(separate chaining): 해시 테이블의 충돌 문제를 링크드 리스트를 이용해 해결한 방법
close hashing(open addressing): 해시 중복이 발생하면 해당 해시 값부터 순차적으로 빈공간을 찾아 저장
'''


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [0 for i in range(self.table_size)]

    def hash_func(self, key):
        return key % self.table_size

    def get_address(self, key):
        key = ord(key[0])
        hash_address = self.hash_func(key)
        return hash_address

    def save_data(self, key, value):
        hash_add = self.get_address(key)
        self.hash_table[hash_add] = value

    def read(self, key):
        hash_add = self.get_address(key)
        return self.hash_table[hash_add]

    def delete(self, key):
        hash_add = self.get_address(key)
        if self.hash_table[hash_add] != 0:
            self.hash_table[hash_add] = 0


class Openhash:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [0 for i in range(self.table_size)]

    def hash_func(self, key):
        return key % self.table_size

    def get_address(self, key):
        key = ord(key[0])
        # key = hash(key)
        hash_address = self.hash_func(key)
        return hash_address

    def save_data(self, key, value):
        hash_add = self.get_address(key)

        if self.hash_table[hash_add] != 0:
            for i in range(len(self.hash_table[hash_add])):
                if self.hash_table[hash_add][i][0] == key:
                    self.hash_table[hash_add][i][1] = value
            self.hash_table[hash_add].append([key, value])
        else:
            self.hash_table[hash_add] = [[key, value]]

    def read(self, key):
        hash_add = self.get_address(key)

        if self.hash_table[hash_add] != 0:
            for i in range(len(self.hash_table[hash_add])):
                if self.hash_table[hash_add][i][0] == key:
                    return self.hash_table[hash_add][i][1]

    def delete(self, key):
        hash_add = self.get_address(key)

        if self.hash_table[hash_add] != 0:
            for i in range(len(self.hash_table[hash_add])):
                if self.hash_table[hash_add][i][0] == key:
                    if len(self.hash_table[hash_add]) == 1:
                        self.hash_table[hash_add][i] = 0
                    else:
                        del self.hash_table[hash_add][i]


class Closehash:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [0 for i in range(self.table_size)]

    def hash_func(self, key):
        return key % self.table_size

    def get_address(self, key):
        key = ord(key[0])
        hash_address = self.hash_func(key)
        return hash_address

    def save_data(self, key, value):
        hash_add = self.get_address(key)

        if self.hash_table[hash_add] != 0:
            for i in range(hash_add, len(self.hash_table)):
                if self.hash_table[i] == 0:
                    self.hash_table[i] = [key, value]
                    return
        else:
            self.hash_table[hash_add] = [key, value]

    def read(self, key):
        hash_add = self.get_address(key)

        for i in range(hash_add, len(self.hash_table)):
            if self.hash_table[i][0] == key:
                return self.hash_table[i][1]

    def delete(self, key):
        hash_add = self.get_address(key)

        for i in range(hash_add, len(self.hash_table)):
            if self.hash_table[i][0] == key:
                self.hash_table[i] = 0
                return


# h_table = Closehash(8)
# h_table.save_data('Dk', 1111)
# h_table.save_data('Da', 2222)
# print(h_table.read('Dk'))
# print(h_table.hash_table)
# print(h_table.get_address('Dk'))
# h_table.delete('Da')
# print(h_table.hash_table)


'''
Tree
이진 탐색 트리(BST): 탐색 속도 ↑
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.head = None

    def insert(self, value):
        # 루트가 없으면 들어온 값을 루트로
        if self.head is None:
            self.head = Node(value)
        else:
            self.current_node = self.head
            while True:
                # 현재 노드보다 value가 작으면 왼쪽자식으로
                # 왼쪽 자식에 값이 없으면 들어온 값을 왼쪽 자식에 삽입
                # 왼쪽 자식에 값이 있으면 왼쪽자식을 현 노드로
                if value < self.current_node.value:
                    if self.current_node.left is None:
                        self.current_node.left = Node(value)
                        break
                    else:
                        self.current_node = self.current_node.left
                # 현재 노드보다 value가 크면 오른쪽자식으로
                else:
                    if self.current_node.right is None:
                        self.current_node.right = Node(value)
                        break
                    else:
                        self.current_node = self.current_node.right

    def search(self, value):
        # 루트가 없으면 거짓반환
        if self.head is None:
            return False
        else:
            self.current_node = self.head
            while True:
                # value가 현 노드의 값과 같으면 반환
                if value == self.current_node.value:
                    return self.current_node.value
                else:
                    # value가 현 노드 값보다 크면 오른쪽 자식과 비교
                    if value > self.current_node.value:
                        if value == self.current_node.right:
                            return self.current_node.right
                        elif self.current_node.right is None:
                            return "Not found"
                        else:
                            self.current_node = self.current_node.right
                    # value가 현 노드보다 작으면 왼쪽 자식과 비교
                    else:
                        if value == self.current_node.left:
                            return self.current_node.left
                        elif self.current_node.left is None:
                            return "Not found"
                        else:
                            self.current_node = self.current_node.left

    def delete(self, value):
        if self.head is None:
            return False
        else:
            # 삭제할 노드 탐색
            self.current_node = self.head
            self.parent = self.head
            checked = False

            while self.current_node:
                # value값이 현재 노드와 같으면 true
                if value == self.current_node.value:
                    checked = True
                    break
                # value값이 현재 노드보다 크면 현재 노드를 부모노드로
                # 현재 노드의 오른쪽 자식을 현재 노드로
                elif value > self.current_node.value:
                    self.parent = self.current_node
                    self.current_node = self.current_node.right
                else:
                    self.parent = self.current_node
                    self.current_node = self.current_node.left

            if checked is False:
                return False

            # case1 자식이 없는 노드인 경우
            if self.current_node.right is None and self.current_node.left is None:
                if value < self.parent.value:
                    self.parent.left = None
                else:
                    self.parent.right = None

            # case2 자식이 하나있는 노드인 경우
            # 현재 노드의 왼쪽 자식만 있을 때
            elif self.current_node.left is not None and self.current_node.right is None:
                # 현재 노드가 부모 노드의 왼쪽자식일 때
                if value < self.parent.value:
                    self.parent.left = self.current_node.left
                else:
                    self.parent.right = self.current_node.left
            # 현재 노드의 오른쪽 자식만 있을 때
            elif self.current_node.right is not None and self.current_node.left is None:
                if value < self.parent.value:
                    self.parent.left = self.current_node.right
                else:
                    self.parent.right = self.current_node.right

            # case3 자식이 두개 있는 노드인 경우
            elif self.current_node.left is not None and self.current_node.right is not None:
                # 3-1 현재 노드가 부모 노드의 왼쪽 자식일 때
                if value < self.parent.value:
                    self.change_node = self.current_node.right
                    self.change_node_parent = self.current_node.right
                    # 삭제할 노드의 오른쪽 자식 중 가장 작은 값을 change_node로
                    while self.change_node.left is not None:
                        self.change_node_parent = self.change_node
                        self.change_node = self.change_node.left
                    # change_node의 오른쪽에 자식이 있는 경우
                    if self.change_node.right is not None:
                        self.change_node_parent.left = self.change_node.right
                    # change_node의 오른쪽에 자식이 없는 경우
                    else:
                        self.change_node_parent.left = None

                    self.parent.left = self.change_node
                    self.change_node.right = self.current_node.right
                    self.change_node.left = self.change_node.left
                # 3-2 현재 노드가 부모 노드의 오른쪽 자식일 때
                else:
                    self.change_node = self.current_node.right
                    self.change_node_parent = self.current_node.right

                    while self.change_node.left is not None:
                        self.change_node_parent = self.change_node
                        self.change_node = self.change_node.left
                    if self.change_node.right is not None:
                        self.change_node_parent.left = self.change_node.right
                    else:
                        self.change_node_parent.left = None

                    self.parent.right = self.change_node
                    self.change_node.right = self.current_node.right
                    self.change_node.left = self.current_node.left

        return True


BST = BinarySearchTree()
BST.insert(5)
BST.insert(10)
BST.insert(3)
BST.insert(7)
print(BST.search(3))
print(BST.delete(10))


'''
힙
'''
