def Separtate_0s_1s(nums):
    count0=nums.count(0)
    count1=nums.count(1)
    print(count1,count0)
    for i in range(count0):
        nums[i]=0
    for j in range(count1):
        nums[i+j]=1
    return nums

nums=[0,1,1,0,1,0,1,0,0,0,1]
print(Separtate_0s_1s(nums))
        
            