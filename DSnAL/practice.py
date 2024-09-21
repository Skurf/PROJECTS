# twoSum

class Solution:
    def twoSum(self,nums: List[int],target:int) -> List[int]:
        prevMap={} #value:index

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
            return
        
#buylowsellhigh
        #twoPointers
        
    def maxProfit(self,prices:List[int]) -> int:
        l,r = 0,1 #l=buy&r=sell
        while r < len(prices):
            #profitable?
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                maxP = max(maxP,profit)
            else:
                l=r
                r += 1
        return maxP
    
    def containsDuplicate(self,nums:List[int])->bool:
        hashset = set()
        for n in nums
        if n in hashset :
            return True
        hashset.add(n)
        return False

    def productExceptSelf(self,nums:List[int])->List[int]:
        res = [1]*(len(nums))
        prefix = 1
        for i in range (len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
    def maxSubarray(self,nums:List[int])->int:
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub,curSum)
        return maxSub

    def moveZeroes(self,nums:List(int))->None:
        prev = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                tmp = nums[prev]
                nums[prev]=nums[i]
                nums[i]=tmp
                prev += 1 

    