from tabulate import tabulate
from Assessment.EmployeeAnalytics.sql.schema import create_table, insert_data
from utils.logger import logger
from db.dbManager import DatabaseManager
from Assessment.EmployeeAnalytics.controller.analyser import PerformanceAnalyzer
from utils.exceptions import DataNotFoundException

def display(title, headers, results):
    if not results:
        raise DataNotFoundException("No data found to display")

    print("\n" + title)
    print(tabulate(results, headers=headers, tablefmt="grid"))

def main():
    db_manager = DatabaseManager()
    cursor = db_manager.connect()

    if not cursor:
        logger.error("Program stopped because database cursorection failed")
        return
    analyzer = PerformanceAnalyzer(cursor)

    try:
        create_table(cursor)
        insert_data(cursor)
        db_manager.commit()
        print("Tables created and data inserted successfully")
        
        while True:
            print()
            print("BUSINESS ANALYTICS SYSTEM")
            print("1. Salary Rank within Departments")
            print("2. Performance Trend Analysis")
            print("3. Employee Hierarchy")
            print("4. Top Performers")
            print("5. Exit")
            choice = int(input("Enter your choice (1-5): "))

            match choice:
                case 1 :
                    header, results = analyzer.salary_rank()
                    display("Salary Rank within Departments:",header,results)
                    continue

                case 2:
                    header, results = analyzer.performance_trend()
                    display("Performance Trend Analysis:",header,results)
                    continue

                case 3:
                    header, results = analyzer.employee_hierarchy()
                    display("Employee Hierarchy:" ,header,results)
                    continue

                case 4:
                    header, results = analyzer.top_performers()
                    display("Top Performers:" ,header,results)
                    continue 

                case 5:
                    print("Exiting the program....")
                    break

                case _:
                    print("Invalid choice. Please select a number between 1 and 5.")
                    continue

    except Exception as e:
        logger.error(f"Error in main function: {e}")
        print("Error:", e)

    else:
        logger.info("Main function executed successfully")

    finally:
        db_manager.close()

if __name__ == "__main__":
    main()