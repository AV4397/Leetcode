class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i+1, len(nums) - 1
            while l < r:
                totalSum = nums[i] + nums[l] + nums[r]

                if totalSum > 0:
                    r -= 1
                elif totalSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                
        return res
