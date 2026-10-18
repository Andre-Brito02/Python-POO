class ListEmployees:
    def __init__(self, id:int, name:str, salary:float):
        self._id = id
        self._name = name
        self._salary = salary

    @property
    def id(self):
        return self._id

    def increase_salary(self, percentage:float):
        self._salary += self._salary*percentage / 100.0

    def __str__(self):
        return f"{self._id}, {self._name}, {self._salary:.2f}"

lista_de_funcionarios = []
qtd_funcionarios = int(input("How many employees will be registered? "))

for i in range(qtd_funcionarios):
    print(f"\nEmployee #{i+1}:")
    while True:
        id = int(input("Id: "))
        
        # Cria uma lista rápida contendo apenas os IDs já registrados
        ids_existentes = [emp.id for emp in lista_de_funcionarios]
        
        if id in ids_existentes:
            print("This id is already registered!")
        else:
            break # O ID é único, sai do loop de validação
    name = input("Name: ")
    salary = float(input("Salary: "))

    emp = ListEmployees(id, name, salary)
    lista_de_funcionarios.append(emp)


id = int(input("\nEnter the employee id that will have salary increase: "))
achou_id = False

for emp in lista_de_funcionarios:
    if id == emp.id:
        percentage = float(input("Enter the percentage: "))
        emp.increase_salary(percentage)
        achou_id = True
        break

if not achou_id:
    print("This id does not exist")

print("\nList of employees: ")
for func in lista_de_funcionarios:
    print(func)
