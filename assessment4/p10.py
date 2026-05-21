# 10. Shop Class

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        print(self.products)

s = Shop()
s.add_product("Mobile")
s.add_product("Laptop")
s.show_products()