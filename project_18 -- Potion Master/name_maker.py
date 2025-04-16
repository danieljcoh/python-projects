import string
import time
import random

def grant_a_name():
    
    name_length = random.randint(3,7)
    vowels = "aeiouy"
    possible_chars = string.ascii_lowercase
    name = ""
    
    for i in range(name_length):
        if i % 2 == 0 or i % 3 == 0:
            random_choice = random.choice([True, False])
            if random_choice:
                name += random.choice(vowels)
            else:
                name += random.choice(possible_chars) 
        else:
            name += random.choice(possible_chars)

    name = name.title()
    print("Your name shall be...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print(name)
    return name