import logging


def is_called(func):
    
    def wrapper(*args, **kwargs):
        logging.info(f"{func.__name__} is called")
        res = func(*args, **kwargs)
        logging.info(f"{func.__name__}is executed with args:{args} and kwargs: {kwargs}")
        return res
    return wrapper

class Donut:
    """Donut is """
    def __init__(self, name: str, price: float, production_cost: float, topping=None, filled=False) -> float:
        self.name = name
        self.price = price
        self.prod_cost = production_cost
        self.topping = topping # glassatura
        self.filled = filled # ripieno
    
    @is_called    
    def calculate_profit(self):
        """returns the profit of the donut's seller"""
        return self.price - self.prod_cost
    
    @is_called 
    def apply_discount(self, percent):
        """returns the discuont you applied"""
        discount = self.price * (percent / 100)
        self.price = round(self.price - discount, 2)
        
    @is_called 
    def sell(self, quantity=1):
        """returns the sold qunatity of Donut"""
        if quantity > self.stock_quantity:# raise an exception if a donut is not avaible
            raise ValueError("Not enough stock available.")
        self.stock_quantity -= quantity
        return quantity * self.price
    
    @is_called 
    def is_available(self):
        """return True if a Donut is avaible, False otherwise"""
        return self.stock_quantity > 0
    
    @is_called 
    def __str__(self):
        """returns a human readable of the donut"""
        return f"Donut ({'Filled' if self.filled else 'Classic'}) - €{self.price} x {self.stock_quantity} left"
