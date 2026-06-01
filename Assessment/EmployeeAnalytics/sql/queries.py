

def salary_rank(cursor):
    cursor.execute("""
        SELECT NAME, DEPARTMENT, SALARY,
               RANK() OVER (PARTITION BY DEPARTMENT ORDER BY SALARY DESC) AS Salary_Rank
        FROM employees;
    """)
    return (["NAME", "DEPARTMENT", "SALARY", "SALARY_RANK"], cursor.fetchall())

def performance_trend(cursor):
    cursor.execute("""
      SELECT EMPLOYEE_ID, REVIEW_DATE, RATING,
                LAG(RATING) OVER (PARTITION BY EMPLOYEE_ID ORDER BY REVIEW_DATE) AS Previous_Rating,
                RATING - LAG(RATING) OVER (PARTITION BY EMPLOYEE_ID ORDER BY REVIEW_DATE) AS Rating_Change
                FROM performance;
    """)
    return (["EMPLOYEE_ID", "REVIEW_DATE", "RATING", "PREVIOUS_RATING", "RATING_CHANGE"], cursor.fetchall())
    
def employee_hierarchy(cursor):
    cursor.execute("""
      WITH RECURSIVE emp_hierarchy AS(
      SELECT EMPLOYEE_ID, NAME , MANAGER_ID
      FROM employees
      WHERE manager_id IS NULL
                   
      UNION ALL
                   
      SELECT e.employee_id, e.name, e.manager_id
      FROM employees e JOIN emp_hierarchy 
      ON e.manager_id = emp_hierarchy.employee_id
      ORDER BY MANAGER_ID
    )
    SELECT *
    FROM emp_hierarchy;
    """)
    return (["EMPLOYEE_ID", "NAME", "MANAGER_ID"], cursor.fetchall())

def top_performers(cursor):
    cursor.execute("""
        WITH avg_rating AS (
    SELECT e.NAME, e.DEPARTMENT, ROUND(AVG(p.RATING), 2) AS AVG_RATING
    FROM employees e JOIN performance p
    ON e.EMPLOYEE_ID = p.EMPLOYEE_ID
    GROUP BY e.EMPLOYEE_ID
    )
    SELECT * FROM avg_rating
    WHERE AVG_RATING = (
        SELECT MAX(a.AVG_RATING)
        FROM avg_rating a
        WHERE a.DEPARTMENT = avg_rating.DEPARTMENT
    );
    """)
    return (["NAME", "DEPARTMENT", "AVG_RATING"], cursor.fetchall())