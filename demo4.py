from demo2 import emp
class emp:
    def __init__(self, name,lname,salary):
        self.name = name
        self.lname = lname
        self.salary = salary


a = emp('a','jack',4000)
b = emp('b','son',2000)
c = emp('c','abc',1400)

# a.name = 'a'
# a.lname = 'jack'
# a.salary = 4000
#
# b.name = 'b'
# b.lname = 'son'
# b.salary = 1000
#
# c.name = 'a'
# c.lname = 'abc'
# c.salary = 2000

print(a.lname,b.lname,a.salary)
print(a.salary, b.salary)


