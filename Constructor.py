class Mentor:
    def __init__(self, name, tech, age):#we define constructor using dunder init means __init__ ans self is a keyword which accepts all the parameter by default 
        self.name = name
        self.tech = tech
        self.age = age
    def teach(self):
        print(f"{self.name} teaches")
    def groom(self):
        print(f"{self.name} grooms")
m1 = Mentor("Gamana","python",23)
print(f"{m1.name}, {m1.tech}, {m1.age}")
m1.teach()
m1.groom()
m2 = Mentor("Nikitha", "Java", 24)
print(f"{m2.name}, {m2.tech}, {m2.age}")
m2.teach()
m2.groom()
m3 = Mentor("Sandesh", "Software Tetsing", 29)
print(f"{m3.name}, {m3.tech}, {m3.age}")
m3.teach()
m3.groom()

#--------------------------------------------using input()--------------------------------------------------------------

class Mentor:
    def __init__(self, name, tech, salary):
        self.name = name
        self.tech = tech
        self.salary = salary

    def teach(self):
        print(f"{self.name} teaches {self.tech}")

    def groom(self):
        print(f"{self.name} grooms students")
              
n = input("Enter Mentors Name : ")
t = input("Enter Mentors Tech : ")
s = input("Enter Mentors Salary : ")

m = Mentor(n, t, s)
print(f"{m.name} {m.tech} {m.salary}")
m.teach()
m.groom()

n = input("Enter Mentors Name : ")
s = input("Enter Mentors Tech : ")
t = input("Enter Mentors Salary : ")

m1 = Mentor(n, t, s)
print(f"{m1.name} {m1.tech} {m1.salary}")
m1.teach()
m1.groom()

n = input("Enter Mentors Name : ")
s = input("Enter Mentors Tech : ")
t = input("Enter Mentors Salary : ")

m2 = Mentor(n, t, s)
print(f"{m2.name} {m2.tech} {m2.salary}")
m2.teach()Gaman
m2.groom()

#------------- with input() for employee ----------------------------

class Employee:
    def __init__(self, name, role, age, salary):
        self.name = name
        self.role =role
        self.age = age
        self.salary = salary

    def project(self):
        print(f"{self.name} works on {self.role} projects")

    def work(self):
        print(f"{self.name} is working with a salary of {self.salary}")
              
n = input("Enter Employee Name : ")
r = input("Enter Employee role : ")
a = input("Enter Employee age : ")
s = input("Enter Employee Salary : ")

e = Employee(n, r, a, s)
print(f"{e.name} {e.role}  {e.age} {e.salary}")
e.project()
e.work()

n = input("Enter Employee Name : ")
r = input("Enter Employee role : ")
a = input("Enter Employee age : ")
s = input("Enter Employee Salary : ")

e2 = Employee(n, r, a, s)
print(f"{e2.name} {e2.role}  {e2.age} {e2.salary}")
e2.project()
e2.work()

n = input("Enter Employee Name : ")
r = input("Enter Employee role : ")
a = input("Enter Employee age : ")
s = input("Enter Employee Salary : ")

e3 = Employee(n, r, a, s)
print(f"{e3.name} {e3.role}  {e3.age} {e3.salary}")
e3.project()
e3.work()





