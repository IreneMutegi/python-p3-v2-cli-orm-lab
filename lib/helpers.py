from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# Department functions
def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)

def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(f'Department {name} not found')

def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')

def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)

def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')

def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# Employee functions
def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(f"<Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")

def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(f"<Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>") if employee else print(f"Employee {name} not found")

def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    print(f"<Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>") if employee else print(f"Employee {id_} not found")

def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = input("Enter the employee's department id: ")

    try:
        department_id = int(department_id)
        department = Department.find_by_id(department_id)

        if not department:
            raise ValueError(f"Department ID {department_id} does not exist.")
        
        employee = Employee.create(name=name, job_title=job_title, department_id=department_id)
        print(f"Success: <Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")
    except Exception as exc:
        print(f"Error creating employee: {exc}")

def update_employee():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    
    if not employee:
        print(f"Employee {id_} not found")
        return
    
    try:
        name = input(f"Enter the new name for {employee.name}: ")
        job_title = input(f"Enter the new job title for {employee.name}: ")
        department_id = input(f"Enter the new department ID for {employee.name}: ")

        department = Department.find_by_id(department_id)
        if not department:
            print(f"Department ID {department_id} does not exist.")
            return
        
        employee.name = name
        employee.job_title = job_title
        employee.department_id = department_id

        employee.update()
        print(f"Success: <Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")
    except Exception as exc:
        print(f"Error updating employee: {exc}")

def delete_employee():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    
    if not employee:
        print(f"Employee {id_} not found")
        return
    
    try:
        employee.delete()
        print(f"Employee {id_} deleted")
    except Exception as exc:
        print(f"Error deleting employee: {exc}")

def list_department_employees():
    department_id = input("Enter the department's id: ")
    department = Department.find_by_id(department_id)
    
    if not department:
        print(f"Department {department_id} not found")
        return
    
    employees = department.employees()
    if employees:
        for employee in employees:
            print(f"<Employee {employee.id}: {employee.name}, {employee.job_title}, Department ID: {employee.department_id}>")
    else:
        print(f"No employees found in department {department_id}")
