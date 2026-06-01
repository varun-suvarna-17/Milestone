from sql.queries import (
    salary_rank,
    performance_trend,
    employee_hierarchy,
    top_performers
)

class PerformanceAnalyzer:
    def __init__(self, cursor):
        self.cursor = cursor

    def salary_rank(self):
        return salary_rank(self.cursor)

    def performance_trend(self):
        return performance_trend(self.cursor)

    def employee_hierarchy(self):
        return employee_hierarchy(self.cursor)

    def top_performers(self):
        return top_performers(self.cursor)