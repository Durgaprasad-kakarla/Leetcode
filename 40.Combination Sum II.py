class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        def combine(nums, target):
            ans = []
            temp = []
            nums.sort()#we have to sort the nums as we have to print the list in lexicographical order
            combinations(nums, target, ans, temp, 0)
            return ans


        def combinations(nums, target, ans, temp, ind):
            if target == 0:#if target is zero then put the temp into 'ans' list
                ans.append(temp)
                print(ans)
                return
            for i in range(ind, len(nums)):
                if i > ind and nums[i] == nums[i - 1]:#if i>ind and  one element and it's previous element is same then move to the next index
                    continue
                if nums[i] > target:#if nums[i] is greater than the target then as is it is sorted next elements also bigger than that so break the loop
                    break
                combinations(nums, target - nums[i], ans, temp+[nums[i]], i + 1)#Here backtracking occurs checks the next element and add an element to the temp and target will be reduced target-nums[i]


        ans = combine(nums, target)
        return ans
