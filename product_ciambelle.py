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

