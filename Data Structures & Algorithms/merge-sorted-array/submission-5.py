class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        nums1Pointer, nums2Pointer = 0,0
        nums1copy = nums1.copy()

        while index < (m + n):
            if nums2Pointer >= n or (nums1Pointer < m and nums1copy[nums1Pointer] <= nums2[nums2Pointer]):
                nums1[index] = nums1copy[nums1Pointer]
                nums1Pointer += 1
            else:
                nums1[index] = nums2[nums2Pointer]
                nums2Pointer += 1
            index += 1



        
