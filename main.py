import sys

stdout_main = sys.stdout

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
    def __init__(self, rego, make, model, current_odometer, driver):
        self.rego = rego
        self.make = make
        self.model = model
        self.current_odometer = current_odometer
        self.driver = driver

    def display_odometer(self):
        print(f"The vehicle current odometer is {self.current_odometer} ")

    def update_odometer(self, km):
        self.current_odometer += km
        if self.current_odometer < 0:
            print("The odometer is not valid ")

    def vehicle_info(self):
        print(f"""
            Vehicle registration number {self.rego} is a {self.make}. Model is {self.model}.Odometer {self.current_odometer} km. 
        """)


class Car(Vehicle):
    def __init__(self, rego, make, model, current_odometer, body_type, color, upholstery, num_of_doors, driver):
        super().__init__(rego, make, model, current_odometer, driver)
        self.body_type = body_type
        self.color = color
        self.upholstery = upholstery
        self.number_of_doors = num_of_doors

    def display_color(self):
        print(f"The color of {self.make}-{self.model} is {self.color}")

    def change_color(self, c_color):
        self.color = c_color

    def car_info(self):
        print(f"""
            Vehicle registration number {self.rego} is a {self.make}. Model is {self.model}.Odometer {self.current_odometer} km.
            The driver of the vehicle is {self.driver.f_name} {self.driver.l_name}. Driver License number: {self.driver.licence_number}
            Additional details:
            The car details are: body type {self.body_type}, color {self.color}, {self.upholstery} interior, {self.number_of_doors} doors.
        """)


class Truck(Vehicle):
    def __init__(self, rego, make, model, current_odometer, max_load_cap, num_of_axles, num_of_wheels, driver):
        super().__init__(rego, make, model, current_odometer, driver)
        self.max_load_cap = max_load_cap
        self.num_of_axles = num_of_axles
        self.num_of_wheels = num_of_wheels
        self.driver = driver

    def truck_info(self):
        print(f"""
               Vehicle registration number {self.rego} is a {self.make}. Model is {self.model}.Odometer {self.current_odometer} km.
               The driver of the vehicle is {self.driver.f_name} {self.driver.l_name}. Driver License number: {self.driver.licence_number}
               Additional details:
               The truck details are: max_load_cap {self.max_load_cap}, {self.num_of_axles} axles, {self.num_of_wheels} wheels.
           """)


class Driver:
    min_demerit_points = 0
    max_demerit_points = 12
    demerit_warning = 9

    def __init__(self, licence_number, f_name, l_name, mobile, address, states_of_drive, current_demerit_points):
        self.licence_number = licence_number
        self.f_name = f_name
        self.l_name = l_name
        self.mobile = mobile
        self.address = address
        self.states_of_drive = states_of_drive
        self.current_demerit_points = current_demerit_points

    def display_current_demerit_points(self):
        print(f"The driver {self.f_name} {self.l_name}'s current demerit points is {self.current_demerit_points}.")

    def decrease_demerit(self, number):
        self.current_demerit_points -= number
        if self.current_demerit_points < Driver.min_demerit_points:
            print(f"Demerit points should not be allowed to fall below {Driver.min_demerit_points}")

        elif self.current_demerit_points >= Driver.demerit_warning:
            print("License suspension is imminent")

    def increase_demerit(self, number):
        self.current_demerit_points += number
        if self.current_demerit_points > Driver.max_demerit_points:
            print(f"Demerit points should not be allowed to increase beyond {Driver.max_demerit_points}")
        elif self.current_demerit_points >= Driver.demerit_warning:
            print("License suspension is imminent")
        else:
            print(f"The driver {self.f_name} {self.l_name} 's current demerit points is {self.current_demerit_points}")

    def driver_info(self):
        print(
            f"The driver {self.f_name} {self.l_name}, has a driver licence number : {self.licence_number}\nContact phone number is : {self.mobile}\nDriver address is :")
        for (k, v) in self.address.items():
            print(f"{k} : {v}")
        print("The driver is licenced to drive in the following states:")
        for state in self.states_of_drive:
            print(f"{state}", end=" :  ")
        print()

    def write_driver_info(self):
        sys.stdout = open("DriverInfo.txt", "w")
        self.driver_info()
        sys.stdout.close()
        sys.stdout = stdout_main

    @staticmethod
    def read_driver_info():
        with open("DriverInfo.txt", "r") as file:
            contents = file.read()
            print(contents)


def main():
    input("Press Enter to continue")
    driver1 = Driver(3313377, "Gladys", "Berejkilan", "0414566999", address1, states1, 8)
    driver1.display_current_demerit_points()
    input("Press Enter to continue")
    driver1.decrease_demerit(2)
    driver1.display_current_demerit_points()
    input("Press Enter to continue")
    driver1.increase_demerit(3)
    input("Press Enter to continue")
    driver1.display_current_demerit_points()
    input("Press Enter to continue")
    driver1.driver_info()
    input("Press Enter to continue")
    driver1.write_driver_info()
    driver1.read_driver_info()

    driver2 = Driver(9877345, "Boris", "Johnson", "0414123456", address2, states2, 3)
    driver2.display_current_demerit_points()
    input("Press Enter to continue")
    driver2.decrease_demerit(2)
    driver2.display_current_demerit_points()
    input("Press Enter to continue")
    driver2.increase_demerit(13)
    driver2.display_current_demerit_points()
    input("Press Enter to continue")
    driver2.driver_info()
    driver2.write_driver_info()
    driver2.read_driver_info()

    car1 = Car("BBJ702", "Mazda", "CX3", 10000, "Hatch", "Blue", "Leather", 5, driver1)
    input("Press Enter to continue")
    car1.vehicle_info()
    input("Press Enter to continue")
    car1.display_color()
    input("Press Enter to continue")
    car1.change_color("White")
    car1.display_color()
    input("Press Enter to continue")
    car1.display_odometer()
    car1.update_odometer(29000)
    car1.display_odometer()
    input("Press Enter to continue")
    car1.car_info()

    car2 = Car("OY0400", "Ford", "Festiva", 39785, "Sedan", "Green", "Fabric", 4, driver2)
    input("Press Enter to continue")
    car2.vehicle_info()
    input("Press Enter to continue")
    car2.display_color()
    input("Press Enter to continue")
    car2.change_color("Black")
    car2.display_color()
    car2.display_odometer()
    car2.update_odometer(10000)
    car2.display_odometer()
    input("Press Enter to continue")
    car2.car_info()

    truck1 = Truck("XJBJ882", "Kenworth", "BigMother5000", 150000, "40 tonnes", 5, 18, driver1)
    input("Press Enter to continue")
    truck1.vehicle_info()
    input("Press Enter to continue")
    truck1.display_odometer()
    truck1.update_odometer(15000)
    truck1.display_odometer()
    input("Press Enter to continue")
    truck1.truck_info()

    truck2 = Truck("ARC542", "Hyundai", "iLoad", 76520, "2 tonnes", 2, 4, driver2)
    input("Press Enter to continue")
    truck2.vehicle_info()
    truck2.display_odometer()
    truck2.update_odometer(-29000000)
    truck2.display_odometer()
    input("Press Enter to continue")
    truck2.truck_info()


if __name__ == "__main__":
    main()
