
def create_table(cursor):
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS employees (
            EMPLOYEE_ID INTEGER PRIMARY KEY,
            NAME         TEXT    NOT NULL,
            DEPARTMENT   TEXT    NOT NULL,
            SALARY       INTEGER    NOT NULL,
            JOIN_DATE    TEXT    NOT NULL,
            MANAGER_ID   INTEGER,
            FOREIGN KEY (MANAGER_ID) REFERENCES employees (EMPLOYEE_ID)
        )"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS performance (
            PERFORMANCE_ID     INTEGER    PRIMARY KEY   AUTOINCREMENT,
            EMPLOYEE_ID        INTEGER    NOT NULL,
            RATING             INTEGER    NOT NULL,
            REVIEW_DATE        TEXT    NOT NULL,
            FOREIGN KEY (EMPLOYEE_ID) REFERENCES employees (EMPLOYEE_ID)
        )"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS attendance (
            ATTENDANCE_ID      INTEGER    PRIMARY KEY   AUTOINCREMENT,
            EMPLOYEE_ID        INTEGER    NOT NULL,
            DATE               TEXT    NOT NULL,
            STATUS             TEXT    NOT NULL,
            FOREIGN KEY (EMPLOYEE_ID) REFERENCES employees (EMPLOYEE_ID)
        )"""
    )

def insert_data(cursor):
   employees = [
    (1, 'Alice Johnson', 'Management', 120000, '2020-01-15', None),

    (2, 'Varun Suvarna', 'Engineering', 85000, '2020-03-22', 1),
    (3, 'Rohan Shetty', 'Engineering', 78000, '2021-05-10', 2),
    (4, 'Nikhil Rao', 'Engineering', 72000, '2022-01-18', 2),

    (5, 'Akash Salian', 'HR', 60000, '2019-11-10', 1),
    (6, 'Sanvi Kamath', 'HR', 58000, '2020-02-05', 5),

    (7, 'Sanidhya Shetty', 'Sales', 75000, '2020-04-18', 1),
    (8, 'Priya Nair', 'Sales', 70000, '2021-06-20', 7),

    (9, 'Arjun Kumar', 'Finance', 80000, '2020-07-12', 1),
    (10, 'Megha Patel', 'Finance', 72000, '2021-03-08', 9)
    ]
   cursor.executemany(
        """INSERT OR IGNORE INTO employees (EMPLOYEE_ID, NAME, DEPARTMENT, SALARY, JOIN_DATE, MANAGER_ID)
           VALUES (?, ?, ?, ?, ?, ?)""",
        employees
    )

   performance = [
    (1, 2, 3, '2023-01-01'),
    (2, 2, 4, '2023-06-01'),
    (3, 2, 5, '2023-12-01'),

    (4, 3, 2, '2023-01-01'),
    (5, 3, 3, '2023-06-01'),
    (6, 3, 4, '2023-12-01'),

    (7, 4, 3, '2023-01-01'),
    (8, 4, 4, '2023-06-01'),
    (9, 4, 4, '2023-12-01'),

    (10, 5, 4, '2023-01-01'),
    (11, 5, 4, '2023-06-01'),
    (12, 5, 5, '2023-12-01'),

    (13, 6, 3, '2023-01-01'),
    (14, 6, 3, '2023-06-01'),
    (15, 6, 4, '2023-12-01'),

    (16, 7, 4, '2023-01-01'),
    (17, 7, 5, '2023-06-01'),
    (18, 7, 5, '2023-12-01'),

    (19, 8, 2, '2023-01-01'),
    (20, 8, 3, '2023-06-01'),
    (21, 8, 4, '2023-12-01'),

    (22, 9, 3, '2023-01-01'),
    (23, 9, 4, '2023-06-01'),
    (24, 9, 5, '2023-12-01'),

    (25, 10, 4, '2023-01-01'),
    (26, 10, 4, '2023-06-01'),
    (27, 10, 5, '2023-12-01')
    ]
   cursor.executemany(
        """INSERT OR IGNORE INTO performance (PERFORMANCE_ID, EMPLOYEE_ID, RATING, REVIEW_DATE)
           VALUES (?, ?, ?, ?)""",
        performance
    )

   attendance = [
    (1, 2, '2023-12-01', 'Present'),
    (2, 3, '2023-12-01', 'Present'),
    (3, 4, '2023-12-01', 'Absent'),
    (4, 5, '2023-12-01', 'Present'),
    (5, 6, '2023-12-01', 'Present'),
    (6, 7, '2023-12-01', 'Present'),
    (7, 8, '2023-12-01', 'Absent'),
    (8, 9, '2023-12-01', 'Present'),
    (9, 10, '2023-12-01', 'Present'),

    (10, 2, '2023-12-02', 'Present'),
    (11, 3, '2023-12-02', 'Present'),
    (12, 4, '2023-12-02', 'Present'),
    (13, 5, '2023-12-02', 'Absent'),
    (14, 6, '2023-12-02', 'Present'),
    (15, 7, '2023-12-02', 'Present'),
    (16, 8, '2023-12-02', 'Present'),
    (17, 9, '2023-12-02', 'Present'),
    (18, 10, '2023-12-02', 'Absent')
   ]
   cursor.executemany(
        """INSERT OR IGNORE INTO attendance (ATTENDANCE_ID, EMPLOYEE_ID, DATE, STATUS)
           VALUES (?, ?, ?, ?)""",
        attendance
    )