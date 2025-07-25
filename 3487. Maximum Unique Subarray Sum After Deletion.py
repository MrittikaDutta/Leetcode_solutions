class Solution:
    def maxSum(self, nums: List[int]) -> int:
        l1=len(nums)
        l=[]
        c=0

        if l1==1:
            return nums[0]
        
        for i in nums:
            if i>0:
                l.append(i)
            else:
                c+=1
        if c==l1:
            return max(nums)
        return sum(list(set(l)))
