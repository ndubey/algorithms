# count number of bits set in binary representation doesn't work on negative numbers

print("Enter a positive integer in decimal form:")
num = int(input())
cnt = 0
while num != 0:
    cnt += num&1
    num = num>>1
    print(num)

print("Number of bits set: %d" %cnt) 
