class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        tracker = {}
        for num in nums:
            if tracker.get(num):
                return True
            else:
                tracker[num] = 1
        return False




