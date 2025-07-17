class Solution(object): 

    def findKthLargest(self, nums, k):
        """
        - Insert the elements into a max-heap 
        - Heapify (if needed)
        - Search through the heap until 
        the k-th largest element is found 
        --------------------------------------

        Runtime Complexity: 

        Spacetime Complexity: 
        """ 
        self.nums = nums

        max_heap = []

        #insert into the heap 
        for index in range(len(self.nums)):
            max_heap.append(insert(nums[i]))
        print(max_heap)


    def heapifyUp(self, index):

        while index > 0:
            parent_index = index - 1 // 2

            if self.nums[index] > self.nums[parent_index]:
                self.nums[index], self.nums[parent_index] = self.nums[parent_index], self.nums[index]
                index = parent_index 
                heapifyUp(index)
            else:
                break 


    def insert(self, val):

        nums.append(self.val)
        heapifyUp(len(nums)-1)



# Testcases 
first_heap = Solution()
first_heap.findKthLargest([3,2,1,5,6,4], 2)
        