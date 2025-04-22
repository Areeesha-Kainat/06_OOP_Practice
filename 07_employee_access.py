#  Access Level: Classified


class Employee:
    def __init__(self):
        self.name = "John"           # Public
        self._salary = 50000         # Protected
        self.__ssn = "123-45-6789"   # Private

emp = Employee()
print(emp.name)
print(emp._salary)
try:
    print(emp.__ssn)
except AttributeError:
    print("Private attribute cannot be accessed directly.")
