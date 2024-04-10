class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n=len(deck)
        deck.sort()
        ordered_deck=[0]*n
        queue=deque()
        for i in range(n):
            queue.append(i)
        i=0
        while queue:
            node=queue.popleft()
            ordered_deck[node]=deck[i]
            if queue:
                queue.append(queue.popleft())
            i+=1
        return ordered_deck
''' Time Complexity--O(n)
    Space Complexity--O(n)'''
