import csv

states1 = ["Victoria", "New South Wales", "Queensland", "Northern Territory"]
states2 = ["Victoria", "New South Wales", "Queensland", "Tasmania", "South Australia"]
address1 = {
    "Street": "178 Bluff Road",
    "City": "Manly",
    "State": "NSW",
    "PostCode": "2101",
}
address2 = {
    "Street": "10 Downing Street",
    "City": "Brighton",
    "State": "VIC",
    "PostCode": "3188",
}


class Vehicle:
    """
    A class to represent a vehicle.

    Attributes
    ----------
    rego: vehicle's registration number
    make: vehicle's brand
    model: vehicle's model
    current_odometer: vehicle's current odometer
    driver: the driver of the vehicle

    Methods:
    ----------
    display_odometer(): display vehicle's current odometer
    update_odometer(km): update vehicle's odometer
    vehicle_general_info(): display vehicle's general information

    """

    def __init__(self, rego, make, model, current_odometer, driver):
        """
        Constructs all the necessary attributes for the vehicle object.
        :param rego: vehicle's registration number
        :param make: vehicle's brand
        :param model: vehicle's model
        :param current_odometer: vehicle's current odometer
        :param driver: the driver of the vehicle
        """

        self.rego = rego
        self.make = make
        self.model = model
        self.current_odometer = current_odometer
        self.driver = driver

    def display_odometer(self):
        """
        Prints the vehicle's current odometer
        :return: None

        """
        print(f"The vehicle current odometer is {self.current_odometer} ")

    def update_odometer(self):
        """
        Update vehicle's odometer by adding number of kilometers driven
        :return: None
        """
        while True:
            try:
                km = int(input(f"How many kilometers do you want to add to {self.make}?\n"))
            except ValueError:
                print("Error! Please put in a valid number")
            else:
                self.current_odometer += km
                if self.current_odometer < 0:
                    print("The odometer should not less than zero.Please put in a positive number ")
                    self.current_odometer -= km
                else:
                    print(f"The {self.make} current odometer is {self.current_odometer} ")
                    break

    def vehicle_general_info(self):
        """
        Prints the vehicle's general information rego, make, mode and current_odometer
        :return: None
        """
        print(f"""
            The vehicle registration number {self.rego} is a {self.make}. Model is {self.model}.Odometer {self.current_odometer} km. 
        """)


class Car(Vehicle):
    """
    A class to represent a car ,and it is a subclass of the Vehicle.

    Attributes
    ----------
    rego: car's registration number
    make: car's brand
    model: car's model
    current_odometer: car's current odometer
    body_type: car's body type
    color: color of the car
    upholstery: car's interior
    num_of_doors: how many doors a car have
    driver: the driver of the car

    Methods:
    ----------
    display_color(): display car's current color
    display_color(c_color): change car's color
    car_with_driver(): display car's specific and general data along with an associated given drivers' details
    """

    def __init__(self, rego, make, model, current_odometer, body_type, color, upholstery, num_of_doors, driver):
        """
        Constructs all the necessary attributes for the car object.
        :param rego: car's registration number
        :param make: car's brand
        :param model: car's model
        :param current_odometer: car's current odometer
        :param body_type: car's body type
        :param color: color of the car
        :param upholstery: car's interior
        :param num_of_doors: how many doors a car have
        :param driver: the driver of the car
        """
        super().__init__(rego, make, model, current_odometer, driver)
        self.body_type = body_type
        self.color = color
        self.upholstery = upholstery
        self.number_of_doors = num_of_doors

    def car_specific(self):
        print(
            f"The {self.make} car additional details are: body type {self.body_type}, color {self.color}, {self.upholstery} interior, {self.number_of_doors} doors.")

    def display_color(self):
        """
        Prints car's current color
        :return: None
        """
        print(f"The color of {self.make}-{self.model} is {self.color}.")

    def change_color(self):
        """
        change car's color
        :param c_color: which color want to change for the car
        :return: None
        """
        print(f"The color of {self.make}-{self.model} is {self.color}")
        colour = input("What color do you want to change?\n")
        self.color = colour
        print(f"The color of {self.make}-{self.model} is {self.color}")

    def car_with_driver(self):
        """
        Prints car's specific and general data along with an associated given drivers' details
        :return: None
        """
        print(
            f"Vehicle registration number {self.rego} is a {self.make}. Model is {self.model}. Current odometer is {self.current_odometer} km.")
        self.car_specific()
        print(f"The driver info of {self.make} as follows:")
        self.driver.driver_info()


class Truck(Vehicle):
    """
    A class to represent a truck, and it is a subclass of the Vehicle.

    Attributes
    ----------
    rego: truck's registration number
    make: truck's brand
    model: truck's model
    current_odometer: truck's current odometer
    max_load_cap: truck's max_load_cap
    num_of_axles: how many axles a truck have
    num_of_wheels: how many wheels a truck have
    driver: the driver of the truck

    Methods:
    ----------
    truck_with_dirver(): display truck's specific and general data along with an associated given drivers' details

    """

    def __init__(self, rego, make, model, current_odometer, max_load_cap, num_of_axles, num_of_wheels, driver):
        """
        Constructs all the necessary attributes for the truck object.
        :param rego: truck's registration number
        :param make: truck's brand
        :param model: truck's model
        :param current_odometer: truck's current odometer
        :param max_load_cap: truck's max_load_cap
        :param num_of_axles: how many axles a truck have
        :param num_of_wheels: how many wheels a truck have
        :param driver: the driver of the truck
        """
        super().__init__(rego, make, model, current_odometer, driver)
        self.max_load_cap = max_load_cap
        self.num_of_axles = num_of_axles
        self.num_of_wheels = num_of_wheels
        self.driver = driver

    def truck_specific(self):
        print(
            f"The {self.make} truck additional details are: max_load_cap {self.max_load_cap}, {self.num_of_axles} axles, {self.num_of_wheels} wheels.")

    def truck_with_driver(self):
        """
        Prints truck's specific and general data along with an associated given drivers' details
        :return: None
        """
        print(
            f"Vehicle registration number {self.rego} is a {self.make}. Model is {self.model}. Current odometer is {self.current_odometer} km.")
        self.truck_specific()
        print(f"The driver info of {self.make} as follows:")
        self.driver.driver_info()


class Driver:
    """
    A class to represent a driver.

    Attributes
    ----------
    min_demerit_points : class attribute, minimum amount of demerit a driver allow to have set to 0
    max_demerit_points: class attribute, maximum amount of demerit a driver allow to have and set to 12
    demerit_warning: class attribute, when reach demerit amount of 9 will display warning message
    licence_number: driver's licence_number
    f_name: driver's first name
    l_name: driver's last name
    mobile: driver's mobile
    address: driver's address
    states_of_drive: states driver's are licenses to drive in
    current_demerit_points: driver's current demerit points

    Methods:
    ----------
    display_current_demerit_points(): display driver's current demerit points
    decrease_demerit(number): decrease driver's demerit points
    increase_demerit(number): increase_demerit driver's demerit points
    driver_info(): display all the data for a driver
    write_driver_info(): write driver info into a csv file
    read_driver_info(): static method, read driver info from csv file
    """
    min_demerit_points = 0
    max_demerit_points = 12
    demerit_warning = 9

    def __init__(self, licence_number, f_name, l_name, mobile, address, states_of_drive, current_demerit_points):
        """
        Constructs all the necessary attributes for the driver object.
        :param licence_number: driver's licence_number
        :param f_name: driver's first name
        :param l_name: driver's last name
        :param mobile: driver's mobile
        :param address: driver's address
        :param states_of_drive: states driver's are licenses to drive in
        :param current_demerit_points: driver's current demerit points
        """
        self.licence_number = licence_number
        self.f_name = f_name
        self.l_name = l_name
        self.mobile = mobile
        self.address = address
        self.states_of_drive = states_of_drive
        self.current_demerit_points = current_demerit_points

    def display_current_demerit_points(self):
        """
        Prints driver's current demerit points
        :return: None
        """
        print(f"The driver {self.f_name} {self.l_name}'s current demerit points is {self.current_demerit_points}.")

    def decrease_demerit(self):
        """
        Decrease driver's demerit points
        :return: None
        """
        while True:
            try:
                number = int(
                    input(f"How many demerit points do you want to decrease for {self.f_name} {self.l_name}\n"))
            except ValueError:
                print("Error! Please put in a valid number")
            else:
                self.current_demerit_points -= number
                if self.current_demerit_points < Driver.min_demerit_points:
                    print(
                        f"Demerit points should not be allowed to fall below {Driver.min_demerit_points}. Please put in a new number")
                    self.current_demerit_points += number
                elif self.current_demerit_points >= Driver.demerit_warning:
                    print("License suspension is imminent")
                    break
                else:
                    print(
                        f"The driver {self.f_name} {self.l_name}'s current demerit points is {self.current_demerit_points}.")
                    break

    def increase_demerit(self):
        """
        Increase driver's demerit points
        :return: None
        """
        while True:
            try:
                number = int(
                    input(f"How many demerit points do you want to increase for {self.f_name} {self.l_name}\n"))
            except ValueError:
                print("Error! Please put in a valid number")
            else:
                self.current_demerit_points += number
                if self.current_demerit_points > Driver.max_demerit_points:
                    print(
                        f"Demerit points should not be allowed to increase beyond {Driver.max_demerit_points}. Please put in a new number")
                    self.current_demerit_points -= number
                elif self.current_demerit_points >= Driver.demerit_warning:
                    print("License suspension is imminent")
                    break
                else:
                    print(
                        f"The driver {self.f_name} {self.l_name}'s current demerit points is {self.current_demerit_points}.")
                    break

    def driver_info(self):
        """
        Prints all the data for a driver
        :return: None
        """
        print(
            f"The driver {self.f_name} {self.l_name}, has a driver licence number : {self.licence_number}. Current "
            f"demerit point is {self.current_demerit_points}.\nContact phone number is : {self.mobile}\nDriver "
            f"address is :") 
        for (k, v) in self.address.items():
            print(f"{k} : {v}")
        print("The driver is licenced to drive in the following states:")
        for state in self.states_of_drive:
            print(f"{state}", end=" :  ")
        print()

    def write_driver_info(self):
        """
        write driver infor to a csv file
        :return: None
        """
        with open("DriverInfo.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [self.licence_number, self.f_name, self.l_name, self.mobile, self.address, self.states_of_drive,
                 self.current_demerit_points])

    @staticmethod
    def read_driver_info():
        """
        read driver info from csv file.
        :return: None
        """
        with open("DriverInfo.csv", "r") as data:
            content = data.read()
            print(content)


# set all class functions
all_function = ["car_general_info", "truck_general_info", "car_specific", "truck_specific", "driver_info",
                "display_current_demerit_points",
                "decrease_demerit", "increase_demerit", "update_odometer", "change_color", "car_with_driver",
                "truck_with_driver", "exit"]


def main():
    driver1 = Driver(3313377, "Gladys", "Berejkilan", "0414566999", address1, states1, 8)
    driver2 = Driver(9877345, "Boris", "Johnson", "0414123456", address2, states2, 3)
    car1 = Car("BBJ702", "Mazda", "CX3", 10000, "Hatch", "Blue", "Leather", 5, driver1)
    car2 = Car("OY0400", "Ford", "Festiva", 39785, "Sedan", "Green", "Fabric", 4, driver2)
    truck1 = Truck("XJBJ882", "Kenworth", "BigMother5000", 150000, "40 tonnes", 5, 18, driver1)
    truck2 = Truck("ARC542", "Hyundai", "iLoad", 76520, "2 tonnes", 2, 4, driver2)
    print("Welcome to the Inventory APP presentation.")
    while True:
        print("Please choose which information do you want to display?\n")
        for i, func in enumerate(all_function, 1):
            print(i, func)
        num = int(input())
        if num == 1:
            car1_g = getattr(car1, all_function[num - 1].replace("car", "vehicle"))
            car2_g = getattr(car2, all_function[num - 1].replace("car", "vehicle"))
            car1_g()
            car2_g()
        elif num == 2:
            truck1_g = getattr(truck1, all_function[num - 1].replace("truck", "vehicle"))
            truck2_g = getattr(truck2, all_function[num - 1].replace("truck", "vehicle"))
            truck1_g()
            truck2_g()
        elif num == 3:
            car1_s = getattr(car1, all_function[num - 1])
            car2_s = getattr(car2, all_function[num - 1])
            car1_s()
            car2_s()
        elif num == 4:
            truck1_s = getattr(truck1, all_function[num - 1])
            truck2_s = getattr(truck2, all_function[num - 1])
            truck1_s()
            truck2_s()
        elif num == 5:
            driver1_g = getattr(driver1, all_function[num - 1])
            driver2_g = getattr(driver2, all_function[num - 1])
            driver1_g()
            print()
            driver2_g()
        elif num == 6:
            driver1_dd = getattr(driver1, all_function[num - 1])
            driver2_dd = getattr(driver2, all_function[num - 1])
            driver1_dd()
            driver2_dd()
        elif num == 7:
            driver1_decrease = getattr(driver1, all_function[num - 1])
            driver2_decrease = getattr(driver2, all_function[num - 1])
            driver1_decrease()
            driver2_decrease()
        elif num == 8:
            driver1_increase = getattr(driver1, all_function[num - 1])
            driver2_increase = getattr(driver2, all_function[num - 1])
            driver1_increase()
            driver2_increase()
        elif num == 9:
            car1_odo = getattr(car1, all_function[num - 1])
            car2_odo = getattr(car2, all_function[num - 1])
            car1_odo()
            car2_odo()
        elif num == 10:
            car1_color = getattr(car1, all_function[num - 1])
            car2_color = getattr(car2, all_function[num - 1])
            car1_color()
            input("Please any key to continue.")
            car2_color()
        elif num == 11:
            car1_with_driver = getattr(car1, all_function[num - 1])
            car2_with_driver = getattr(car2, all_function[num - 1])
            car1_with_driver()
            input("Please any key to continue.")
            car2_with_driver()
            input("Please any key to continue.")
        elif num == 12:
            truck1_with_driver = getattr(truck1, all_function[num - 1])
            truck2_with_driver = getattr(truck2, all_function[num - 1])
            truck1_with_driver()
            input("Please any key to continue.")
            truck2_with_driver()
        elif num == 13:
            break

if __name__ == "__main__":
    main()














# # future reference

# import sys
# stdout_main = sys.stdout  #  set the current file handle as standard default ouput (console)

#     def write_driver_info(self):
#         """
#         Redirect output from console to a text file
#         :return: None
#         """
#         sys.stdout = open("DriverInfo.txt", "a")    #Redirect sys.stdout to a text file
#         self.driver_info()       #Prints to the redirected stdout (Output.txt)
#         sys.stdout.close()       #Close the file
#         sys.stdout = stdout_main  # Restore sys.stdout to our old saved file handler
