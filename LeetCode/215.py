# import heapq
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         # nums.sort()
#         # self.insertionSort(nums)
#         # nums = self.heapSort(nums)
#         nums = self.mergeSort(nums)
#         return(nums[len(nums)-k])
#     def insertionSort(self, nums):
#         for i in range(len(nums)):
#             k = nums.index(min(nums[i:len(nums)]), i, len(nums))
#             nums[k], nums[i] = nums[i], nums[k]
#     def heapSort(self, nums):
#         heapq.heapify(nums)
#         sorted_nums_heap = []
#         for i in range(len(nums)):
#             sorted_nums_heap.append(heapq.heappop(nums))
#         return sorted_nums_heap
#     def mergeSort(self, nums):
#         if len(nums) == 1:
#             return nums
#         else:
#             a = self.mergeSort(nums[:len(nums)//2])
#             b = self.mergeSort(nums[len(nums)//2: len(nums)])
#             return self.merge(a, b)

#     def merge(self, a, b):
#         i = 0
#         j = 0
#         split_list = []
#         while i < len(a) and j < len(b):
#             if a[i] < b[j]:
#                 split_list.append(a[i])
#                 i += 1
#             else:
#                 split_list.append(b[j])
#                 j += 1
#         if i < len(a):
#             split_list.extend(a[i:len(a)])
#         if j < len(b):
#             split_list.extend(b[j:len(b)])
#         return split_list




import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # self.insertionSort(nums)
        # nums = self.heapSort(nums)
        # nums = self.mergeSort(nums)
        # return(nums[len(nums)-k])
        return self.quickSelect(nums, 0, len(nums)-1, k)
    def insertionSort(self, nums):
        for i in range(len(nums)):
            k = nums.index(min(nums[i:len(nums)]), i, len(nums))
            nums[k], nums[i] = nums[i], nums[k]
    def heapSort(self, nums):
        heapq.heapify(nums)
        sorted_nums_heap = []
        for i in range(len(nums)):
            sorted_nums_heap.append(heapq.heappop(nums))
        return sorted_nums_heap
    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        else:
            a = self.mergeSort(nums[:len(nums)//2])
            b = self.mergeSort(nums[len(nums)//2: len(nums)])
            return self.merge(a, b)

    def merge(self, a, b):
        i = 0
        j = 0
        split_list = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                split_list.append(a[i])
                i += 1
            else:
                split_list.append(b[j])
                j += 1
        if i < len(a):
            split_list.extend(a[i:len(a)])
        if j < len(b):
            split_list.extend(b[j:len(b)])
        return split_list
    
    def quickSelect(self, nums, s, e, k):
        pivot = self.partition(nums, s, e)
        if pivot == len(nums)-k:
            return nums[pivot]
        elif pivot < len(nums)-k:
            return self.quickSelect(nums, pivot+1, e, k)
        else:
            return self.quickSelect(nums, s, pivot-1, k)
        
    def partition(self, nums, s, e):
        nums[s], nums[s+(e-s)//2] = nums[s+(e-s)//2], nums[s]
        i = s
        j = s + 1
        while j <= e:
            if nums[j] < nums[s]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        
        nums[s], nums[i] = nums[i], nums[s]
        return(i)
        