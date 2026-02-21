print("Digit Frequency Counter")
num = int(input("Enter number: "))
zero = 0
other = 0
while num > 0:
digit = num % 10
if digit == 0:
zero = zero + 1
else:
other = other + 1
num = num // 10
print("Zero digits:", zero)
print("Other digits:", other)
if zero > other:
print("More zeros")
else:
print("More non-zero digits"
total = zero + other
print("Total digits:", total)