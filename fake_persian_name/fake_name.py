import random
import os

class FakePersianName():
    def __init__(self, gender):
        if gender == "male":
            self.gender = 0
        elif gender == "female":
            self.gender = 1
        elif gender == "random":
            self.gender = random.randint(0, 1)
        else:
            self.gender = None

    def generate_name(self):
        if self.gender == None:
            return None
        basedir = os.path.abspath(os.path.dirname(__file__))
        files = [os.path.join(basedir, "name_boy.txt"), os.path.join(basedir, "name_girl.txt"),]
        def first_name(gender):
            with open(files[self.gender], 'r') as file:
                names = file.read().split("\n")
            first_name = names[random.randrange(len(names))]

            return first_name
        
        def last_name():
            with open(files[random.randint(0, 1)]) as file:
                names = file.read().split("\n")
            last_name = names[random.randrange(len(names))]+"ی"

            return last_name
        
        first = first_name(self.gender)
        last = last_name()
        name = first + " " + last

        return name