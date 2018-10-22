def OddnumberofTimes(nums):
    hash={}
    odd_number=set()
    for i in nums:
        hash[i]=hash.get(i,0)+1
    for k,v in hash.items():
        if hash[k]%2!=0:
            odd_number.add(k)
    return odd_number

nums=[3,2,1,2,3,1,1]
print(OddnumberofTimes(nums))
            