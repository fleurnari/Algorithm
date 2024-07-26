from queue import PriorityQueue

n = int(input())

pq = PriorityQueue()

for i in range(n):
  card = int(input())
  pq.put(card)

card1 = 0
card2 = 0
answer = 0

while pq.qsize() > 1:
  card1 = pq.get()
  card2 = pq.get()
  newCard = card1 + card2
  answer += newCard
  pq.put(newCard)

print(answer)