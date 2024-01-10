taskList=[]

class task :
    def __init__(self,Title):
        self.Title = [Title]

    def rtn(self):

        result = ""

        for i in range(len(self.Title)): # i is not updating sutck at a = 1 
            a=i+1
            result +=  f"\n tasks no {a}: {self.Title[i]}"
        return result 
    

while True :    
    order1 = input("Press 'A' to ADD tasks and 'D' to Delete tasks or 'Q'  : \n").upper()
    if len(order1) == 1 :
        pass
    


    if order1 == "A" :
        noTask=int(input("Input no of tasks : \n"))



        for i in range(noTask):
             TTask=input("Input task no {} : \n".format(i+1) )
             a = task(TTask)
             taskList.append(a)

        for i in taskList:
           print(i.rtn())




    elif order1 == "D" :
         if len(taskList) == 0 :
             print("\nNo Tasks Available To Be Deleted.\n")
         else:
             n = int(input("Enter the tasks no you want to delete : \n"))
             del taskList[n-1]
             for i in taskList:
                print(i.rtn())

             

    elif order1 == "Q" :
        break
    else:
        print("\n*****************Input Single character***************\n")
        input("Press 'A' to ADD tasks and 'D' to Delete tasks : \n").upper()
   

# Output :
#Press 'A' to ADD tasks and 'D' to Delete tasks or 'Q'  : 
#A
#Input no of tasks :
#3
#Input task no 1 :
#a
#Input task no 2 :
#b
#Input task no 3 :
#c
#
# tasks no 1: a
#
# tasks no 1: b
#
# tasks no 1: c


# task no not changing 


