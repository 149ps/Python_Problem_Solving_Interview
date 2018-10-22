def OddnumberofTimes(nums):
    result=0
    for i in nums:
        result=result^i
    return result

nums=[3,2,1,2,3,1,1]
print(OddnumberofTimes(nums))