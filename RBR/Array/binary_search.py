def binary_search(nums,target):
    l=0
    r=len(nums)-1
    while l<=r:
        m=l+(r-l)//2
        if target==nums[m]:
            return m
        if target>nums[m]:
            l=m+1
        else:
            r=m-1
    return l

a=[1,3,5,6]
print(binary_search(a,5))
    