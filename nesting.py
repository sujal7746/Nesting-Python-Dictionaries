cars = {}       #dictionary for holding
print(cars)
print(type(cars))     #type is dictionary
print()

car_1 = {'make': 'BMW', 'speed': 'fast'}  #dict car_1 key: value
car_2 = {'make': 'jio', 'speed': 'not good'}
car_3 = {'make': 'Airtel', 'speed': 'super fast'}

cars['car 1'] = car_1    #Assign car_1 dict to cars, creating a key
cars['car 2'] = car_2
cars['car 3'] = car_3

print(cars)
print()

from pprint import pprint
pprint(cars)
print()

print(cars['car 2'] ['make'])      #what make is car 2?
print(cars['car 3'] ['speed'])     #what is the speed of car 3?

# 3- level nesting
vehicle = {'cars': cars, 'planes':None, 'trains': None}  #creating a dict with key value pairs
pprint(vehicle)

print()
print(vehicle['cars'])
print(vehicle['planes'])
print(vehicle['trains'])

print()
vehicle_cars = vehicle['cars']  #assign nested dict to new variable
pprint(vehicle_cars)

print()
print(type(vehicle_cars))         #variable type dictionary
