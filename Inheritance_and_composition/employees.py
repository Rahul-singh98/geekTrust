from representations import AsDictionaryMixin
from productivity import ProductivitySystem
from hr import PayrollSystem
from contacts import AddressBook


class EmployeeDatabase:
    def __init__(self):
        self._employees = [
            {
                "id"   : 1,
                'name' : 'Mary Poppins',
                'role' : 'manager'
            },
            {
                "id"   : 2,
                'name' : 'John Smith',
                'role' : 'secretary'
            },
            {
                "id"   : 3,
                'name' : 'Kevin Bacon',
                'role' : 'sales'
            },
            {
                "id"   : 4,
                'name' : 'Jane Doe',
                'role' : 'factory'
            },
            {
                "id"   : 5,
                'name' : 'Robin Williams',
                'role' : 'secretary'
            },
        ]
        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_addressess = AddressBook()

    @property
    def employees(self):
        return [self._create_employee(**data) for data in self._employees]

    def _create_employee(self, id, name, role):
        address = self.employee_addressess.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)

# from hr import (
#     SalaryPolicy,
#     HourlyPolicy,
#     CommissionPolicy
# )

# from productivity import (
#     ManagerRole,
#     SecretaryRole,
#     SalesRole,
#     FactoryRole
# )

class Employee(AsDictionaryMixin):
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self._role = role
        self._payroll = payroll

    def work(self, hours):
        duties = self._role.perform_duties(hours)
        print(f"Employee {self.id} - {self.name}:")
        print(f"- {duties}")
        print('')
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll()


# class SalaryEmployee(Employee):
#     def __init__(self, id, name, weekly_salary):
#         super().__init__(id, name)
#         self.weekly_salary = weekly_salary

#     def calculate_payroll(self):
#         return self.weekly_salary

# class HourlyEmployee(Employee):
#     def __init__(self, id, name, hours_worked, hours_rate):
#         super().__init__(id, name)
#         self.hours_worked = hours_worked
#         self.hours_rate = hours_rate

#     def calculate_payroll(self):
#         return self.hours_rate * self.hours_worked

# class CommissionEmployee(SalaryEmployee):
#     def __init__(self, id, name, weekly_salary, commission):
#         super().__init__(id, name, weekly_salary)
#         self.commission = commission

#     def calculate_payroll(self):
#         fixed = super().calculate_payroll()
#         return fixed + self.commission

# class Manager(Employee, ManagerRole, SalaryPolicy):
#     def __init__(self, id, name, weekly_salary):
#         SalaryPolicy.__init__(self, weekly_salary)
#         super().__init__(id,name)

# class Secretary(Employee, SecretaryRole, SalaryPolicy):
#     def __init__(self, id, name, weekly_salary):
#         SalaryPolicy.__init__(self, weekly_salary)
#         super().__init__(id,name)

# class SalesPerson(Employee, SalesRole, CommissionPolicy):
#     def __init__(self, id, name, weekly_salary, commission):
#         CommissionPolicy.__init__(self, weekly_salary, commission)
#         super().__init__(id,name)

# class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
#     def __init__(self, id, name, hours_worked, hours_rate):
#         HourlyPolicy.__init__(self, hours_worked, hours_rate)
#         super().__init__(id,name)

# class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
#     def __init__(self, id, name, hours_worked, hours_rate):
#         HourlyPolicy.__init__(self, hours_worked, hours_rate)
#         super().__init__(id, name)

employee_database = EmployeeDatabase()