class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(arr,l,mid,r):
            j=mid+1
            total=0
            for i in range(l,mid+1):
                while j<=r and nums[i]>2*nums[j]:
                    j+=1
                total+=(j-(mid+1))
            left=l
            right=mid+1
            temp=[]
            while left<=mid and right<=r:
                if arr[left]<=arr[right]:
                    temp.append(arr[left])
                    left+=1
                else:
                    temp.append(arr[right])
                    right+=1
            while left<=mid:
                temp.append(arr[left])
                left+=1
            while right<=r:
                temp.append(arr[right])
                right+=1
            for i in range(l,r+1):
                arr[i]=temp[i-l]
            return total
        def mergesort(arr,l,r):
            if l>=r:
                return 0
            mid=(l+r)//2
            inv=mergesort(arr,l,mid)
            inv+=mergesort(arr,mid+1,r)
            inv+=merge(arr,l,mid,r)
            return inv
        return mergesort(nums,0,len(nums)-1)
 ''' Time Complexity--O(nlogn)+O(n)+O(n)
     Space Complexity--O(n)'''
