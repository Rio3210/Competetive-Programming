class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def helper(nums, left, right):
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            left_majority = helper(nums, left, mid)
            right_majority = helper(nums, mid+1, right)
            
            if left_majority == right_majority:
                return left_majority
            
            left_count=nums[left:right+1].count(left_majority)
            right_count=nums[left:right+1].count(right_majority)
            # left_count = sum(1 for i in range(left, right+1) if nums[i] == left_majority)
            # right_count = sum(1 for i in range(left, right+1) if nums[i] == right_majority)
            
            return left_majority if left_count > right_count else right_majority
        
        return helper(nums, 0, len(nums)-1)

    
        # hashmap={}
        # for num in nums:
        #     if num not in hashmap:
        #         hashmap[num]=0
        #     hashmap[num]+=1
        # for i in hashmap:
        #     if hashmap[i]>(len(nums)//2):
        #         return i