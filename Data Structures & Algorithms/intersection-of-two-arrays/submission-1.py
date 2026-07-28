class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        res = []

        for num2 in nums2:
            if num2 in seen:
                res.append(num2)
                seen.remove(num2)
        return res
        