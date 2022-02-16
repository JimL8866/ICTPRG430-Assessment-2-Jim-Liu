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
    def __init__(self, rego, make, model, current_odometer):
        self.rego = rego
        self.make = make
        self.model = model
        self.current_odometer = current_odometer
        self.driver = None

    def display_odometer(self):
        print(f"The vehicle current odometer is {self.current_odometer} ")

    def update_odometer(self, km):
        self.current_odometer += km
        if self.current_odometer < 0:
            print("The odometer is not valid ")
        else:
            print(f"The vehicle current odometer is {self.current_odometer} ")


class Car(Vehicle):
    def __init__(self, rego, make, model, current_odometer, body_type, color, upholstery, num_of_doors, driver):
        super().__init__(rego, make, model, current_odometer)
        self.body_type = body_type
        self.color = color
        self.upholstery = upholstery
        self.number_of_doors = num_of_doors
        self.driver = driver

    def display_color(self):
        print(f"The color of the car is {self.color}")

    def change_color(self, c_color):
        self.color = c_color

    def car_general_info(self):
        print(
            f"Vehicle registration number {self.rego} is a {self.make}.Model is {self.model}.Odometer {self.current_odometer} km")

    def car_spec_info(self):
        print(f"The car details are: {self.body_type}, {self.color}, {self.upholstery}, {self.number_of_doors}")

    def car_with_driver(self):
        self.car_general_info()
        print(
            f"The driver of the vehicle is {self.driver.f_name} {self.driver.f_name}\nDriver License number: {self.driver.licence_number}")
        print("Additional details:")
        self.car_spec_info()


class Truck(Vehicle):
    def __init__(self, rego, make, model, current_odometer, max_load_cap, num_of_axles, num_of_wheels, driver):
        super().__init__(rego, make, model, current_odometer)
        self.max_load_cap = max_load_cap
        self.num_of_axles = num_of_axles
        self.num_of_wheels = num_of_wheels
        self.driver = driver

    def truck_general_info(self):
        print(
            f"Vehicle registration number {self.rego} is a {self.make}.Model is {self.model}.Odometer {self.current_odometer} km")

    def truck_spec_info(self):
        print(f"The truck details are: {self.max_load_cap}, {self.num_of_axles}, {self.num_of_wheels}")

    def truck_with_driver(self):
        self.truck_general_info()
        print(
            f"The driver of the vehicle is {self.driver.f_name} {self.driver.f_name}\nDriver License {self.driver.licence_number}")
        print("Additional details:")
        self.truck_spec_info()


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

    def display_all_info(self):
        print(f"The driver {self.f_name} {self.l_name}, has a driver licence number : {self.licence_number}Contact "
              f"phone number is : {self.mobile}\nDriver address is : ")
        self.display_address()

    def display_address(self):
        for (k, v) in self.address.items():
            print(f"{k} : {v}")

    def display_states_of_drive(self):
        print("The driver is licenced to drive in the following states:")
        for state in self.states_of_drive:
            print(f"{state}:")

    def display_current_demerit_points(self):
        print(f"The driver {self.f_name} {self.l_name} 's current demerit points is {self.current_demerit_points}")

    def decrease_demerit(self, number):
        self.current_demerit_points -= number
        if self.current_demerit_points < Driver.min_demerit_points:
            print(f"Demerit points should not be allowed to fall below {Driver.min_demerit_points}")

        elif self.current_demerit_points > Driver.demerit_warning:
            print("License suspension is imminent")
        else:
            print(f"The driver {self.f_name} {self.l_name} 's current demerit points is {self.current_demerit_points}")

    def increase_demerit(self, number):
        self.current_demerit_points += number
        if self.current_demerit_points > Driver.max_demerit_points:
            print(f"Demerit points should not be allowed to increase beyond {Driver.max_demerit_points}")
        elif self.current_demerit_points > Driver.demerit_warning:
            print("License suspension is imminent")
        else:
            print(f"The driver {self.f_name} {self.l_name} 's current demerit points is {self.current_demerit_points}")


def main():
    driver1 = Driver(3313377, "Gladys", "Berejkilan", "0414566999", address1, states1, 8)
    driver1.display_all_info()
    input("Press Enter to continue")
    driver1.display_address()
    input("Press Enter to continue")
    driver1.display_states_of_drive()
    input("Press Enter to continue")
    driver1.display_current_demerit_points()
    input("Press Enter to continue")
    driver1.decrease_demerit(2)
    input("Press Enter to continue")
    driver1.increase_demerit(3)
    input("Press Enter to continue")

    driver2 = Driver(9877345, "Boris", "Johnson", "0414123456", address2, states2, 3)
    driver2.display_all_info()
    input("Press Enter to continue")
    driver2.display_address()
    input("Press Enter to continue")
    driver2.display_states_of_drive()
    input("Press Enter to continue")
    driver2.display_current_demerit_points()
    input("Press Enter to continue")
    driver2.decrease_demerit(2)
    input("Press Enter to continue")
    driver2.increase_demerit(3)

    car1 = Car("BBJ702", "Mazda", "CX3", 10000, "Hatch", "Blue", "Leather", 5, driver1)
    input("Press Enter to continue")
    car1.display_color()
    car1.change_color("White")
    input("Press Enter to continue")
    car1.display_color()
    input("Press Enter to continue")
    car1.car_general_info()
    input("Press Enter to continue")
    car1.car_spec_info()
    input("Press Enter to continue")
    car1.car_with_driver()

    car2 = Car("OY0400", "Ford", "Festiva", 39785, "Sedan", "Green", "Fabric", 4, driver2)
    input("Press Enter to continue")
    car2.display_color()
    car2.change_color("White")
    input("Press Enter to continue")
    car2.display_color()
    input("Press Enter to continue")
    car2.car_general_info()
    input("Press Enter to continue")
    car2.car_spec_info()
    input("Press Enter to continue")
    car2.car_with_driver()

    truck1 = Truck("XJBJ882", "Kenworth", "BigMother5000", 150000, "40 tonnes", 5, 18, driver1)
    input("Press Enter to continue")
    truck1.truck_general_info()
    input("Press Enter to continue")
    truck1.truck_spec_info()
    input("Press Enter to continue")
    truck1.truck_with_driver()
    input("Press Enter to continue")

    truck1.display_odometer()
    input("Press Enter to continue")
    truck1.update_odometer(20000)

    truck2 = Truck("ARC542", "Hyundai", "iLoad", 76520, "2 tonnes", 2, 4, driver2)
    input("Press Enter to continue")
    truck2.truck_general_info()
    input("Press Enter to continue")
    truck2.truck_spec_info()
    input("Press Enter to continue")
    truck2.truck_with_driver()
    input("Press Enter to continue")

    truck2.display_odometer()
    input("Press Enter to continue")
    truck2.update_odometer(10000)
    input("Press Enter to continue")


if __name__ == "__main__":
    main()
