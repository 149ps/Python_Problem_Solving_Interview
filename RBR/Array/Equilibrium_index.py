def pivot_index(nums):
    sum,left_sum=0,0
    for i in range(len(nums)):
        sum+=nums[i]
    for j in range(len(nums)):
        sum-=nums[j]
        if left_sum==sum:
            return j
        left_sum+=nums[j]

nums=[7,2,1,4,6,4,0]
print(pivot_index(nums))
        