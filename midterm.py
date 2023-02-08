""" ABC Inc. is a company that has number of employees. When the CEO of the company asks his secretary for a list of employees and their salaries. 
She has to produce a sorted list of employee salaries. Sometimes the CEO asks for a particular employee and his/her salary. 
You are a software developer works in this company, you see this as a requirement and develop a software. 

You will create a class called SalarySearchAndSort with the class variable to hold the list of employee salaries. 
You will create two class methods searchList and sortList. Write BinarySearch in searchList method and any one of the Sorting Methods we learnt in sortList.

The instance of the class above mentioned should be used to create a list and print the sorted list first. 
For simplicity, we don't have the employee name, etc. 
So for searching a particular employee salary, you just search the number in the list and your application should return that number if it is in the list. 
If not print the salary not found.

"""

class SalarySearchAndSort():
    def __init__(self, list, target):
        self.__list = list
        self.__target = target

    def sortList(self, list):
        for i in range(1, len(self.__list)):
            j = i
            while self.__list[j-1] > self.__list[j] and j > 0:
                self.__list[j-1], self.__list[j] = self.__list[j], self.__list[j-1]
                j -= 1

    def searchList(self, list, target):
        left = 0
        right = len(self.__list) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.__list[mid] == self.__target:
                return mid
            elif self.__list[mid] < self.__target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    

#list1 = [3,56,65,34,78,23,12]
list1 = list()
a = 'y'
while a.lower() == 'y':
    salary = int(input("Enter the employee's salary: "))
    list1.append(salary)
    a = input("Enter 'y' if you want to add more employee's salary: ")
    
    
target = int(input("Enter the salary you want to find: "))
print("List of the Employee's salaries: ", list1)
instance =SalarySearchAndSort(list1,target)
sort = instance.sortList(list1)
print("Employee's salaries sorted: ",list1)
search = instance.searchList(list1, target)
print("The index of salary need to find is: ", search)

