def calculate_factorial(a):
   
    ans = 1
    for number in range(1, a + 1):
        ans *= number
    print("Factorial of", a, "is", ans)


a =  int(input("the number you want Factorial off : \n "))
    
calculate_factorial(a)
 
