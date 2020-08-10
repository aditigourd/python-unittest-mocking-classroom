import mysql.connector

class DbHelper:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="datagrokr",
            password="1234",
            database="employees"
        )
    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        client = self.conn.cursor()
        client.execute("select max(salary) from employees e inner join salaries s on e.emp_no=s.emp_no;")
        results = client.fetchall()
        max_salary=results[0][0]
        return max_salary

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        client = self.conn.cursor()
        client.execute("select min(salary) from employees e inner join salaries s on e.emp_no=s.emp_no;")
        results = client.fetchall()
        min_salary = results[0][0]
        return min_salary

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)