#check whether binary representation is a palindrome

print("Enter a positive integer: ")
num = int(input())
#reverse the bits and take &
temp = num
reversedNum = 0
while temp > 0:
    reversedNum <<= 1
    reversedNum |= (temp&1)
    temp >>= 1
    #print(reversedNum)
#print(reversedNum)
print(reversedNum == num)


