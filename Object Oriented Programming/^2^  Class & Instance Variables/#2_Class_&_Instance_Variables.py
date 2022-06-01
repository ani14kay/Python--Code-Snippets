class Employee:

    #Class Variables
    num_of_emps = 0
    raise_amt = 1.07
    
    # The init method
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
emp_1 = Employee('Anisha', 'Katiyar', 75000)
emp_2 = Employee('Test', 'Employee', 50000)

# Printing Results to identify differences
print(Employee.num_of_emps)

Employee.raise_amt=1.11

print(emp_2.__dict__)
emp_2.raise_amt = 1.05
print(emp_2.__dict__)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)