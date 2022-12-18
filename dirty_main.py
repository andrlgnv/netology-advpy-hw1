from application.salary import *
from application.people import *
from datetime import *
from flask_blacklist import *

if __name__ == '__main__':
    print(datetime.now())
    calculate_salary()
    get_employees()
