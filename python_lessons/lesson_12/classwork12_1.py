class Transport:
    def __init__(self, transport_brand, color, speed):
        self.brand = transport_brand
        self.color = color
        self.speed = speed

    def go(self):
        return f"{self.brand} поїхав"

    def stop(self):
        return f"{self.brand} зупинився"


class Car(Transport):
    def __str__(self):
        return f" type transport: {self.brand}, color: {self.color}, speed: {self.speed}"


class Bus(Transport):
    def __str__(self):
        return f" type transport: {self.brand}, color: {self.color}, speed: {self.speed}"


car1 = Car("subaru", "black", 160)
car2 = Car("mitsubisi", "green", 90)
bus1 = Bus("Mersedess", "white", 50)
bus2 = Bus("mitsubisi", "green", 60)
print(car1)
print(car2)
print(bus1)
print(bus2)
print(bus1.go())
print(bus2.stop())