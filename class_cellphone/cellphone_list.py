# This program creates five Cellphone objects and
# stores them in a list.

import cellphone

def main():
    

    # The make_list() function gets data from the user
    # for five phones. The function returns a list 
    # of Cellphone objects containing the data.

    def make_list():
        # Create an empty list
        phone_list =[]

        # Add five Cellphone objects to the list
        print('Enter data for five phones. ')
        for count in range(1,6):
            # Get the phone data.
            print("Phone number " + str(count) + ":")
            man = input("Enter the manufacturer: ")
            mod = input("Enter the model number: ")
            retail = float(input("Enter the retail price: "))

            print()

            # Create a new Cellphone object in memory and 
            # assign it to the phone variable.
            phone = cellphone.Cellphone(man, mod, retail)

            # Add the object to the list.
            phone_list.append(phone)

        return phone_list
    # The display_list funtion accepts a list containing 
    # Cellphone objects as an argument and displays the 
    # data stored in each object.

    def display_list(phone_list):
        for item in phone_list:
            print(item.get_manufact())
            print(item.get_model())
            print(item.get_retail_price())
            print()

    # Get a list of Cellphone objects.

    phones = make_list()

    # Display the data in the list.
    print("Here is the data you entered: ")
    display_list(phones)

# Call the main function
main()
