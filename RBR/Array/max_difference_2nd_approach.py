def max_difference(nums):
    diff=[]
    for i in range(0,len(nums)-1):
        diff.append(nums[i+1]-nums[i])
    return maxSubArray(diff)
    

def maxSubArray(nums):
    max_sum=nums[0]
    for i in range(1,len(nums)):
        if nums[i]>0:
            nums[i]=nums[i]+nums[i-1]
        max_sum=max(max_sum,nums[i])
    return max_sum


nums=[3,1,4,7,5,100,10]
print(max_difference(nums))