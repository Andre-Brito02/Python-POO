from abc import ABC, abstractmethod

class Contribuinte(ABC):
    def __init__(self, nome:str, renda_anual:float):
        self._nome = nome
        self._renda_anual = renda_anual

    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def renda_anual(self) -> float:
        return self._renda_anual

    @abstractmethod
    def tax(self):
        pass

class PessoaFisica(Contribuinte):
    def __init__(self, nome:str, renda_anual:float, gasto_saude:float):
        super().__init__(nome, renda_anual)
        self._gasto_saude = gasto_saude

    @property
    def gasto_saude(self) -> float:
        return self._gasto_saude

    def tax(self) -> float:
        imposto = 0.15 if self._renda_anual < 20000 else 0.25
        return (self._renda_anual * imposto) - (self._gasto_saude * 0.5)

class PessoaJuridica(Contribuinte):
    def __init__(self, nome:str, renda_anual:float, qtd_funcionarios:int):
        super().__init__(nome, renda_anual)
        self._qtd_funcionarios = qtd_funcionarios

    @property
    def qtd_funcionarios(self) -> int:
        return self._qtd_funcionarios

    def tax(self) -> float:
        imposto = 0.16 if self._qtd_funcionarios < 10 else 0.14
        return self._renda_anual * imposto

qtd_contribuintes = int(input("Enter the number of tax payers: "))
contribuintes = []

for i in range(1, qtd_contribuintes+1):
    print(f'Tax payer #{i} data:')
    choice = input('Individual or company (i/c)? ').lower()

    nome = input("Name: ")
    renda_anual = float(input("Anual income: "))

    match choice:
        case 'i':
            gasto_saude = float(input("Health expenditures: "))
            pf = PessoaFisica(nome, renda_anual, gasto_saude)
            contribuintes.append(pf)
        case 'c':
            qtd_funcionarios = int(input("Number of employees: "))
            pj = PessoaJuridica(nome, renda_anual, qtd_funcionarios)
            contribuintes.append(pj)

total_imposto = 0.0
print("\nTAXES PAID:")
for dados in contribuintes:
    imposto_contribuinte = dados.tax()
    total_imposto += imposto_contribuinte
    print(f'{dados.nome}: $ {imposto_contribuinte:.2f}')

print(f'\nTOTAL TAXES: $ {total_imposto:.2f}')