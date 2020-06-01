from abc import ABC, abstractmethod


class Department:
    """
    Class that creates department structure
    """

    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    """
    Abstract class that creates Employee structure
    """

    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self.__department = department

    @abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(self):
        return 8

    def get_department(self):
        return self.__department.name

    def set_department(self, new_department):
        self.__department.name = new_department


class Manager(Employee):
    """
    Manager class which return calc_bonus used for managers only
    """
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department("managers", 1))

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Employee):
    """
    Seller class allows to get and put sellers
    quantities and calcuted its specific bonus
    """
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department("sellers", 2))
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def put_sales(self, new_sales):
        self.__sales += new_sales

    def calc_bonus(self):
        return self.__sales * 0.15
