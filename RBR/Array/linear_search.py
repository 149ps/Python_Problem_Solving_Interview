def linear_search(a,target):
    i=0
    b=[]
    for i in range(len(a)):
        if a[i]==target:
            b.append(i)
        else:
            i+=1
    return b


a=[1,2,34,5,4,6,22,123,341,2]
print(linear_search(a,2))