import math

class Item:
    def __init__(self, name:str, brand:str, 
                 quantity:int, cost:float, markup:int, 
                 price:float, min_quantity:int, max_quantity:int, 
                 vendor:str):
       self.name=name
       self.brand=brand
       self.quant=quantity
       self.cost=cost
       self.markup=markup
       self.price=price
       self.min_=min_quantity
       self.max_=max_quantity
       self.vendor=vendor

    def add_new_item(self):
        pass
    def update_item(self):
        pass
    def rem_item(self):
        pass
    def price_adjustment(self, cost, markup):
        markup_decimal = self.markup / 100.0
        markup_amount = self.cost * markup_decimal
        unmodified_price = markup_amount + cost
        if unmodified_price % 1 != 0.99:
            self.price = math.floor(unmodified_price) + 0.99
    def update_item_quant(self):
        pass
