# Base class: Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._mileage = 0  # Encapsulation: Protected attribute

    def start(self):
        print(f"The {self.make} {self.model} is starting.")

    def stop(self):
        print(f"The {self.make} {self.model} is stopping.")

    def drive(self, distance):
        print(f"The {self.make} {self.model} is driving {distance} miles.")
        self._mileage += distance

    def get_mileage(self):
        return self._mileage


# Derived class: Car (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)  # Calling the parent class constructor
        self.num_doors = num_doors

    def open_trunk(self):
        print(f"The {self.make} {self.model} is opening its trunk.")


# Derived class: Motorcycle (inherits from Vehicle)
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)  # Calling the parent class constructor
        self.has_sidecar = has_sidecar

    def wheelie(self):
        print(f"The {self.make} {self.model} is doing a wheelie!")


# Derived class: ElectricCar (inherits from Car)
class ElectricCar(Car):
    def __init__(self, make, model, year, num_doors, battery_capacity):
        super().__init__(make, model, year, num_doors)  # Calling the parent class constructor
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"The {self.make} {self.model} is charging its battery.")


# Function to display vehicle details (polymorphism)
def display_vehicle_info(vehicle):
    print(f"Make: {vehicle.make}")
    print(f"Model: {vehicle.model}")
    print(f"Year: {vehicle.year}")
    print(f"Mileage: {vehicle.get_mileage()}")

    if isinstance(vehicle, Car):
        print(f"Number of doors: {vehicle.num_doors}")
        vehicle.open_trunk()
    elif isinstance(vehicle, Motorcycle):
        print(f"Has sidecar: {vehicle.has_sidecar}")
        vehicle.wheelie()
    elif isinstance(vehicle, ElectricCar):
        print(f"Battery capacity: {vehicle.battery_capacity}")
        vehicle.charge()

    print()


# Create objects of different vehicle types
car = Car("Toyota", "Camry", 2022, 4)
motorcycle = Motorcycle("Honda", "CBR", 2021, False)
electric_car = ElectricCar("Tesla", "Model S", 2023, 4, 100)

# Create a list of vehicles (polymorphism)
vehicles = [car, motorcycle, electric_car]

# Iterate over the vehicles and display their information
for vehicle in vehicles:
    display_vehicle_info(vehicle)
    vehicle.start()
    vehicle.drive(50)
    vehicle.stop()
    print()