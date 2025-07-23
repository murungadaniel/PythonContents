class Item_1:
    def __init__(self,name):
        self.name = name
    def calculate_total_price(self,x,y):
        return x*y


item3 = Item_1("Phone")
print(item3.name)