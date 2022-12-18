from application.salary import calculate_salary
from application.people import get_employees
import datetime
import flask_blacklist

if __name__ == '__main__':
    print(datetime.now())
    calculate_salary()
    get_employees()