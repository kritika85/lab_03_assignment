class Emp:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def _str_(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"

def sort_employee_data(employee_list, sorting_parameter):
    if sorting_parameter == 1:
        return sorted(employee_list, key=lambda emp: emp.age)
    elif sorting_parameter == 2:
        return sorted(employee_list, key=lambda emp: emp.name)
    elif sorting_parameter == 3:
        return sorted(employee_list, key=lambda emp: emp.salary)
    else:
        raise ValueError("Wrong sorting parameter")

if _name_ == "_main_":
    employees = [
        Emp("161E90", "Raman", 41, 56000),
        Emp("161F91", "Himadri", 38, 67500),
        Emp("161F99", "Jaya", 51, 82100),
        Emp("171E20", "Tejas", 30, 55000),
        Emp("171G30", "Ajay", 45, 44000),
    ]

    print("Employee Table")
    print("Employee ID Name Age Salary (PM)")
    for employee in employees:
        print(employee)

    sorting_option = int(input("Enter sorting parameter (1. Age, 2. Name, 3. Salary): "))

    sorted_employees = sort_employee_data(employees, sorting_option)

    print("\nSorted Employee Data:")
    print("Employee ID Name Age Salary (PM)")
    for employee in sorted_employees:
        print(employee)