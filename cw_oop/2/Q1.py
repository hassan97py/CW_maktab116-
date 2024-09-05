class Vehicle:
    
    def __init__(self, make, model, year):
        self.set_make(make)
        self.set_model(model)
        self.set_year(year)

    def set_make(self, make):
        if not isinstance(make, str) or not make.strip():
            raise ValueError("Make must be a non-empty string.")
        self._make = make.strip()

    def get_make(self):
        return self._make

    def set_model(self, model):
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Model must be a non-empty string.")
        self._model = model.strip()

    def get_model(self):
        return self._model

    def set_year(self, year):
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer.")
        self._year = year

    def get_year(self):
        return self._year

    def display_details(self):
        print(f"Make: {self.get_make()}")
        print(f"Model: {self.get_model()}")
        print(f"Year: {self.get_year()}")

my_vehicle = Vehicle("Peugout", "206", 1398)

my_vehicle.display_details()

my_vehicle.set_model("207")
my_vehicle.set_year(1403)
# my_vehicle.set_model("")
# my_vehicle.set_year(-2)

my_vehicle.display_details()