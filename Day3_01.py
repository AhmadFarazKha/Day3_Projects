from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age, species, diet):
        self.name = name
        self.age = age
        self.species = species
        self.diet = diet
        self.feeding_schedule = []
        self.health_records = []
        self.observations = []

    @abstractmethod
    def calculate_food_quantity(self):
        pass

    def add_feeding_record(self, date, amount):
        self.feeding_schedule.append((date, amount))

    def add_health_record(self, date, treatment):
        self.health_records.append((date, treatment))

    def add_observation(self, date, observation):
        self.observations.append((date, observation))

class Mammal(Animal):
    def __init__(self, name, age, species, diet, fur_color):
        super().__init__(name, age, species, diet)
        self.fur_color = fur_color

    def calculate_food_quantity(self):
        # Implement specific calculation for mammals
        pass

class Reptile(Animal):
    def __init__(self, name, age, species, diet, temperature_preference):
        super().__init__(name, age, species, diet)
        self.temperature_preference = temperature_preference

    def calculate_food_quantity(self):
        # Implement specific calculation for reptiles
        pass

class Bird(Animal):
    def __init__(self, name, age, species, diet, wingspan):
        super().__init__(name, age, species, diet)
        self.wingspan = wingspan

    def calculate_food_quantity(self):
        # Implement specific calculation for birds
        pass

# Example Usage
lion = Mammal("Leo", 5, "Lion", "Meat", "Golden")
snake = Reptile("Python", 3, "Python", "Rodents", "Warm")
eagle = Bird("Eagle", 10, "Golden Eagle", "Meat", 2.3)

lion.add_feeding_record("2024-11-26", 5)
lion.add_health_record("2024-11-25", "Checkup")
lion.add_observation("2024-11-26", "Active and playful")

print(lion.name, lion.feeding_schedule) 

