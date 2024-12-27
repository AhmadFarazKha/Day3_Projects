from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    #VehicleFleet #AbstractClass #VehicleManagement
    Abstract base class for all vehicles.
    """
    def __init__(self, vehicle_id, model, year):
        self.vehicle_id = vehicle_id
        self.model = model
        self.year = year
        self.mileage = 0
        self.maintenance_log = []

    @abstractmethod
    def calculate_fuel_consumption(self, distance):
        """
        #FuelConsumption #Polymorphism 
        Calculates fuel consumption for a given distance.
        """
        pass

    @abstractmethod
    def get_maintenance_schedule(self):
        """
        #MaintenanceSchedule #VehicleMaintenance 
        Returns the maintenance schedule for the vehicle.
        """
        pass

    def add_mileage(self, distance):
        """
        #AddMileage #VehicleTracking 
        Adds mileage to the vehicle's total mileage.
        """
        self.mileage += distance

    def add_maintenance_record(self, date, service_type):
        """
        #MaintenanceRecord #VehicleMaintenance 
        Adds a maintenance record to the vehicle's log.
        """
        self.maintenance_log.append((date, service_type))

class Truck(Vehicle):
    """
    #Truck #VehicleType 
    Class representing a truck.
    """
    def __init__(self, vehicle_id, model, year, load_capacity):
        super().__init__(vehicle_id, model, year)
        self.load_capacity = load_capacity

    def calculate_fuel_consumption(self, distance):
        """
        #TruckFuelConsumption #FuelConsumption 
        Calculates fuel consumption for a truck.
        """
        # Implement specific fuel consumption logic for trucks
        # (e.g., based on load, terrain, etc.)
        return distance * 0.1  # Example: 0.1 liters per kilometer

    def get_maintenance_schedule(self):
        """
        #TruckMaintenance #MaintenanceSchedule 
        Returns the maintenance schedule for a truck.
        """
        return [
            ("03-01", "Oil Change"),
            ("06-01", "Tire Rotation"),
            ("09-01", "Brake Inspection"),
        ]

class Van(Vehicle):
    """
    #Van #VehicleType 
    Class representing a van.
    """
    def __init__(self, vehicle_id, model, year, passenger_capacity):
        super().__init__(vehicle_id, model, year)
        self.passenger_capacity = passenger_capacity

    def calculate_fuel_consumption(self, distance):
        """
        #VanFuelConsumption #FuelConsumption 
        Calculates fuel consumption for a van.
        """
        # Implement specific fuel consumption logic for vans
        return distance * 0.08  # Example: 0.08 liters per kilometer

    def get_maintenance_schedule(self):
        """
        #VanMaintenance #MaintenanceSchedule 
        Returns the maintenance schedule for a van.
        """
        return [
            ("02-01", "Oil Change"),
            ("05-01", "Tire Rotation"),
            ("08-01", "Brake Inspection"),
        ]

class Motorcycle(Vehicle):
    """
    #Motorcycle #VehicleType 
    Class representing a motorcycle.
    """
    def __init__(self, vehicle_id, model, year):
        super().__init__(vehicle_id, model, year)

    def calculate_fuel_consumption(self, distance):
        """
        #MotorcycleFuelConsumption #FuelConsumption 
        Calculates fuel consumption for a motorcycle.
        """
        # Implement specific fuel consumption logic for motorcycles
        return distance * 0.05  # Example: 0.05 liters per kilometer

    def get_maintenance_schedule(self):
        """
        #MotorcycleMaintenance #MaintenanceSchedule 
        Returns the maintenance schedule for a motorcycle.
        """
        return [
            ("01-01", "Oil Change"),
            ("04-01", "Tire Check"),
            ("07-01", "Brake Check"),
        ]

# Example Usage (Careem/Uber/Yango)
truck1 = Truck("T001", "Ford F-150", 2022, 1000)
van1 = Van("V001", "Toyota Hiace", 2021, 7)
motorcycle1 = Motorcycle("M001", "Honda CBR", 2020)

# Calculate fuel consumption for a 100km trip
truck_fuel = truck1.calculate_fuel_consumption(100)
van_fuel = van1.calculate_fuel_consumption(100)
motorcycle_fuel = motorcycle1.calculate_fuel_consumption(100)

print(f"Truck fuel consumption: {truck_fuel} liters")
print(f"Van fuel consumption: {van_fuel} liters")
print(f"Motorcycle fuel consumption: {motorcycle_fuel} liters")

# Get maintenance schedule for truck
truck_maintenance = truck1.get_maintenance_schedule()
print("Truck Maintenance Schedule:")
for date, service in truck_maintenance:
    print(f"{date}: {service}")

