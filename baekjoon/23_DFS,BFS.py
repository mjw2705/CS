import sys


def Dfs_2606():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    dic = {}
    for i in range(n):
        dic[i + 1] = set()

    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        dic[a].add(b)
        dic[b].add(a)

    def dfs(start, dic):
        for i in dic[start]:
            if i not in visit:
                visit.append(i)
                dfs(i, dic)

    def bfs(start, dic):
        queue = [start]
        while queue:
            for i in dic[queue.pop()]:
                if i not in visit:
                    visit.append(i)
                    queue.append(i)

    visit = []
    dfs(1, dic)
    print(len(visit) - 1)





# if __name__ == '__main__':
    # dfs_2606()