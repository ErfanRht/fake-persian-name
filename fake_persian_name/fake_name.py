from importlib import resources
import random
import io
import os

def generate_name(gender):
    if gender == "male":
        gender = 0
    elif gender == "female":
        gender = 1
    elif gender == "random":
        gender = random.randint(0, 1)
    else:
        return "The entered argument is not true. Please read the documentation of this package at PYPI.org"

    basedir = os.path.abspath(os.path.dirname(__file__))
    files = ["name_boy.txt","name_girl.txt"]
    def first_name(gender):
        with resources.open_text('fake_persian_name',files[gender]) as file:
            names = file.read().split("\n")
        first_name = names[random.randrange(len(names))]

        return first_name
    
    def last_name():
        with resources.open_text('fake_persian_name',files[gender]) as file:
            names = file.read().split("\n")
        last_name = names[random.randrange(len(names))]+"ی"

        return last_name
    
    first = first_name(gender)
    last = last_name()
    name = first + " " + last

    return name