import random
import sys
import time

class Character:
    def __init__(self, name, hp, defense):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defense = defense

    def attack(self):
        self.atk = random.randint(1, 20)
        return self.atk
    
    def runAway(self):
        self.defense = self.defense +5

class Fighter(Character):
    def __init__(self):
        self.name = 'Fighter'
        self.hp = 20
        self.defense = 6
        self.description = "Fully armoured figure carrying a broadsword \nand shield, the Fighter is an intimidating sight to behold!\n"
        self.attacking = "You shout as you bring your sword to bear\non your opponent, attempting to cleave them in two!\n"
        self.defending = "You bring your shield up between you and\nyour enemy, preparing for their next attack!\n"

    def damage(self):
        self.dmg = random.randint(1, 10)
        return self.dmg

    def defend(self):
        self.defense = self.defense + 2
        return self.defense

class Rogue(Character):
    def __init__(self):
        self.name = 'Rogue'
        self.hp = 10
        self.defense = 13
        self.description = "Clad in black leather armor and wielding a wickedly \ncurved short sword, the Rogue is the shadow that all monsters fear.\n"
        self.attacking = "Wrapping yourself in shadow, you dash \nforward to slice your enemy in their weak spot!\n"
        self.defending = "Assuming a defensive crouch, you prepare\nfor your enemy's next attack!\n"

    def damage(self):
        self.dmg = random.randint(1, 8)
        return self.dmg

    def defend(self):
        self.defense = self.defense + 2
        return self.defense

class Wizard(Character):
    def __init__(self):
        self.name = 'Wizard'
        self.hp = 6
        self.defense = 10
        self.description = "Seemingly defenseless human, wearing only the \nrobes of his magical order. Many have underestimated \nhim before, but they are no longer around...\n"
        self.attacking = "Calling upon your arcane power, you thrust\nyour palm toward your enemy, and three magical orbs\n fly at your enemy, striking them in the face!\n"
        self.defending = "You call upon your power to create a magical barrier\naround you, preparing for your enemy's attack!\n"

    def attack(self):
        self.atk = 20
        return self.atk

    def damage(self):
        self.dmg = random.randint(3, 6)
        return self.dmg

    def defend(self):
        self.defense = self.defense + 4
        return self.defense

class Monster:
    def __init__(self, name, hp, defense):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defense = defense

    def attack(self):
        self.atk = random.randint(1, 20)
        return self.atk

class Orc(Monster):
    def __init__(self):
        self.name = 'Orc'
        self.hp = 8
        self.defense = 8
        self.description = "Tall and muscular, with mottled green skin and \nsharp teeth, he wields a primitive looking cleaver.\n"
        self.attacking = "The Orc charges, swinging his cleaver at your head!\n"

    def damage(self):
        self.dmg = random.randint(1, 5)
        return self.dmg

class Goblin(Monster):
    def __init__(self):
        self.name = 'Goblin'
        self.hp = 4
        self.defense = 10
        self.description = "A small creature, with dark green skin and black \neyes that promise a slow death, it brandishes \nit's serrated dagger menacingly...\n"
        self.attacking = "Faster than your eye can follow, the \nGoblin attacks with his dagger!\n"

    def damage(self):
        self.dmg = random.randint(1, 4)
        return self.dmg

class Troll(Monster):
    def __init__(self):
        self.name = 'Troll'
        self.hp = 15
        self.defense = 5
        self.description = "This huge, hulking grey mass roars at you, \nspreading spittle and bad breath across the entire field.\n"
        self.attacking = "Bellowing with rage, the beast charges you, claws \nswinging wildly!\n"

    def damage(self):
        self.dmg = random.randint(1, 8)
        return self.dmg

class Spider(Monster):
    def __init__(self):
        self.name = 'Giant Spider'
        self.hp = 15
        self.defense = 9
        self.description = "Standing at nearly nine feet tall, this giant Black Widow looks deadly!"
        self.attacking = "Hissing and clicking madly, it skitters in for a bite!"

    def damage(self):
        self.dmg = random.randint(1, 4)
        return self.dmg

class Owlbear(Monster):
    def __init__(self):
        self.name = 'Owlbear'
        self.hp = 15
        self.defense = 6
        self.description = "This huge bear is covered in feathers and has the head of a great horned \nowl. It's screech is deafening as it barrels onto the field.\n"
        self.attacking = "Screaming its fury, it rakes you with its deadly claws!"

    def damage(self):
        self.dmg = random.randint(2, 5)
        return self.dmg

class Zombie(Monster):
    def __init__(self):
        self.name = 'Zombie'
        self.hp = 25
        self.defense = 7
        self.description = "A rotting corpse of what used to be a man, this \ncreature makes no sound as it shambles slowly toward you."
        self.attacking = "A soft moan escapes the creature as it swings it's arm like a club, trying \nto hit you!"

    def damage(self):
        self.dmg = random.randint(1, 3)
        return self.dmg

class arena:
    def __init__(self):
        tutorial = input("Would you like to read a tutorial? y/n ").lower()
        if tutorial == "y":
            self.tutorial()
        self.user = self.choose()
        self.monster = self.chooseMonster()
        print("Very well, be prepared for a fight to the death!\n")
        time.sleep(2)
        print("From the north, a {}! {} \n".format(self.user.name, self.user.description))
        time.sleep(5)
        print("From the south, a(n) {}! {} \n".format(self.monster.name, self.monster.description))
        time.sleep(4)
        self.action()

    def action(self):
        self.actions = input("You have a few choices, will you: Attack(A)? Defend(D)? or Run Away(R)? ").lower()
        if self.actions == "a":
            print(self.user.attacking)
            self.user.attack()
            time.sleep(1)
            if self.user.atk >= self.monster.defense:
                self.user.damage()
                time.sleep(1)
                print("You have struck the {} for {} damage! \n".format(self.monster.name, self.user.dmg))
                self.monster.hp = self.monster.hp - self.user.dmg
                if self.monster.hp <= 0:
                    time.sleep(1)
                    print("The {} is defeated! \n".format(self.monster.name))
                    time.sleep(1)
                    self.playAgain()
                elif self.monster.hp > 0:
                    self.cont()
            elif self.user.atk < self.monster.defense:
                time.sleep(1)
                print("You missed! \n")
                self.cont()
        elif self.actions == "d":
            time.sleep(1)
            print(self.user.defending)
            self.user.defend()
            self.cont()
        elif self.actions == "r":
            self.user.runAway()
            self.monster.attack()
            self.monster.damage()
            if self.monster.atk > self.user.defense:
                time.sleep(1)
                print("Your retreat attempt was unsuccessful, and you were struck by the {}! \n".format(self.monster.name))
                self.user.hp = self.user.hp - self.monster.dmg
                if self.user.hp <= 0:
                    time.sleep(1)
                    print("Your wounds overcome you, and you die. Game Over! \n")
                    time.sleep(1)
                    self.playAgain()
                elif self.user.hp > 0:
                    time.sleep(1)
                    print("You are down to: {} life! \n".format(self.user.hp))
                    self.action()
            elif self.monster.atk <= self.user.defense:
                time.sleep(1)
                print("Whew! You got away safely! Coward. \n")
                time.sleep(1)
                self.playAgain()
        else:
            print("You did not enter a valid option.")
            self.action()

    def choose(self):
        time.sleep(1)
        print("You must now choose a class!")
        time.sleep(1)
        chosen = input("You can be a Fighter(F), a Rogue(R), or a Wizard(W): ").lower()
        if chosen == "f":
            user = Fighter()
        elif chosen == "r":
            user = Rogue()
        elif chosen == "w":
            user = Wizard()
        else:
            print("You did not enter an available class.")
            main()

        return user

    def chooseMonster(self):
        ran = random.randint(1, 6)
        if ran == 1:
            monster = Orc()
        elif ran == 2:
            monster = Goblin()
        elif ran == 3:
            monster = Troll()
        elif ran == 4:
            monster = Spider()
        elif ran == 5:
            monster = Owlbear()
        elif ran == 6:
            monster = Zombie()
        return monster

    def cont(self):
        time.sleep(1)
        print(self.monster.attacking)
        self.monster.attack()
        if self.monster.atk >= self.user.defense:
            self.monster.damage()
            time.sleep(1)
            print("The {} hit you for {} damage!".format(self.monster.name, self.monster.dmg))
            self.user.hp = self.user.hp - self.monster.dmg
            if self.user.hp <= 0:
                time.sleep(1)
                print("Your wounds overcome you, and you die. Game Over! \n")
                time.sleep(1)
                self.playAgain()
            elif self.user.hp > 0:
                time.sleep(1)
                print("You are down to: {} life! \n".format(self.user.hp))
                self.action()
        elif self.monster.atk < self.user.defense:
            time.sleep(1)
            print("The {} missed it's attack! \n".format(self.monster.name))
            self.action()
        

    def playAgain(self):
        play = input("Would you like to play again? y/n ").lower()
        if play == "y":
            main()
        elif play == "n":
            self.close()
        else:
            print("You did not enter a valid option.")
            self.playAgain()

    def close(self):
        sys.exit()

    def tutorial(self):
        print("Welcome to the wonderful world of Dungeons and Dragons!\n \
This simple game will introduce you to the concepts and \n \
basic strategies of the table-top game that I have \n \
grown up loving. \n \
In this game, you will be introduced to a few \n \
character types, the fair and noble Fighter, the\n \
mysterious, deadly Rogue, and the wise and \n \
knowledgeable Wizard. After choosing which \n \
character you would like to play, you will be presented \n \
with a monster to fight, and three actions: Attack, \n \
Defend, and Run Away. Attack will (obviously) strike out\n \
at your opponent, based on the table-top rules which involve\n \
a random roll result from 1 to 20. Defend will boost your defense\n \
so that you are harder to hit. Run Away, while a cowardly act \n \
for a hero such as yourself, will make you turn and run from the \n \
monster, but watch out! You might just get caught...\n \
Good luck! And happy hunting...\n")

def main():
    print("Welcome to the arena! \n")
    arena()
    
main()

