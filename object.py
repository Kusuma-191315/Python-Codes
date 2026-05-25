class Mentor:
    def define_states(self):
        self.name = "kusuma"
        self.tech = "python"
        self.age = 21
    def teach(self):
        print("Mentor teaches")
    def groom(self):
        print("Mentor Grooms")
m = Mentor()
m.teach()
m.groom()
m.define_states()
print(f"name:{m.name}")
print(f"age: {m.age}")
print(f"tech: {m.tech}")