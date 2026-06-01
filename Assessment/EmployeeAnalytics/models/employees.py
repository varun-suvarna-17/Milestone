class Employee:
    def __init__(self, employee_id, name, department, salary, join_date, manager_id=None):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.join_date = join_date
        self.manager_id = manager_id