class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        count=1
        longest=0
        nums.sort()
        for i in range(len(nums)):
            if i+1<len(nums) and nums[i] == nums[i+1]:
                continue
            if i+1<len(nums) and nums[i]+1 == nums[i+1]:
                count+=1
            else:
                longest=max(longest,count)
                count=1
        longest=max(longest,count)
        return longest
        