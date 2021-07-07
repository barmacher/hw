class Employee:
    emp_count = 0
    work_rate = 2

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_count(self):
        pass

    def display_employee(self):
        print(f'Моё имя {self.name}')
        print(f'Зарплата {self.salary}')

    def change_name(self,name1):
        self.name = name1


    def get_total_salary(self):
        return self.salary

p1 = Employee('Igor',20000)
p2 = Employee('Kairat',30000)

print(p1.name,p1.salary)

p1.display_employee()

p2.change_name('Vasya')
print(p2.name)


print(p1.get_total_salary())