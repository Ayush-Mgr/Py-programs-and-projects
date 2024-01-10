class Task:
    def __init__(self, Title):
        self.Title = [Title]


    def rtn(self):
        result = ""
        for i in range(len(self.Title)):
            a = i + 1
            result += f"\n tasks no {a}: {self.Title[i]}"
        return result

# Create instances of the Task class
uu = Task("uu")
bu = Task("bu")
cu = Task("cu")


# Print the information for each instance
print(uu.rtn())
print(bu.rtn())
print(cu.rtn())
