nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

import sys

sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def solution(nodeinfo):
    def preorder(node):
        preorders.append(node.value[2])
        if node.left:
            preorder(node.left)
        if node.right:
            preorder(node.right)

    def postorder(node):
        if node.left:
            postorder(node.left)
        if node.right:
            postorder(node.right)
        postorders.append(node.value[2])

    answer = []
    preorders = []
    postorders = []
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)

    sortednode = sorted(nodeinfo, key=lambda  x: (-x[1], x[0]))
    print(sortednode)

    root = None
    for node in sortednode:
        if not root:
            root = Tree(node)
        else:
            current = root
            while True:
                # 현재 root보다 들어온 값이 작고, 왼쪽노드에 자식이 없으면 왼쪽노드로 삽입
                if node[0] < current.value[0]:
                    if current.left:
                        current = current.left
                        continue
                    else:
                        current.left = Tree(node)
                        break
                if node[0] > current.value[0]:
                    if current.right:
                        current = current.right
                        continue
                    else:
                        current.right = Tree(node)
                        break

    preorder(root)
    postorder(root)
    answer.append(preorders)
    answer.append(postorders)

    return answer

print(solution(nodeinfo))