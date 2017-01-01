#Binary To Hexadecimal.



def convertHex(fourBinDig):
    assert(len(fourBinDig) <= 4, "Should be less than four digit")
    power = 1;
    num = 0
    for i in range (len(fourBinDig)):
        num += power*int(fourBinDig[-i - 1])
        power *= 2
    print("binary num : " + fourBinDig + " hex: "+str(num))
    if num < 10:
        return str(num)
    elif num == 10:
        return 'A'
    elif num == 11:
        return 'B'
    elif num == 12:
        return 'C'
    elif num == 13:
        return 'D'
    elif num == 14:
        return 'E'
    elif num == 15:
        return 'F'



print("Enter a binary number:")


binary = input()
li = []
def toHex(binary, li):
    if len(binary) < 4:
        li.append(convertHex(binary))
    else:
        li.append(convertHex(binary[-4:]))
        toHex(binary[0:-4],li)

toHex(binary,li)

#reverse the list
li.reverse()
hexnum = "".join(li)
print(hexnum)


