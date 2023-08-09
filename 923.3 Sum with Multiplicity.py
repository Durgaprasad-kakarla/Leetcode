class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = []
        arr.sort()
        n=len(arr)
        dict1=Counter(arr)
        count=0
        def ncr(n,r):
            res=1
            for i in range(r):
                res=(res*(n-i))//(i+1)
            return res
        for i in range(n):
            if i != 0 and arr[i] == arr[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                total_sum = arr[i] + arr[j] + arr[k]
                if total_sum < target:
                    j += 1
                elif total_sum > target:
                    k -= 1
                else:
                    nums = [arr[i], arr[j], arr[k]]
                    dict2=Counter(nums)
                    res=1
                    for x in set(nums):
                        res=res*ncr(dict1[x],dict2[x])
                    count+=res
                    j += 1
                    k -= 1
                    while j < k and arr[j] == arr[j - 1]:
                        j += 1
                    while j < k and arr[k] == arr[k + 1]:
                        k -= 1
        return count%(10**9+7)
''' Time Complexity--O(n*n)
    Space Complexity--O(n)'''
