# This program demonstrates the Car class.

import vehicle

def main():
    # Create an object from the Car class.
    # The car is a 2022 Kia with 20,000 miles, priced 
    # at $20,500.00, and has 4 doors.
    used_car = vehicle.Car('Kia', 2022, 20000, 20500, 4)

    # Display the car's data.
    print('Make:', used_car.get_make())
    print('Model:', used_car.get_model())
    print('Milage:', used_car.get_milage())
    print('Price:', used_car.get_price())
    print('Number of doors:', used_car.get_doors())

# Call the main function
main()