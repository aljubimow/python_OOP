class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price >= 10000:
            self.tax = 0.15
        else: 
            self.tax = 0.12
        self.displayInfo()
    
    def displayInfo(self):
        print "Price: $" + str(self.price) 
        print "Speed:" + str(self.speed) + "mph" 
        if self.fuel == 100:
            print "Fuel: full"
        if self.fuel in range (75,99):
            print "Fuel: kinda full"
        if self.fuel in range (50,74):
            print "Fuel: more than half"
        if self.fuel in range (25,49):
            print "Fuel: less than half"
        if self.fuel in range (1,24):
            print "Fuel: almost empty"
        if self.fuel == 0:
            print "Fuel: empty"
        print "Mileage:" + str(self.mileage) + "mpg"
        print "Tax:" + str(self.tax)
        return self


car1 = Car(199989.84, 103, 0, 15000)
car2 = Car(8999, 123, 30, 20000)
car3 = Car(19900, 82, 79, 35000)
car4 = Car(100, 14, 80, 1000)
car5 = Car(103040.43, 100, 65, 35000)
car6 = Car(35499.95, 1, 75, 100000)