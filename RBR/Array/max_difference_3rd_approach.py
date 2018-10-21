def max_differnce(nums):
    min_ele=nums[0]
    cur_diff,max_diff=nums[1]-nums[0],nums[1]-nums[0]
    for i in range(1,len(nums)):
        print(nums[i])
        if nums[i]<min_ele:
            min_ele=nums[i]
            
        else:
            cur_diff=nums[i]-min_ele
            print(cur_diff)
            if cur_diff>max_diff:
                max_diff=cur_diff
    return max_diff


nums=[4,3,10,2,9,1,6]
print(max_differnce(nums))