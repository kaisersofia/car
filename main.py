class Vehicle:
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

    def display_info(self):
        print(f"Марка: {self.brand}, Год выпуска: {self.year}, Цвет: {self.color}")

class Car(Vehicle):
    def __init__(self, brand, year,color, num_doors):
        super().__init__(brand, year,color)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Количество дверей: {self.num_doors}")

class Motorcycle(Vehicle):
    def __init__(self, brand, year,color, engine_capacity):
        super().__init__(brand, year,color)
        self.engine_capacity = engine_capacity

    def display_info(self):
        super().display_info()
        print(f"Объем двигателя: {self.engine_capacity} см³")


car1 = Car("BMW", 2017, "Blue")
motorcycle1 = Motorcycle("Suziki", 2022, 2)

car1.display_info()
print()
motorcycle1.display_info()