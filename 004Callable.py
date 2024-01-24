

class College:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    

c = College(name="NSEC", code=109)
print(f"Class is callable or not ? {callable(College)}")
print(f"Object is callable or not ? {callable(c)}")

# - So class is callable by default but object is not callable by default

class Student:
    def __init__(self, name, department):
        self.name = name
        self.department = department
    
    def __call__(self):
        print("Student class is callable")

s = Student(name="Sukriti", department="ECE")

print(f"Class is callable or not ? {callable(Student)}")
print(f"Object is callable or not ? {callable(s)}")

# - So we call __call__ to make the object callable

