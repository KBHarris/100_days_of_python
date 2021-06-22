print("\n                                                                    Welcome to S.W.A.T Breach! \n")
choice1 = input("You approach the terrorist hideout undetected and stack up on the front entrance. Do you breach with your SHOTGUN or slowly open the DOOR? ")

if choice1.lower() == 'shotgun':
    print("\nYou blow the hinges off the door with your shotgun, you don't notice the now armed grenade taped to the inside door frame as you enter. Two steps later you're filled with shrapnel. \n")
    print("                                                                           GAME OVER")
    exit()
elif choice1.lower() == 'door':
    print("\nYou slowly open the door and luckily notice a frag grenade tripwire trap taped to the inside door frame. You clip the tripwire and enter the room.")

choice2 = input('\nYou approach a "T" intersection in the hallway. Do you go LEFT or RIGHT? ')

if choice2.lower() == "left":
    print("\nYou peek left and catch a terrorist guard by surprise and drop him.")
elif choice2.lower() == "right":
    print("\nYou turn right down the hall, even as you do you know that you made a mistake by not checking your six. Before you can react, two rounds rip through the back of your vest. Should have put in your back plates. \n")
    print("                                                                           GAME OVER")
    exit()

choice3 = input("\nA terrorist, now alerted by your gunshots, screams that he has a hostage. You peek into the room to see him hiding behind a man with a pistol to his head. You can FLASHBANG the terroist, enter the room and SHOOT him in the head, or shoot the HOSTAGE. ")

if choice3.lower() == "flashbang":
    print("\nYou prep a flashbang and roll it into the room. Unfortunatly, the terrorist reacts fast enough to get a few rounds off into the drywall that you are standing behind and you catch one in the neck.\n")
    print("                                                                           GAME OVER")
    exit()
elif choice3.lower() == "shoot":
    print("\nYou step in and fire, sending a round through the hostage's shoulder and into the terrorist causing him to pull the trigger with the gun against the hostage's head. Both collapse on the ground dead. Mission failed.\n")
    print("                                                                           GAME OVER")
    exit()
elif choice3.lower() == "hostage":
    print("\nYou step into the door way and fire a round into the hostage's leg causing him to collapse, this stuns the terroist long enough for you to take him out. You lead the hostage to safety.\n")
    print("                                                           You're deeply nuts, you know that? Shoot the hostage....\n")
    print("                                                                           Mission Accomplished!")