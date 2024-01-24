"""
- Nested class is a class defined within another class.
- Scope is limited to the outer class, accessible by its name.
- Used for encapsulation, grouping related classes.
- Outer class can access nested class members, but not vice versa.
- Instances of nested class can be created within outer class methods.
- Nested class has its own namespace, can have attributes and methods.
- Useful when a class is closely related and not intended for external use.
- Visibility of nested class outside is limited for encapsulation.
- Common pattern: Factories or helper classes as nested classes.
- Contributes to readable and organized code when a clear relationship exists.

"""


class University:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.colleges = []
    
    def __str__(self):
        output = ""
        output += f"University : {self.name} and Code : {self.code}\n"
        output += f"Colleges\n=================================================\n"
        for col in self.colleges:
            output += str(col)
        return output

    def addCollege(self, name, location):
        college = self.College(name, location)
        self.colleges.append(college)

    class College:
        def __init__(self, name, location):
            self.name = name
            self.location = location
        
        def __str__(self):
            return f"College : {self.name} and location : {self.location}\n"
        
university = University(name="MAKAUT", code="WB101")
university.addCollege(name="NSEC", location="Garia")
university.addCollege(name="TMSL", location="Salt Lake, Kolkata")
university.addCollege(name="JGEG", location="Jalpaiguri")
university.addCollege(name="BCROYEC", location="Durgapur")

print(university)