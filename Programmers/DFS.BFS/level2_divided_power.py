ns = 9, 4, 7
wiress = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]], [[1,2],[2,3],[3,4]], [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

from collections import defaultdict, deque

def bfs(graph, start, visited):
    queue = deque([start])
    result = 1
    visited[start] = True
    while queue:
        v =  queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                result += 1
                queue.append(i)
                visited[i] = True
    return result

def solution(n, wires):
    line = defaultdict(list)
    for f, s in wires:
        line[f].append(s)
        line[s].append(f)

    answer = n
    for start, not_visit in wires:
        visited = [False] * (n+1)
        visited[not_visit] = True
        result = bfs(line, start, visited)
        answer = min(abs(result - (n-result)), answer)
    return answer

for n, wires in zip(ns, wiress):
    print(solution(n, wires))
