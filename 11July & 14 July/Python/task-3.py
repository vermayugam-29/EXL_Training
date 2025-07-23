price = float(input("Enter the price of item : "))
quantity = float(input("Enter the quantity of item : "))

totalBill = price * quantity
print("Total Price" , totalBill)

if totalBill > 5000 :
    discount = 0.15 * totalBill
    totalBill -= discount

print("Price after discount" , totalBill)

gst = 0.18 * totalBill

totalBill += gst

print("Final Amount to Pay :", totalBill)






