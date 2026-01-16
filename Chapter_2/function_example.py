# Functions and methods, instance vs local

# use import to import file/module
import DimmerSwitch

# **Function** definition
def givemeColor():
    color = 255
    print('Color level is', color)

# Creating an object from class in different file
# Use module.class to instantiate object

oDimmer1 = DimmerSwitch.DimmerSwitch()
oDimmer2 = DimmerSwitch.DimmerSwitch()

givemeColor()

# Using **methods** of the object
oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()
oDimmer1.show()

oDimmer2.turnOff()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.show()

# Color level is 255
# Switch is on? True
# Brightness is: 2
# Switch is on? False
# Brightness is: 4