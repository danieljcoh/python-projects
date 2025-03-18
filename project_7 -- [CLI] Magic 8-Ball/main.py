from random import randint

def shake_8_ball():
    question = input("What would you like to know? ")
    list = ["Definitely!", "Probably", "Ehh, IDK", "Ha--, You wish!", "Probably-Not", "No!",
            "Definitely not!", "Likely", "Not likely!", "NO!"]
    
    random_indx = randint(0, len(list) - 1)
    print(list[random_indx])

shake_8_ball()
    
    