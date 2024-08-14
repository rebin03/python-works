class Instructor():
    followers = 0
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    def display(self, subject_name):
        print(f"Hi I'm {self.name} and I teach {subject_name}")
        
    def update_followers(self, follower_name):
        self.followers += 1


instructor1 = Instructor("Helen", "Chennai")
print(instructor1.name)

instructor1.display("Python")

print(instructor1.followers)
instructor1.update_followers("Sam")
print(instructor1.followers)