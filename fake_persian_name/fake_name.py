import random

class FakePersianName(gender):
    files = ["name_boy.txt", "name_girl.txt"]
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

    class generate_name():
        first = first_name(gender)
        last = last_name()
        name = first + " " + last

if __name__ == "__main__":
    pass