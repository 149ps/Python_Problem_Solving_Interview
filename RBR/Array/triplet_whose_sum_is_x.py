def SumisX(nums):
    nums.sort()
    triplets=[]
    list1=[]
    for i in range(0,len(nums)-2):
        l=i+1
        r=len(nums)-1
        while l<r:
            sum=nums[i]+nums[l]+nums[r]
            if sum==0:
                list1.append(nums[i])
                list1.append(nums[l])
                list1.append(nums[r])
                triplets.append(list1)
                print(triplets)
            if sum<0:
                l+=1
            if sum>0:
                r-=1
    return triplets
nums=[-1, 0, 1, 2, -1, -4]
print(SumisX(nums))