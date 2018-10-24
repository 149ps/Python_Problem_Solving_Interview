def OddnumberofTimes(nums):
    result=0
    for i in nums:
        result=result^i
    return result

nums=[3,2,1,2,3,1,61]
print(OddnumberofTimes(nums))