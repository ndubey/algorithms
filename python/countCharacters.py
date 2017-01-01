print("Please enter your string to count the caharcters")

str = input()

D = {}
for char in str:
    D.setdefault(char, 0)
    D[char] += 1;

print(D)

