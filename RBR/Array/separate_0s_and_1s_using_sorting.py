def Separtate_0s_1s(nums):
    l,r=0,len(nums)-1
    while l<r:
        while l<r:
            while nums[l]==0 and l<r:
                l+=1
            while nums[r]==1 and r>l:
                r-=1
            if l<r:
                nums[l]=0
                nums[r]=1
                l+=1
                r-=1
    return nums

nums=[0,1,1,0,1,0,1,0,0,0,1]
print(Separtate_0s_1s(nums))