
r=int(input("how many rows you want:\n") )
obj=(input("input the character to print:\n"))
for i in range(r):

    for k in range (r,i,-1):
        print(" ",end=" ")


    for j in range(i*2 + 1):
        print("",obj,end="")
    print()


# OutPut
    
# how many rows you want:
# 10
# input the character to print:
# *
    
    
#                      *
#                    * * *
#                  * * * * *
#                * * * * * * *
#              * * * * * * * * *
#            * * * * * * * * * * *
#          * * * * * * * * * * * * *
#        * * * * * * * * * * * * * * *
#      * * * * * * * * * * * * * * * * *
#    * * * * * * * * * * * * * * * * * * *