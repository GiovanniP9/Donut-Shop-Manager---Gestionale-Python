import logging


def is_called(func):
    
    def wrapper(*args, **kwargs):
        logging.info(f"{func.__name__} is called")
        res = func(*args, **kwargs)
        logging.info(f"{func.__name__}is executed with args:{args} and kwargs: {kwargs}")
        return res
    return wrapper


class Donut:
    """Donut represents a real donut you can buy in a store"""
    def __init__(self, name: str, sale_price: float, production_cost: float) -> float:
        self.name = name
        self.price = sale_price
        self.prod_cost = production_cost
        
    @is_called    
    def calculate_profit(self):
        return self.price - self.prod_cost

#CREAZIONE DELLA CLASSE FABBRICA
class store:
    def __init__(self): # Inizializza l'inventario e il profitto totale
        self.inventory = {}
        self.total_profit = 0
    
    # Metodo per aggiungere un prodotto all'inventario
    def add_product(self, product, quantity):
        if product in self.inventory:
            self.inventory[product] += quantity
        else:
            self.inventory[product] = quantity
        print(f"Added {quantity} of {product} to inventory.")
        
    # Metodo per vendere un prodotto
    def sell_product(self, product_name, quantity):
        if product_name in self.inventory and self.inventory[product_name] >= quantity:
            product = self.inventory[product_name] # product lo metti come chiave
            self.inventory[product_name] -= quantity # Aggiorna la quantità in inventario
            profit = product.calculate_profit() * quantity # Calcola il profitto
            self.total_profit += profit # Aggiungi il profitto totale
            print(f"sold {quantity} of {product}. Profit: {profit}.") 
        else:
            print("Product not available or insufficient quantity.") 
    
    # metodo per vedere i prodotti in inventario        
    def show_inventory(self):
        print("Inventory:")
        for product, quantity in self.inventory.items():
            print(f"{product}: {quantity} units")
        else:
            print("Inventory is empty.")
    # Metodo per vedere il profitto totale
    def show_profit(self):
        print(f"Total profit: {self.total_profit}")
    
    
        