class Employee:
    """Common base class for all employees"""
    empCount = 0 #variabila de clasa pt nr total al angajatilor

    def __init__(self, name, salary):
        # variabile petru a stoca detaliile angajatului
        self.name = name
        self.salary = salary
        self.tasks = {} #dictionar pentru stocarea sarcinilor angajatilor
        Employee.empCount += 1 #incrementare nr angajati cand se creeaza un nou angajat

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self): #afiseaza doar salariul angajatului
        print( " Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1 #decrementarea nr lui de angajati la stergerea unui angajat

    def update_salary(self, new_salary): #actualizeaza salariul angajatului
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"): #modifica statusul unei sarcini sau adauga o sarcina noua
        self.tasks[task_name]=status

    def display_task(self, status):   #afiseaza sarcinile cu un anumit status
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee): #subclasa clasei employee

    mgr_count = 0 #variabila de clasa pt nr total al managerilor

    def __init__(self, name, salary, departament):
        super().__init__(name, salary)
        self.departament = f"B04_{departament}" #include codul departamentului in numele departamentului
        Manager.mgr_count+=1    #incrementare nr manageri cand se creeaza un nou manager

    def display_employee(self):  #suprascrie metoda de afisare pt a arata doar salariul managerului 
        print("Name : ", self.salary)

    def display_mgr_count(self):   #afiseaza nr ul total de manageri
        print(f"Total number of manager(s) is {Manager.mgr_count}")

# X = 7   ,X % 3=1
# Y = 11  ,Y/3=3
#creeaza instantele clasei employee
Employee1 = Employee("Stefania", 5500)
Employee2 = Employee("Luca", 4800)
Employee3 = Employee("Serban", 6000)

#afiseaza detaliile angajatilor
Employee1.display_employee()
Employee2.display_employee()
Employee3.display_employee()

#afiseaza nr ul total de angajati
Employee3.display_emp_count()
#creeaza instante ale clasei manager
ManagerI= []

Manager1 = Manager("Roberta", 8400, "departament_a")
ManagerI.append(Manager1)
Manager2 = Manager("Beatrice", 6800, "departament_b")
ManagerI.append(Manager2)
Manager3 = Manager("Marius", 9000,"departament_c")
ManagerI.append(Manager3)

#afiseaza detaliile managerilor
for i in ManagerI:
    i.display_employee()
#afiseaza nr ul total de angajati
ManagerI[0].display_emp_count()
#afiseaza nr ul total de manageri
ManagerI[0].display_mgr_count()


