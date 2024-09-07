from pprint import pprint



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

vehicle = {'cars': cars, 'planes': None, 'trains': None} #create dict with key value pairs

plane_1 = {'Model': 'Boing 55'}
plane_2 = {'Model': 'Airbus'}
planes = {'plane 1': plane_1, 'plane 2': plane_2}
vehicle['planes'] =  planes

train_1 = {'Model': 'Shridham'}
train_2 = {'Model': 'Ak878'}
trains = {'train 1': train_1, 'train 2': train_2}
vehicle['trains'] = trains

pprint(vehicle)
