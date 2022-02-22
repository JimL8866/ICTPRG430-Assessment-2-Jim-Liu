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
    vehicle_info(): display vehicle's general information

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
                km = int(input("How many kilometers do you want to add the vehicle\n"))
            except ValueError:
                print("Error! Please put in a valid number")
            else:
                self.current_odometer += km
                if self.current_odometer < 0:  
                    print("The odometer should not less than zero.Please put in a positive number ")
                    self.current_odometer -= km
                else:
                    break

    def vehicle_info(self):
        """
        Prints the vehicle's general information rego, make, mode and current_odometer
        :return: None
        """
        print(f"""
            Vehicle registration number {self.rego} is a {self.make}. Model is {self.model}.Odometer {self.current_odometer} km. 
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
    car_info(): display car's specific and general data along with an associated given drivers' details
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

    def display_color(self):
        """
        Prints car's current color
        :return: None
        """
        print(f"The color of {self.make}-{self.model} is {self.color}")

    def change_color(self, c_color):
        """
        change car's color
        :param c_color: which color want to change for the car
        :return: None
        """
        self.color = c_color

    def car_info(self):
        """
        Prints car's specific and general data along with an associated given drivers' details
        :return: None
        """
        print(f"""
            Vehicle registration number {self.rego} is a {self.make}. Model is {self.model}.Odometer {self.current_odometer} km.
            The driver of the vehicle is {self.driver.f_name} {self.driver.l_name}. Driver License number: {self.driver.licence_number}
            Additional details:
            The car details are: body type {self.body_type}, color {self.color}, {self.upholstery} interior, {self.number_of_doors} doors.
        """)


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
    truck_info(): display truck's specific and general data along with an associated given drivers' details

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

    def truck_info(self):
        """
        Prints truck's specific and general data along with an associated given drivers' details
        :return: None
        """
        print(f"""
               Vehicle registration number {self.rego} is a {self.make}. Model is {self.model}.Odometer {self.current_odometer} km.
               The driver of the vehicle is {self.driver.f_name} {self.driver.l_name}. Driver License number: {self.driver.licence_number}
               Additional details:
               The truck details are: max_load_cap {self.max_load_cap}, {self.num_of_axles} axles, {self.num_of_wheels} wheels.
           """)


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
                number = int(input("How many demerit points do you want to decrease\n"))
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
                    break

    def increase_demerit(self):
        """
        Increase driver's demerit points
        :return: None
        """
        while True:
            try:
                number = int(input("How many demerit points do you want to increase\n"))
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
                    break

    def driver_info(self):
        """
        Prints all the data for a driver
        :return: None
        """
        print(
            f"The driver {self.f_name} {self.l_name}, has a driver licence number : {self.licence_number}\nContact phone number is : {self.mobile}\nDriver address is :")
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


def main():
    input("Press Enter to continue")
    # create driver1 instance
    driver1 = Driver(3313377, "Gladys", "Berejkilan", "0414566999", address1, states1, 8)
    driver1.display_current_demerit_points()
    # test driver1 demerit decrease
    driver1.decrease_demerit()
    driver1.display_current_demerit_points()
    # test driver1 demerit increase
    driver1.increase_demerit()
    driver1.display_current_demerit_points()

    input("Press Enter to continue")
    # prints driver1 all data
    driver1.driver_info()
    input("Press Enter to continue")
    # write driver1 data to a text file
    driver1.write_driver_info()
    # read driver1 data from a text file
    driver1.read_driver_info()

    input("Press Enter to continue")
    # create driver2 instance
    driver2 = Driver(9877345, "Boris", "Johnson", "0414123456", address2, states2, 3)
    driver2.display_current_demerit_points()
    # test driver2 demerit decrease
    driver2.decrease_demerit()
    driver2.display_current_demerit_points()
    # test driver2 demerit increase
    driver2.increase_demerit()
    driver2.display_current_demerit_points()

    input("Press Enter to continue")
    # prints driver2 all data
    driver2.driver_info()
    input("Press Enter to continue")
    # write driver2 data to a text file
    driver2.write_driver_info()
    # read driver2 data from a text file
    driver2.read_driver_info()

    # create car1 instance
    car1 = Car("BBJ702", "Mazda", "CX3", 10000, "Hatch", "Blue", "Leather", 5, driver1)
    input("Press Enter to continue")
    # prints car1 general data
    car1.vehicle_info()
    input("Press Enter to continue")
    # test car1 color change
    car1.display_color()
    input("Press Enter to continue")
    car1.change_color("White")
    car1.display_color()
    input("Press Enter to continue")
    car1.display_odometer()
    # test car1 odometer change
    car1.update_odometer()
    car1.display_odometer()
    input("Press Enter to continue")
    # prints car1 general data with specific data along with driver data
    car1.car_info()

    # create car2 instance
    car2 = Car("OY0400", "Ford", "Festiva", 39785, "Sedan", "Green", "Fabric", 4, driver2)
    input("Press Enter to continue")
    # prints car2 general data
    car2.vehicle_info()
    input("Press Enter to continue")
    # test car2 color change
    car2.display_color()
    input("Press Enter to continue")
    car2.change_color("Black")
    car2.display_color()
    car2.display_odometer()
    # test car2 odometer change
    car2.update_odometer()
    car2.display_odometer()
    input("Press Enter to continue")
    # prints car2 general data with specific data along with driver data
    car2.car_info()

    # create truck1 instance
    truck1 = Truck("XJBJ882", "Kenworth", "BigMother5000", 150000, "40 tonnes", 5, 18, driver1)
    input("Press Enter to continue")
    # print truck1 general data
    truck1.vehicle_info()
    input("Press Enter to continue")
    # test truck1 odometer change
    truck1.display_odometer()
    truck1.update_odometer()
    truck1.display_odometer()
    input("Press Enter to continue")
    # prints truck1 general data with specific data along with driver data
    truck1.truck_info()

    # create truck2 instance
    truck2 = Truck("ARC542", "Hyundai", "iLoad", 76520, "2 tonnes", 2, 4, driver2)
    input("Press Enter to continue")
    # print truck2 general data
    truck2.vehicle_info()
    # test truck2 odometer change
    truck2.display_odometer()
    truck2.update_odometer()
    truck2.display_odometer()
    input("Press Enter to continue")
    # prints truck2 general data with specific data along with driver data
    truck2.truck_info()


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
