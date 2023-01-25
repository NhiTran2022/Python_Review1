# This program creates a Car object, a Truck object,
# and an SUV object.

import vehicle

def main():
    # Create an object from the Car class.
    # The car is a 2022 Kia with 20,000 miles, priced 
    # at $20,500.00, and has 4 doors.
    used_car = vehicle.Car('Kia', 2022, 20000, 20500, 4)

    # Create a Truck object for a used 2002
    # Toyota pickup with 40,000 miles, priced 
    # at $12,000, with 4-wheel drive.
    truck = vehicle.Truck('Toyota', 2002, 40000, 12000.0, '4WD')

    # Create a SUV object for a used 2000
    # Volvo with 30,000 miles, priced 
    # at $18,000, with 5 passenger capacity.

    suv = vehicle.SUV('Volvo', 2000, 30000, 18000.0,5)

    print('USED CAR INVENTORY')
    print('==================')
    # Display the car's data.
    print("The following car is in inventory")
    print('Make:', used_car.get_make())
    print('Model:', used_car.get_model())
    print('Milage:', used_car.get_milage())
    print('Price:', used_car.get_price())
    print('Number of doors:', used_car.get_doors())

    # Display the truck's data.
    print('The following pickup truck is in inventory.')
    print('Make:', truck.get_make())
    print('Model:', truck.get_model())
    print('Milage:', truck.get_milage())
    print('Price:', truck.get_price())
    print('Drive type:', truck.get_drive_type())

    # Display the SUV's data.
    print('The following SUV is in inventory')
    print('Make:', suv.get_make())
    print('Model:', suv.get_model())
    print('Milage:', suv.get_milage())
    print('Price:', suv.get_price())
    print('Passenger Capacity:', suv.get_pass_cap())

# Call the main function
main()