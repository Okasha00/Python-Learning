# Next OOP concept: Multiple Objects



class mobile:
    def __init__(self,name,price):
        self.name=name
        self.price=price


    def show(self):
        print(self.name)
        print(self.price)

m1=mobile("Phone is:S23","and price is:43000")
m2=mobile("Phone is:S32","and price is:45000")
m1.show()
m2.show()
