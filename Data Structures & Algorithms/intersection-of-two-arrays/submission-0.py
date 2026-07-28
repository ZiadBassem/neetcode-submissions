class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dummy = set()
        res = set()
        for num1 in nums1:
            dummy.add(num1)
        for num2 in nums2:
            if num2 in dummy:
                res.add(num2)
        return list(res)




        