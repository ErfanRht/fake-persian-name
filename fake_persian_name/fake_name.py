from importlib import resources
import requests
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
        return None

    url = "https://raw.githubusercontent.com/jadijadi/persianwords/master/"

    file = ["name_boy.txt","name_girl.txt"]
    suffix = ["زاده", "پور" ,"" ,"خوانی", "صفت",  ""]

    def first_name(gender):
        """
        with resources.open_text('fake_persian_name',files[gender]) as file:
            names = file.read().split("\n")
        """
        names = (requests.get(url+file[gender]).text).split("\n")
        first_name = names[random.randrange(len(names))]

        return first_name
    
    def last_name():
        names = (requests.get(url+file[gender]).text).split("\n")
        last_name = names[random.randrange(len(names))]
        if last_name[len(last_name)-1] == "ی" or last_name[len(last_name)-1] == "ه":
            last_name = last_name + ("ی" if random.randrange(2) != 1 else "")
        last_name = last_name + " " + suffix[random.randrange(len(suffix))]

        return last_name
    
    first = first_name(gender)
    last = last_name()
    name = first + " " + last

    return name