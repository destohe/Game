# imports from the random&time class
import random
import time

# initializing global variables
user_health = 100
enemy_health = 100
battle_continue = True


class BattleGame:
    # constructor
    def __init__(self, attack_options):
        self.attack_options = attack_options

    # methods
    def offense(self):
        if self.attack_options == 1:
            offense_damage = random.randint(18, 25)
            return offense_damage

        elif self.attack_options == 2:
            offense_damage = random.randint(10, 35)
            return offense_damage

    def heal(self):
        health_regen = random.randint(16, 32)
        return health_regen

    def timer(self):
        sleep_time = random.randrange(1, 3)
        print('\nAI choosing attack.....!')
        time.sleep(sleep_time)

# try and except so if an integer is entered it will return true and if a string is entered it will expect it and
# return as false
def parse_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

# checks for valid integers and if a string is found will return error message and prompt the user again
def check_for_valid_input():
    valid_input = False
    while valid_input is False:
        choice = input('\nSelect an attack: ')
        if parse_int(choice) is True:
            return int(choice)
        else:
            print('Invalid choice! your turn is lost.')


# while loop set to true to keep prompting the user to enter an attack.
while battle_continue:
    print('\nOffense Choices\n1. Close range attack\n2. Far range attack\n3. Heal')
    # take the input in as a string and convert to integer
    attack_options = check_for_valid_input()

    # if health is over 80 it will focus on attacking
    if enemy_health < 80:
        enemy_choice = random.randint(1, 2)
    else:
        enemy_choice = random.randint(1, 3)

    # creating an object for enemy
    enemy_fighter = BattleGame(enemy_choice)
    # creating an object for user
    user_fighter = BattleGame(attack_options)
    # initializing local variables
    damage_to_enemy = 0
    damage_to_user = 0
    heal_user = 0
    heal_enemy = 0

    # if the user inputs 1 or 2 the user will deal damage to the enemy
    if attack_options == 1:
        damage_to_enemy = user_fighter.offense()
        heal_user = 0
        print('You inflicted damage to the enemy with a normal attack!', damage_to_enemy, 'damage.')

    elif attack_options == 2:
        damage_to_enemy = user_fighter.offense()
        heal_user = 2
        print('This was a risk! but you got the job done and inflicted damage to the enemy!', damage_to_enemy, 'damage')

    # if the enemy is assigned an attack the user will deal damage to the user
    if enemy_choice == 1 or enemy_choice == 2:
        damage_to_user = enemy_fighter.offense()
        heal_enemy = 0
        print('Enemy has inflicted damage to you!', damage_to_user, 'damage.')

    # if 3 is entered by the user will heal but the AI will be able still to deal damage
    if attack_options == 3:
        heal_user = user_fighter.heal()
        damage_to_enemy = 0
        print('You regened but the enemy may have inflicted damage!', heal_user, 'health points.')

    # if 3 is entered by the enemy will heal but the user will be able still to deal damage
    if enemy_choice == 3:
        heal_enemy = enemy_fighter.heal()
        damage_to_user = 0
        print('The enemy has regened health', heal_enemy, 'health points.')

    # if an invalid number is entered by the user will miss it's turn while the AI will still deal damage
    if attack_options != 1 and attack_options != 2 and attack_options != 3:
        print('Invalid choice! your turn is lost.')

    else:
        enemy_fighter.timer()

    # take away users health from damage done and then add heal user
    user_health = user_health - damage_to_user + heal_user
    # take away AI's health from damage done and then add heal AI
    enemy_health = enemy_health - damage_to_enemy + heal_enemy

    # if health is greater than 100 than let it equal to 100
    if user_health > 100:
        user_health = 100

    # if health is less than or equal 0 the battle will end and exit the loop
    elif user_health <= 0:
        user_health = 0
        battle_continue = False

    # if health is greater than 100 than let it equal to 100
    if enemy_health > 100:
        enemy_health = 100

    # if health is less than or equal 0 the battle will end and exit the loop
    elif enemy_health <= 0:
        enemy_health = 0
        battle_continue = False

    print("\n*** Current Health ***")
    print("User:", user_health)
    print("AI:", enemy_health)

print("*** Final Health ***")
print("User:", user_health)
print("AI:", enemy_health)

if user_health < enemy_health:
    print("\nYou lost! Play again?")

elif user_health == enemy_health:
    print("\nDraw, you must fight again")

else:
    print('\nYou won against the AI!')
