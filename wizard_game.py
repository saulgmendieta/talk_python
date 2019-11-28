import random
import time
from actors import Wizard, Creature, SmallAnimal, Dragon


def print_header():
    print('------------------------------------------')
    print('             WIZARD GAME APP')
    print('------------------------------------------')
    print()


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, scaliness=75, breaths_fire=True),
        Wizard('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)

        print('A {} of level {} has appear from a dark and foggy forest...'.format(
            active_creature.name,
            active_creature.level
        ))

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard hides to recover')
                time.sleep(5)
                print('The wizard have recovered his health')
        elif cmd == 'r':
            print('The wizard {} took the decision to run away'.format(hero.name))
        elif cmd == 'l':
            print('The wizard {} sees the surroundings and sees:'.format(
                hero.name
            ))
            for c in creatures:
                print('* A {} of level {}'.format(
                    c.name,
                    c.level
                ))
        else:
            print('Exiting game')
            break

        if not creatures:
            print('')


def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()
