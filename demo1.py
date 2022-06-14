class employee:
    increment = 1.5

    def __init__(self,name,lname,salary):
        self.name = name
        self.lname = lname
        self.salary = salary
        self.increment = 1.5

    def increase(self):
        self.salary = int(self.salary * self.increment)


a = employee('jack','jacson', 4000)
b = employee('rohan','das', 6000)

print(a.salary)
a.increase()
print(a.salary)

# print(a.name,b.name)