import random
import os

def generate_name(gender):
    if gender == "male":
        gender = 0
    elif gender == "female":
        gender = 1
    elif gender == "random":
        gender = random.randint(0, 1)
    else:
        return None

    basedir = os.path.abspath(os.path.dirname(__file__))
    files = [os.path.join(basedir, "name_boy.txt"), os.path.join(basedir, "name_girl.txt"),]
    def first_name(gender):
        with open(files[gender], 'r') as file:
            names = file.read().split("\n")
        first_name = names[random.randrange(len(names))]

        return first_name
    
    def last_name():
        with open(files[random.randint(0, 1)]) as file:
            names = file.read().split("\n")
        last_name = names[random.randrange(len(names))]+"ی"

        return last_name
    
    first = first_name(gender)
    last = last_name()
    name = first + " " + last

    return name