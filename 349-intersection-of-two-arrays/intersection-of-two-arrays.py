class Solution(object):
    def intersection(self, nums1, nums2):
        elements=[]
        for i in nums1:
            if i in nums2 and i not in elements:
                elements.append(i)
        return elements

        