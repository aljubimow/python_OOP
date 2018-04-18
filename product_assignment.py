class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"    
        return self

    def add_tax(self,myTax):
        tax = myTax
        self.price = self.price + (self.price * tax)
        return self

    def product_return(self, myReason):
        reason = myReason
        if reason == 'defective':
            self.status = reason
            self.price = 0
        elif reason == 'in box like new':
            self.status = 'for sale'
        elif reason == 'opened':
            self.status = 'used'
            self.price = self.price - (self.price * .145)

    def displayInfo(self):
        print "Price: " + str(self.price)
        print "Item Name: " + self.item_name
        print "Weight: " + self.weight
        print "Brand: " + self.brand
        print "Status: " + self.status
        return self

prod1 = Product(100, "Apple iPhone", "2lbs", "Apple")

prod1.sell()
prod1.add_tax(.1)
prod1.displayInfo()