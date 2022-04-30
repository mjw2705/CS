import sys
import heapq

N = 3
cards = [10, 20, 40]

# N = int(input())
# cards = []
# for _ in range(N):
#     cards.append(int(sys.stdin.readline().strip()))
# print(N, cards)
answer = 0

heapq.heapify(cards)

if N == 1:
    print(0)
else:
    while len(cards) > 1:
        comp = heapq.heappop(cards) + heapq.heappop(cards)
        answer += comp
        heapq.heappush(cards, comp)
    print(answer)