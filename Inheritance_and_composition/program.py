# from productivity import ProductivitySystem
# from  hr import HourlyPolicy, PayrollSystem
# from employees import EmployeeDatabase
# # import contacts 

# payroll_system = PayrollSystem()
# productivity_system = ProductivitySystem()
# employee_database = EmployeeDatabase()
# employees = employee_database.employees
# manager = employees[0]
# manager.payroll = HourlyPolicy(55)

# productivity_system.track(employees, 40)
# payroll_system.calculate_payroll(employees)


# # manager = employees.Manager(1, "Marry Poppins", 3000)
# # manager.address = contacts.Address(
# #     "121 Admin Rd.",
# #     "Concord",
# #     "NH",
# #     "03301"
# # )

# # secretary = employees.Secretary(2, "John Smith", 1500)
# # secretary.address = contacts.Address(
# #     "67 Paperwork Ave.",
# #     "Manchester",
# #     "NH",
# #     "03101"
# # )
# # sales_guy = employees.SalesPerson(3, "Kevin Bacon", 1000, 2500)
# # factory_worker = employees.FactoryWorker(4, "Jane Doe", 40, 15)
# # temporary_secretary = employees.TemporarySecretary(5, "Robin Williams", 40, 9)

# # _employees = [
# #     manager,
# #     secretary,
# #     sales_guy,
# #     factory_worker,
# #     temporary_secretary
# # ]

# # payroll_system = hr.PayrollSystem()
# # productivity_system = ProductivitySystem()
# # productivity_system.track(_employees, 40)
# # payroll_system.calculate_payroll(_employees)

import json
# from employees import EmployeeDatabase

from hr import calculate_payroll
from productivity import track
from employees import employee_database, Employee

def print_dict(d):
    print(json.dumps(d, indent=2))

employees = employee_database.employees

track(employees, 40)
calculate_payroll(employees)

temp_secretary = Employee(5)
print("Temporary Secretary")
print_dict(temp_secretary.to_dict())