
from utils.exceptions import ManagerDeletionException, EmployeeNotFoundException


class crud_operation():
    def __init__(self, cursor):
        self.cursor = cursor
    
    def add_employee(self, employee):
        self.cursor.execute("""
            INSERT INTO employees
            (EMPLOYEE_ID, NAME, DEPARTMENT, SALARY, JOIN_DATE, MANAGER_ID)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            employee.employee_id,
            employee.name,
            employee.department,
            employee.salary,
            employee.join_date,
            employee.manager_id
        ))

    def delete_employee(self, employee_id):
        self.cursor.execute(
            """SELECT * FROM employees WHERE employee_id = ?""", (employee_id,)
        )
        employee = self.cursor.fetchone()
        if not employee:
            raise EmployeeNotFoundException(
                f"Employee {employee_id} does not exist."
            )
        
        self.cursor.execute(
            """SELECT COUNT(*) FROM employees WHERE manager_id = ?""", (employee_id,)
        )
        count = self.cursor.fetchone()[0]
        if count > 0:
            raise ManagerDeletionException(
                f"Cannot delete employee {employee_id}. "
                "Other employees report to this manager."
            )
        
        self.cursor.execute(""" DELETE FROM employees WHERE EMPLOYEE_ID = ?
""", (employee_id,))