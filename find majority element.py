class Solution(object):
    def majorityElement(self, nums):
        count = 0
        store = None
        for num in nums:
            if count == 0:
                store = num
            if num == store:
                count += 1
            else:
                count -= 1
        return store