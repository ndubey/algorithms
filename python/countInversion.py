
#take input list
print("How many numbers in your list:");

num = 0;
try:
    num = int(input())

except TypeError:
    print("not an integer defaulting to 10 numbers");
    num = 10;

li = []
for i in range(num):
    li.append(int(input()))


#count inversion
count = 0

# 4  8 20 6 7 9 = 4 6 7 8 9   
def numMergeInversion(li, start, end, mid):

    print("start: " + str(start) + " mid: "+ str(mid) + " end: "+ str(end));
    for i in range(start, end+1):
        print(li[i],end=" ")
    print()

    anotherLi = []
    count = 0
    middle = mid
    for i in range (start, end+1):
        if start >= mid:
            break;
        elif mid > end:
            break;
        if li[start] <= li[mid]:
            anotherLi.append(li[start])
            start += 1
        else:
            anotherLi.append(li[mid])
            count += (mid - middle + 1)
            mid += 1
    if start >= mid:
        for i in range(mid, end+1):
            anotherLi.append(li[i])
    elif mid > end:
        anotherLi.append(li[start])
        for i in range(start+1, middle):
            anotherLi.append(li[i])
            count += (end - middle + 1)
    
    li = anotherLi
    print("inversions: " + str(count))        
    return count



def numInversion(li, start, end):
    if start >= end:
        return 0;
    else:
        return numInversion(li,start, (start+end)//2) + \
                numInversion(li,(start+end)//2 + 1, end) + \
                numMergeInversion(li,start,end, (start+end)//2+1);




print(numInversion(li, 0, num -1)) 

print("sorted")
for i in range (num-1):
    print(li[i],end=" ")
