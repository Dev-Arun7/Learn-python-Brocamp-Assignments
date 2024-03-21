class Home:
    def room1(self):
        width = 100
        breadth = 100
        print('Area of room1:', width * breadth)

    def kitchen(self):
        width = 1222
        breadth = 4888
        print('Area of kitchen:', width * breadth)

class FirstHome(Home):
    def study_room(self):
        width = 200
        breadth = 150
        print('Area of study room:', width * breadth)

class SecondHome(Home):
    def work_area(self):
        width = 150
        breadth = 100
        print('Area of work area:', width * breadth)

first_home = FirstHome()
second_home = SecondHome()

print("First Home:")
first_home.room1()
first_home.kitchen()
first_home.study_room()

print("\nSecond Home:")
second_home.room1()
second_home.kitchen()
second_home.work_area()
