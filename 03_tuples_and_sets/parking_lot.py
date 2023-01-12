number_of_cars = int(input())
parking = set()
for current_car in range(number_of_cars):
    direction, plate_number = input().split(", ")
    if direction == "IN":
        parking.add(plate_number)
    elif direction == "OUT":
        parking.remove(plate_number)
if len(parking) > 0:
    for i in parking:
        print(i)
else:
    print("Parking Lot is Empty")