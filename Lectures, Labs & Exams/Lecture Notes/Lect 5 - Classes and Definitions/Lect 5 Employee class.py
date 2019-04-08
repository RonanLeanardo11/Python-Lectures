class employee:
    name = "Unknown"
    employeeID = "Unknown"
    deptSalary = "Unknown"

emp1 = employee()
emp2 = employee()

# print(employee)
# print(emp1)
# print(emp2)

emp1.name = "Ronan Breen"
emp1.employeeID = 6378
emp1.deptSalary = 40000

emp2.name = "Tom Jones"
emp2.employeeID = 900
emp2.deptSalary = 30000

print("{0:<15} {1:<15} {2:<15}".format("Name", "ID", "Salary"))
print("--------------------------------------")
print("{0:<15} {1:<15} {2:<15}".format(emp1.name,emp1.employeeID,emp1.deptSalary))
print("{0:<15} {1:<15} {2:<15}".format(emp2.name,emp2.employeeID,emp2.deptSalary))