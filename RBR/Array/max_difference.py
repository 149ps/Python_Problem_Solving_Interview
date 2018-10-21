def max_difference(nums):
    cur_max=0
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]<nums[j]:
                if (nums[j]-nums[i])>cur_max:
                    cur_max=nums[j]-nums[i]
                    a=nums[i]
                    b=nums[j]
    return cur_max,a,b

nums=[3,1,4,7,5,100,10]
print(max_difference(nums))
