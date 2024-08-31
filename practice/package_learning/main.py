import HomeShift.HomeShiftItem.cloths.jeans as jeans
import HomeShift.HomeShiftItem.books as book

# This will import all the variables and function in the module
from HomeShift.HomeShiftItem.footwear.clogs import *

# We can't import all the modules directly from a package. but can specify the packages to import in the init module and import all at once.
from HomeShift.HomeShiftItem.footwear import *

jeans.display()
book.display()

display()
brand()
color()

boots.display()
clogs.brand()