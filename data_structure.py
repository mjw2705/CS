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
        if self.head == None:
            self.head = Node(value)
