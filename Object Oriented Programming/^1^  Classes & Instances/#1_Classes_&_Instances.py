
# Empty Class
class Student:
    pass

# Unique Instances of Class
std_1 = Student()
std_2 = Student()

# Another Class
class Employee:

    # The init method
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Anisha', 'Katiyar', 75000)
emp_2 = Employee('Test', 'Employee', 50000)

# 2 ways of printing fullname shown here
print(emp_1.fullname())
print(Employee.fullname(emp_2))
