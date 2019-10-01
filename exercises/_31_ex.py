###~~~Making Decisions~~~###

print("""You enter a dark room with two doors. 
Do you go through door #1 or door #2?!?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a chocolate One Piece Cake")
    print("What do you do?")
    print('1. Go into Second Gear and give the bear the ol\' "Lucci Gattling Gun"')
    print("2. Run over and eat the rest of the cake in One Bite")

    bear = input("> ")

    if bear == "1":
        print('Ooooff!! The giant bear went into Third Gear \"Snake Man\" & King Cobra\'d you to death... feels bad.')
    elif bear == "2":
        print("The giant bear hit you with the ol' Conquerer's Haki and you soiled yourself before you could get to the cake... feels bad.")
    else:
        print("Well the giant bear revealed himself to actually be Bepo from Law's crew. Bepo gave you the rest of the cake since you'll be King of the Pirates on day! Believe it! ")

elif door == "2":
    print("Link, savior of Hyrule, asks you to join him on his quest to save Zelda")
    print("1. Hell Yea Link! I'll join you on your adventure!")
    print("2. I don't know... I'm about as soft as cupcakes...")
    print("3. Whip out your ocarina & drop a fiyah beat!")

    decision = input("> ")

    if decision == "1" or decision == "2":
        print("You frantically grab a Remote Bomb & run around the room scream \"For Narnia! For Narnia!")
        print("KaBoom Boom!!")
        print("... Wasted...")
    else:
        print("Link busted out with a freestyle flow so hot, you 2 uploaded it to your guys new Soundcloud page.")
        print("Track so LIT, it burnt all of Hyrule down... killing Princess Zelda")
        print("Hyrule Gang Hyrule Gang Hyrule Gang Hyrule Gang Hyrule Gang!!!")
        print("...")
        print("Ganondorf joined the squad")
else:
    print("While contemplating your decision, you hear Rick Jame yell \"CHARLIE MURPHY!!\"")
    print("Rick James punched you in the face!")
    print("Unity!!")