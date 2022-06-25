# class is like a template
class Employee:
    def __init__(self, gname, gsalary):  # constructor
        self.name = gname
        self.salary = gsalary


harry = Employee("Harry", 34)
print(harry.name)
