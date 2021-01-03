# Harry Potter Universe

class Professional:
    
    def __init__(self, name, job, salary, house):
        
        self.name = name
        self.job = job
        self.salary = salary
        self.house = house
        
    def change_job(self, job):
        self.job = job
        
    def add_bonus(self, salary):
        self.salary = int(self.salary * 1.05)

prof1 = Professional('Harry Potter', 'Auror', 200, 'Gryffindor')
prof2 = Professional('Hermione Granger', 'Law Enforcer', 225, 'Gryffindor')

print(prof1.job)
prof1.change_job('Head of Aurors')
print(prof1.job)


class Hogwarts_Emps(Professional):
    
    def __init__(self, name, job, salary, house, house_head, difficulty):
        super().__init__(self, name, job, salary, house)
        self.house_head = house_head
        self.difficulty = difficulty
        
        
         

class Heads(Professional):
    
    def __init__(self, name, job, salary, house, employees = None):
        super().__init__(self, name, job, salary, house)
        if employees is None:
            employees = []
        else:
            self.employees = employees
            
    def add_employees(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_employees(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('--> ', emp)
        
        
        