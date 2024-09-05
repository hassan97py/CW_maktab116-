class Laptop:
    def __init__(self,brand,ram,storage):
        self.set_brand(brand)
        self.set_ram(ram)
        self.set_storage(storage)

    def set_brand(self,brand):
        if not isinstance(brand,str) or not brand.split():
            raise ValueError("brand must be a non-empty string. ")
        self.brand=brand
    
    def get_brand(self):
        return self.brand

    def set_ram(self,ram):
        if not isinstance(ram,int) or ram<=0:
            raise ValueError("ram must be a non-empty string. ")
        self.ram=ram

    def get_ram(self):
        return self.ram

    def set_storage(self,storage):
        if not isinstance(storage,int) or storage<=0:
            raise ValueError("storage must be a non-empty string. ")
        self.storage=storage

    def get_storage(self):
        return self.storage
    
    def display_details(self):
        print(f"brand: {self.get_brand()}")
        print(f"ram: {self.get_ram()} GB")
        print(f"storage:  {self.get_storage()} GB")

Lap=Laptop('lenovo',1,512)
Lap.display_details()
