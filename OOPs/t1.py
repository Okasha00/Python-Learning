
# . Your Practice
# Ek Mobile class banao:
# 1. Constructor mein name aur price receive karo.
# 2. Dono values self ke through save karo.
# 3. show_details() method banao.
# 4. Object banao: Samsung, 50000.
# 5. Details print karo.

class mobile:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def show_details(self):
        print(self.name)
        print(self.price)

mob1=mobile("Iphone-SE",32000)
mob1.show_details()
