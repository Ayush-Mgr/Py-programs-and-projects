i = 1
temp = 0
a = int(input("enter the deecimal No :"))
while a != 0 :
    d = a % 2
    temp = temp + (d * i)

    a=a//2
    
    i = i * 10
print("Binary No is: ",temp)



#OutPut:
# enter the deecimal No :23
# Binary No is:  10111
