from potions import magical_potions
from name_maker import grant_a_name
from random import randint

def main():
    choice_1 = input("Do you want to create your own name or be granted one? (c: to create, g: grant): ").lower()
    if choice_1 == "c":
        name = input("What is your name: ")
    else:
        grant_a_name()

    player_magic_power = randint(15, 200)
    print(f"Welcome back, Alchemist {name}.")
    answer = input("What would you like to do? View available potions (view) or use one (use): ").lower()

    if answer == "view":
        print("How would you like to view them sorted? ")
        view_option = input("Magic power (mp), rarity (r), or potency(p): ").lower()
        if view_option == "mp":
            sorted_potions = sorted(magical_potions, lambda item: item["magical_power_needed"], reverse=True) # most potent first
        elif view_option == "r":
            sorted_potions = sorted(magical_potions, lambda item: item["rarity"], reverse=True)
        elif view_option == "p":
            sorted_potions = sorted(magical_potions, lambda item: item["potency"], reverse=True)


if __name__ == "__main__":
    main()

