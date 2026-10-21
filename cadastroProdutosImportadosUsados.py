from decimal import Decimal
from datetime import *

class Product():
    def __init__(self, name:str, price:Decimal):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price

    def price_tag(self) -> str:
        return f"{self._name} $ {self._price:.2f}"

class ImportedProduct(Product):
    def __init__(self, name, price, custom_fee):
        super().__init__(name, price)
        self._custom_fee = custom_fee

    @property
    def custom_fee(self):
        return self._custom_fee

    def total_price(self) -> Decimal:
        return self._price + self._custom_fee

    def price_tag(self) -> str:
        return f"{self._name} $ {self.total_price()} (Custom fee: $ {self._custom_fee:.2f})"

class UsedProduct(Product):
    def __init__(self, name, price, manufacture_date:datetime):
        super().__init__(name, price)
        self._manufacture_date = manufacture_date

    @property
    def manufacture_date(self):
        return self._manufacture_date

    def price_tag(self):
        return f"{self._name} (used) $ {self._price} (Manufacture date: {self._manufacture_date.strftime('%d/%m/%Y')})"

qtd = int(input("Enter the number of products: "))
products = []

for i in range(1, qtd+1):
    print(f'Product #{i} data:')
    choice = input("Common, used or imported (c/u/i)? ").lower()

    name = input("Name: ")
    price = Decimal(input("Price: "))
    
    match(choice):
        case 'c':
            products.append(Product(name, price))
        case 'u':
            data_texto = input("Manufacture date (dd/MM/yyyy): ")
            manufacture_date = datetime.strptime(data_texto, "%d/%m/%Y")
            products.append(UsedProduct(name, price, manufacture_date))
        case 'i':
            custom_fee = Decimal(input("Custom fee: "))
            products.append(ImportedProduct(name, price, custom_fee))

print('\nPRICE TAGS:')
for p in products:
    print(p.price_tag())