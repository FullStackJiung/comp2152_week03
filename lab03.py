import random

# Dice options using list() and range()
diceOptions = list(range(1, 7))

# Weapons array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

print("Available Weapons:", ', '.join(weapons))

# Inputs combat strength hero
combatStrength = int(input("Enter your combat strength (1-6); "))
if combatStrength < 1 or combatStrength > 6:
    print("Invalid input! Combat strength should be between 1 and 6.")
    combatStrength = 1 #Default value for invalid input

    
# Input combat strength for monster
mCombatStrength = int(input("Enter moster's combat strength (1-6)"))
if mCombatStrength < 1 or mCombatStrength > 6:
    print("Invalid input! Monster Combat strength should be between 1 and 6.")
    mCombatStrength = 1 #Default value for invalid input




# # Simulate Battle
for j in range(1, 21, 2): #Simulation of 20 rounds, stepping by 2
    # Dice rolls for hero and monster
    heroRoll = random.choice(diceOptions) 
    monsterRoll = random.choice(diceOptions) 

    # Calculate the weapons
    heroWeapon = weapon(heroRoll - 1)
    monsterWeapon = weapon(monsterRoll - 1)

    # Calculate total strength
    heroTotal = combatStrength + heroRoll
    monsterTotal = combatStrength + monsterRoll

    # Print round details
    print("\n Round {j} Hero rolled {heroRoll}, Monster rolled {monsterRoll}")
    print("Hero selected: {heroWeapon}, Monster selected: {monsterWeapon}")
    print("Hero total strength: {heroTotal}, Monster total strength: {monsterTotal}")

    # Determine winner
    if heroTotal > monsterTotal:
        print ("hero wins!")
    elif heroTotal < monsterTotal:
        print("Monster wins the round")
    else:
        print("It's a tie!")

    if j ==11:
        print("\n Battle Truce declread in Round 11. Game Over!")
        break

if j != 11:
    print("\n Battle concluded after 20 round!")
        
# for j in range(1, 21, 2):
#     heroRoll, monsterRoll = random.choice(diceOptions), random.choice(diceOptions)
#     heroTotal, monsterTotal = combatStrength + heroRoll, mCombatStrength + monsterRoll
#     print(f"Round {j}: Hero({weapons[heroRoll - 1]})={heroTotal}, Monster({weapons[monsterRoll - 1]})={monsterTotal}.", 
#           "Hero wins!" if heroTotal > monsterTotal else "Monster wins!" if heroTotal < monsterTotal else "Tie!")
#     if j == 11:
#         print("Battle Truce declared. Game Over!")
#         break