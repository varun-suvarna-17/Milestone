# Employee Performance Analytics System

## Project Overview

The Employee Performance Analytics System is a Python and SQLite-based business analytics application developed as part of the SIP Assessment. The system stores employee information, performance reviews, attendance records, and organizational hierarchy while providing analytical reports using advanced SQL concepts and Python programming techniques.

The project demonstrates the integration of:

* SQLite Database Management
* Object-Oriented Programming (OOP)
* Exception Handling
* Logging
* Window Functions
* Common Table Expressions (CTEs)
* Recursive CTEs
* Menu-Driven Application Design

---

# Project Architecture

```text
EmployeeAnalytics/
│
├── db/
│   ├── connection.py
│   └── db_manager.py
│
├── controller/
│   └── performance_analyzer.py
│
├── models/
│   └── employee.py
│
├── sql/
│   ├── schema.py
│   └── queries.py
│
├── utils/
│   ├── logger.py
│   └── exceptions.py
│
└── main.py
```

---

# Database Design

The system uses SQLite and consists of three tables:

## Employees Table

Stores employee information.

| Column      | Description                  |
| ----------- | ---------------------------- |
| EMPLOYEE_ID | Unique Employee ID           |
| NAME        | Employee Name                |
| DEPARTMENT  | Department Name              |
| SALARY      | Employee Salary              |
| JOIN_DATE   | Date of Joining              |
| MANAGER_ID  | Self-referencing foreign key |

### Self Referencing Foreign Key

The `MANAGER_ID` column references the `EMPLOYEE_ID` of another employee.

Example:

```text
Alice Johnson (CEO)
    |
    ├── Varun Suvarna
    │      ├── Rohan Shetty
    │      └── Nikhil Rao
    |
    └── Akash Salian
           └── Sanvi Kamath
```

This relationship is later used for Recursive CTE-based hierarchy generation.

---

## Performance Table

Stores employee review history.

| Column         | Description        |
| -------------- | ------------------ |
| PERFORMANCE_ID | Auto Increment ID  |
| EMPLOYEE_ID    | Employee Reference |
| RATING         | Performance Rating |
| REVIEW_DATE    | Review Date        |

Multiple reviews are stored for each employee to support trend analysis.

---

## Attendance Table

Stores employee attendance records.

| Column        | Description        |
| ------------- | ------------------ |
| ATTENDANCE_ID | Auto Increment ID  |
| EMPLOYEE_ID   | Employee Reference |
| DATE          | Attendance Date    |
| STATUS        | Present / Absent   |

---

# Object-Oriented Programming Implementation

## DatabaseManager Class

Responsible for:

* Establishing database connections
* Managing cursors
* Committing transactions
* Closing connections

Methods:

```python
connect()
commit()
close()
```

This class encapsulates all database-related operations.

---

## PerformanceAnalyzer Class

Responsible for:

* Salary Ranking Analysis
* Performance Trend Analysis
* Employee Hierarchy Generation
* Top Performer Identification
* Employee CRUD Operations

Methods:

```python
salary_rank()
performance_trend()
employee_hierarchy()
top_performers()
add_employee()
delete_employee()
```

This class acts as the controller layer of the application.

---

## Employee Class

Represents an Employee object.

Attributes:

```python
employee_id
name
department
salary
join_date
manager_id
```

The Employee class can be used to create employee objects before inserting them into the database.

---

# Analytics Features

## 1. Salary Ranking Within Departments

Uses SQL Window Functions.

```sql
RANK() OVER(
    PARTITION BY department
    ORDER BY salary DESC
)
```

Purpose:

* Compares employees only within their department.
* Assigns salary-based ranks.

Example:

```text
Engineering
-----------
Varun     Rank 1
Rohan     Rank 2
Nikhil    Rank 3
```

---

## 2. Performance Trend Analysis

Uses:

```sql
LAG()
```

Purpose:

* Retrieves previous ratings.
* Calculates rating improvements.

Example:

```text
Current Rating: 5
Previous Rating: 4
Improvement: +1
```

This helps analyze employee growth over time.

---

## 3. Employee Hierarchy

Implemented using Recursive CTE.

```sql
WITH RECURSIVE
```

Purpose:

* Generates reporting hierarchy.
* Displays employees under managers.

Example:

```text
CEO
 ├── Manager
 │    ├── Employee
 │    └── Employee
```

---

## 4. Top Performers by Department

Uses:

* CTE
* Aggregate Functions
* Correlated Subqueries

Process:

1. Calculate average rating for each employee.
2. Determine the maximum average rating within each department.
3. Display top performer(s) from every department.

---

# Exception Handling

The project uses custom exceptions for business rule validation.

## EmployeeNotFoundException

Raised when a user attempts to access or delete a non-existent employee.

## ManagerDeletionException

Raised when attempting to delete a manager who still has employees reporting under them.

Example:

```text
Cannot delete employee 2.
Other employees report to this manager.
```

This preserves hierarchy integrity.

---

# Logging

Logging is implemented using Python's logging module.

Log File:

```text
app.log
```

Tracks:

* Database Connections
* Successful Operations
* Errors
* Program Execution Flow

Example:

```text
INFO : Database connected successfully
ERROR : Employee does not exist
```

---

# User Interface

The application uses a menu-driven console interface.

```text
1. Salary Rank within Departments
2. Performance Trend Analysis
3. Employee Hierarchy
4. Top Performers
5. Add Employee
6. Delete Employee
7. Exit
```

Results are displayed in tabular format using the `tabulate` library.

---

# Technologies Used

* Python 3
* SQLite3
* Tabulate
* Logging Module
* Object-Oriented Programming
* SQL Window Functions
* Common Table Expressions (CTE)
* Recursive CTE

---

# Learning Outcomes

Through this project, the following concepts were implemented and understood:

* Database Design
* SQL Analytics
* Window Functions
* Recursive Queries
* Object-Oriented Programming
* Exception Handling
* Logging
* Modular Programming
* Business Analytics Reporting

---

# Conclusion

The Employee Performance Analytics System successfully combines Python programming and advanced SQL analytics to provide meaningful business insights. The project demonstrates practical application of database management, object-oriented design, analytical query processing, and software engineering principles in a real-world employee management scenario.
