class Student1:
    def __init__(self, name, age, institute):
        self.name = name
        self.age = age
        self.institute = institute
    def Study(self):
        print(f"{self.name} Studies")
s1 = Student1("Abhi", 21, "Kosnest")
print(f"{s1.name} {s1.age} {s1.institute}")
s1.Study()
s2 = Student1("Anu", 21, "Kodnest")
print(f"{s2.name} {s2.age} {s2.institute}")
s2.Study()