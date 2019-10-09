###~~~Designing & Debugging (My Own Game)~~~###

from sys import exit

def snuffles():
    print('You are confronted by Snuffles')
    print('He asks you "Where are your balls Bark Bark?"')
    print('Bark Bark stop to ponder and think about where did his balls go.')
    print('Snuffles procedes to talk to you how humans have been treating dogs and tries to convince you to join him on his planet of intelligent dogs in another dimensions.')
    print('What will Bark Bark do?')

    choice = input('(go or stay)> ')

    if choice == 'go':
        print('Bark Bark abandoned his Dumb Dumb Rafi and joins Snuffles.')
        print("Bark Bark goes on to overthrow Snuffles & became the new leader of the intelligent dogs")
        print("Bark Bark clones a copy of his Dumb Dumb Rafi for every dog because he still misses and loves his Dumb Dumb deeply.")
        print('"You will be missed... Rafi"')
        exit(0)

    elif choice == "stay":
        print("This angers Snuffles")
        print('With only one option left for Snuffles, he declares a fight to the death!')
        print('What will Bark Bark do now?')

        choice2 = input('(fight or refuse)> ')
        if choice2 == 'refuse':
            print('Bark Bark refuses to fight. Hugs & luvs is all Bark Bark is about!')
            print('Snuffles laughs at Bark Bark.')
            print('With Bark Bark refusing to fight, Snuffles does the unimaginable.')
            print('Snuffles grabs Dumb Dumb Rafi and teleports back to his intelligent dog planet, leaving Bark Bark alone until his last breathe.')
            print('But just as the portal was about to close, Bark Bark ran in!')
            print('Snuffles allows Dumb Dumb Rafi to live but will be a prisoner for the rest of his life. Snuffles allows Bark Bark to visit Rafi over other weekend')
            print('Bark Bark & Rafi die a sad and lonely death.')
            exit(0)
        
        elif choice == 'fight':
            print('Just before the final showdown begins, something magical begins to happen.')
            print('All the items collected by Bark Bark begin to glow and start to merge together.')
            print('Alas! The items turned into a mech suit for Bark Bark to wear into battle!')
            print('Bark Bark and Snuffles clash it out for 7 days, and 7 nights.')
            print('Bark Bark and Snuffles begin to charge up and go in for their final attack!')
            print('Which final attack will Bark Bark use?')

            choice3 = input('(kamehameha or fire hawk)> ')
