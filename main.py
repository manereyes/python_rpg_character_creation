### Epic RPG Character creator ###

class Character:
        name = ""
        race = ""
        char_class = ""
        weapon = ""
        job = ""
        background = ""
        

def char_creation(name, race, char_class, weapon, job, background):
    character = Character()
    character.name = name
    character.race = race
    character.char_class = char_class
    character.weapon = weapon
    character.job = job
    character.background = background
    return character

def char_list(new_char):
    print("\n\n--New Character Created--\n")
    print("Name: " + new_char.name)
    print("Race: " + new_char.race)
    print("Class: " + new_char.char_class)
    print("Weapon: " + new_char.weapon)
    print("Job: " + new_char.job)
    print("Background: " + new_char.background)

def main():
    name = input("Your Character's name: ")
    race = input("Your Character's race: ")
    char_class = input("Your Character's class: ")
    weapon = input("Your Character's weapon: ")
    job = input("Your Character's job: ")
    background = input("Your Character's background: ")
    new_char = char_creation(name, race,char_class, weapon, job, background)
    char_list(new_char)




if __name__ == "__main__":
    main()