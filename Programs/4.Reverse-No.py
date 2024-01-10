reverse = 0
Num = int(input("Type Number to reverse: "))

while Num != 0:
    last_digit = Num % 10 
    reverse = reverse * 10 + last_digit
    Num //= 10


print("The reversed No is:", reverse)
