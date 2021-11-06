class Car(object):

    def __init__(self, model,colour, company,speed_Limit):
        self.model = model
        self.colour = colour
        self.company = company
        self.speed_Limit = speed_Limit

    def start(self):
        print("Started")
    
    def stop(self):
        print("Stopped")

    def accelerate(self):
        print("Accelerated")

    def change_gear(self):
        print("Gear Changed")

Audi = Car("A6", "red", "Audi", 100)

print(Audi.start())
print(Audi.stop())
print(Audi.accelerate())
print(Audi.change_gear())
print(Audi.colour, Audi.model, Audi.company, Audi.speed_Limit)