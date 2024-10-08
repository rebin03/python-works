# Example of returning tuple like object

import collections

Player = collections.namedtuple('Player', ['name', 'age', 'country'])

# object of new tuple

p1 = Player('Messi', 36, 'Argentina')
p2 = Player('Ronaldo', 37, 'Portugese')

print(p1.name, p1.age, p1.country)
print(p2.name, p2.age, p2.country)