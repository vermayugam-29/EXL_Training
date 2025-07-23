withrawalAmt = int(input("Please enter amount to withdraw"))
totalAmt = 50000

while True:
    if withrawalAmt >= totalAmt:
        withrawalAmt = int(input("Insufficient balance please try again :"))
    elif withrawalAmt % 100 != 0:
        withrawalAmt = int(input("Please enter valid denomination: "))
    else:
        totalAmt -= withrawalAmt
        break

print("Balance is", totalAmt)