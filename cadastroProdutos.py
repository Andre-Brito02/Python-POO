from enum import Enum
from datetime import *

class OrderStatus(Enum):
    PENDING_PAYMENT = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4

class Client:
    def __init__(self, name:str, email:str, birth_date:datetime):
        self._name = name
        self._email = email
        self._birth_date = birth_date

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def birth_date(self):
        return self._birth_date

class Product:
    def __init__(self, name:str, price:float):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

class OrderItem:
    def __init__(self, quantity:int, price:float, product:Product):
        self._quantity = quantity
        self._price = price
        self._product = product

    @property
    def quantity(self):
        return self._quantity
    
    @property
    def price(self):
        return self._price
    
    @property
    def product(self):
        return self._product

    def sub_total(self):
        return self._price * self._quantity

class Order:
    def __init__(self, moment:datetime, status:OrderStatus, client:Client):
        self._moment = moment
        self._status = status
        self._client = client
        self._items = []

    @property
    def moment(self):
        return self._moment
    
    @property
    def status(self):
        return self._status
    
    @property
    def client(self):
        return self._client
    
    @property
    def itens(self):
        return self._items

    def add_item(self, item:OrderItem):
        self._items.append(item)

    def remove_item(self, item:OrderItem):
        self._items.remove(item)

    def total(self):
        total_value = 0.0

        for item in self._items:
            total_value += item.sub_total()

        return total_value

    def __str__(self):
        resultado = (
            f"Order moment: {self.moment.strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Order status: {self.status.name}\n"
            f"Client: {self.client.name} {self.client.birth_date.strftime('%d/%m/%Y')} - {self.client.email}\n"
            f"Order items:\n"
        )

        # Concatena os itens (usar += é eficiente o suficiente em loops pequenos no Python)
        for item in self._items:
            resultado += f"{item.product.name}, ${item.price:.2f}, Quantity: {item.quantity}, Subtotal: ${item.sub_total():.2f}\n"

        # Adiciona o total
        resultado += f"Total price: ${self.total():.2f}"

        return resultado

print("Enter client data: ")
name = input("Name: ")
email = input("Email: ")
data_texto = input("Birth date (dd/MM/yyyy): ")
birth_date = datetime.strptime(data_texto, "%d/%m/%Y")
client = Client(name, email, birth_date)

print('\nEnter order data: ')
status = input("Status: ").upper()
order = Order(datetime.now(), OrderStatus[status], client)

qtd = int(input("\nHow many items to this order? "))

for i in range(qtd):
    print(f"\nEnter #{i+1} item data: ")
    product_name = input("Product Name: ")
    product_price = float(input("Product Price: "))
    product = Product(product_name, product_price)
    product_quantity = int(input("Quantity: "))
    order_item = OrderItem(product_quantity, product.price, product)

    order.add_item(order_item)

print("\nORDER SUMMARY:")
print(order)