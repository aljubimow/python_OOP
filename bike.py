#bike assignment
class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayinfo(self):
        print ("The bike costs $" + str(self.price))
        print ("The bike has a maximum speed of " + str(self.max_speed) +" mph")
        print ("The bike has a total mileage of " + str(self.miles) +" miles")
        return self

    def ride(self):
        print ("Riding")
        self.miles +=10
        return self
    
    def reverse(self):
        print ("Reversing")
        if self.miles >=5:
            self.miles -=5
        else:
            self.miles = 0
        return self

bike1 = Bike(200,25)
print bike1.ride().ride().ride().reverse().displayinfo()
bike2 = Bike(999,54)
print bike2.ride().ride().reverse().reverse().displayinfo()
bike3 = Bike(4999,15)
print bike3.reverse().reverse().reverse().displayinfo()
