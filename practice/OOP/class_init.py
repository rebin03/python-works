class Instructor():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.followers = 0


instructor1 = Instructor("Helen", "Chennai")
print(instructor1.name)
print(instructor1.address)
print(instructor1.followers)

instructor2 = Instructor("Alexa", "Delhi")
print(instructor2.name)
print(instructor2.address)