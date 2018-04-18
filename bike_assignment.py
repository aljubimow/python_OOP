class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print "The bike's price is $" + str(self.price) 
        print "The bike's maximum speed is " + str(self.max_speed) + "mph" 
        print "The bike's total miles are " + str(self.miles)
    
    def ride(self):
        print "Riding"
        self.miles += 10
    
    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5
        return self

bike1 = Bike(200, 25)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()
bike2 = Bike(1000, 21)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
