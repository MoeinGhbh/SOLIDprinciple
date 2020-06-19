"""Let’s imagine you have a store, and you give a discount of 20% to your 
favorite customers using this class: When you decide to offer double 
the 20% discount to VIP customers. You may modify the class like this:"""

# Befor
class Discount1:
    def __init__(self,customer,price):
        self.customer=customer
        self.price=price

    def discount(self):
        if self.customer=="fav":
            return self.price * .2
        elif self.customer == "vip":
            return self.price * .4  

# after 
class Discount2:
    def __init__(self,customer,price):
        self.price=price
        self.customer=customer

    def fav_customer(self):
        return self.price * .2

class VIPcustomer(Discount1):

    def vip_customer(self):
        return super().fav_customer() * .2