n = int(input())
sum = 0
while n != 0:
    sum += (n % 10)
    n = n // 10

isEven = False
if sum % 2 == 0:
    print("Sum ", sum, "is an even number")
else:
    print("Sum ", sum, "is an odd number")

