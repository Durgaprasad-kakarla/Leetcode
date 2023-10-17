class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root=0
        childrens=set(leftChild+rightChild)
        for i in range(n):
            if i not in childrens:
                root=i
        queue=deque([root])
        dictionary={}
        while queue:
            node=queue.popleft()
            if node in dictionary:
                return False
            dictionary[node]=1
            if leftChild[node]!=-1:
                queue.append(leftChild[node])
            if rightChild[node]!=-1:
                queue.append(rightChild[node])
        return len(dictionary)==n
''' Time Complexity--O(n)
    Space complexity--O(n)'''
