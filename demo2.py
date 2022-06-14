class emp:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    @staticmethod
    def open(day):
        if day == 'sunday':
            print('close')
        else:
            print('open')

print(emp.open('sunday'))

# a = emp('a','jackson',4000)
# b = emp('b','jack',3000)
# c = emp('c','son',2500)
#
#
# print(a.fname,a.lname,a.salary)
# print(b.fname,b.lname,b.salary)



# class programer(emp):
#     def __init__(self,fname,lname,salary,exp,pl):
#         super().__init__(fname,lname,salary)
#         self.exp = exp
#         self.pl = pl
#
#
# a = programer('bhim','jackson', 4000,5,'python')
#
# print(a.fname,a.exp)