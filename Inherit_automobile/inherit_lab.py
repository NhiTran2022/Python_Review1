"""
    Write a class called 'Doctor' inheriting 'Employee'
    with the properties and methods:
        - network
        - yearsOfExperience
        - setters and getters
"""

class Employee:
    def __init__(self, name, employee_id):
        self.__name = name
        self.__employee_id = employee_id

class Doctor(Employee):
    def __init__(self, network, yearsOfExperience):
        self.__network = network
        self.__yearsOfExperience = yearsOfExperience

    # Setter methods
    def set_network(self, network):
        self.__network = network

    def set_yearsOfExperience(self, yearsOfExperience):
        self.__yearsOfExperience = yearsOfExperience

    # Getter methods
    def get_network(self):
        return self.__network

    def get_yearsOfExperience(self):
        return self.__yearsOfExperience