
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
        print buff_dict

nums=[2,4,3,3]
target=6
sss=Solution()
sss.twoSum(nums,target)
'''
############accepted answer#############
class Solution(object):
    def twoSum(self,nums,target):
        if len(nums)<=1:
            print 'only one element'
        else:
            emptydic={}
            for i in range(len(nums)):
                if nums[i] in emptydic.values():
                    if i>nums.index(target-nums[i]):
                        print [i,nums.index(target-nums[i])]
                    else:
                        print [nums.index(target-nums[i]),i]
                    
                else:
                    #print 'herererer'
                    emptydic[nums[i]]=(target-nums[i])
    
            print emptydic
nums=[2,4,3,3]
target=6
sss=Solution()
sss.twoSum(nums,target)
#########accepted answer###########

class solution(object):
    def twosum(self,nums,target):
        if len(nums)<=1:
            print 'only one element'
        else:
            for i in range(len(nums)):
                #print i
                if target-nums[i] in nums:
                    print 'find it'
                    print nums.index(target-nums[i])

givenNums=[2,7,11,15]
target=9
sss=solution()
sss.twosum(givenNums,target)

###sample code####

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
'''
