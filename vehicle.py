class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
        
    def show_details(self):
        print("I am Vehicle")
        print("Mileage of vehicle: ",self.mileage)
        print("Cost of vehicle: ",self.cost)
        
class Car(Vehicle):
    def show_car_details(self):
        print("I am a car")

c1=Car(2200,700)
c1.show_details()
c1.show_car_details()