# Base class
class smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def call(self, number):
        print(f"{self.brand}{self.model} is calling {number} ...")

    def charge(self):
        print(f"{self.brand}{self.model} is charging")

    def info(self):
        return f"{self.brand}{self.model} | Storage: {self.storage}GB | Battery: {self.battery}mAH"
    
# Child class (Inheritance)
class iphone(smartphone):
    def __init__(self, model, storage, battery, face_id=True):
        super().__init__("Apple", model, storage, battery)
        self.face_id = face_id
    
    def unlock(self):
        if self.face_id:
            print(f"{self.model} unlocked using Face ID")
        else:
            print(f"{self.model} unlocked with passcode")

class Samsung(smartphone):
    def __init__(self, model, storage, battery, stylus=False):
        super().__init__("Samsung", model, storage, battery)
        self.stylus = stylus

    def use_stylus(self):
        if self.stylus:
            print(f"{self.model} using S-Pen")
        else:
            print(f"{self.model} has no stylus")

# Testing
phone1 = iphone("iphone 14 pro", 256, 3200)
phone2 = Samsung("Galaxy S23", 512, 4000, stylus=True)

print(phone1.info())
phone1.unlock()
phone1.call("0112951915")

print("\n" + phone2.info())
phone2.use_stylus()
phone2.charge()

    