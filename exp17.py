#Aim:Online Shopping System
#Name:Khan Tasneem
#Date:15-04-2026
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def update_stock(self, quantity):
        self.stock += quantity
        print(f"Stock updated. New stock of {self.name}: {self.stock}")

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class ShoppingCart:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
    
    def add_item(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.update_stock(-quantity)
            print(f"Added {quantity} of {product.name} to cart.")
        else:
            print(f"Insufficient stock for {product.name}.")
    
    def calculate_total(self):
        total = sum(product
