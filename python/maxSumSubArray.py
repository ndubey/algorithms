#Given an array, to find the longest and continuous sub array and get the max sum of the sub array in the given array.



def findMaxSumSubArray(li):
    #{i,j} sub array ending at j 
    maxSubArray=[]
    if len(li) < 1:
        return 0
    maxSubArray.append(li[0])
    largest = li[0]
    for i in range(1,len(li)):
        if maxSubArray[i-1] < 0:
            maxSubArray.append(li[i])
        else:
            maxSubArray.append(maxSubArray[i-1]+li[i])
        if largest < maxSubArray[i]:
            largest = maxSubArray[i]
    #now output result
    return largest




print(" Hom many numbers in your array:")
num = int(input())
li = []
print("Please enter the numbers in the array: ")
for i in range(num):
    li.append(int(input()))

print(findMaxSumSubArray(li))

