# 4. Constructor __init__()
# Constructor object create hote hi automatically run hota hai.

class Laptop:
    def __init__(self,name,price):
        self.name=name
        self.price=price


    def show_details(self):
        print(self.name)
        print(self.price)

Laptop1=Laptop("DELL",450000)
Laptop1.show_details()
    