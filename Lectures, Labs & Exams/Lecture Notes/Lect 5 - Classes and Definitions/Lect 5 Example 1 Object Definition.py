class employee:
    name = "Unknown"
    employeeID = "Unknown"
    deptSalary = "Unknown"

    # Definition - note the indentation
    def empMyPrint(self): # have to pass argument in i.e. self
        print("**************************************")
        print("********** Employee Details **********")
        print("{0:<15} {1:<15} {2:<15}".format("Name", "ID", "Salary"))
        print("**************************************")
        print("{0:<15} {1:<15} {2:<15}".format(self.name,self.employeeID,self.deptSalary))

myEmployee = employee()
myEmployee1 = employee()

myEmployee.name = "Ronan Breen"
myEmployee.employeeID = 6378
myEmployee.deptSalary = 60000

myEmployee1.name = "Tom Jsmes"
myEmployee1.employeeID = 698
myEmployee1.deptSalary = 89000

myEmployee.empMyPrint()
myEmployee1.empMyPrint()