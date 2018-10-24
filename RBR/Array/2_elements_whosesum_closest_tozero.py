def closest_tozero(nums):
    nums.sort()
    l,r=0,len(nums)-1
    cur_sum=0
    closest_sum=999999
    cur_sum=nums[l]+nums[r]
    min_l,max_r=l,r
    while l<r:
        if abs(cur_sum)<abs(closest_sum):
            closest_sum=cur_sum
            min_l=l
            max_r=r
        if cur_sum<0:
            l+=1
        else:
            r-=1
    return closest_sum

nums=[-79,-9,0,59,69,84]
print(closest_tozero(nums))
            