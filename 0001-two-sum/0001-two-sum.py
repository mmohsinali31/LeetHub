class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        alreadySeen={}
        for i, num in enumerate(nums):
            diff=target-num
            if diff in alreadySeen:
                return (alreadySeen[diff],i)
            alreadySeen[num]=i
        