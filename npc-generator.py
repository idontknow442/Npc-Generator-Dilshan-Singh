import random
age = [14,53,12,43,93,29,49,19,29,59,96,95,43,12,5,1,6,34,19,20]
#list of ages that an NPC can have

height = [5.0,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,5.10,5.11,6.0,6.1,6.2,6.3,6.4,6.5,6.6]
#list of heights that an NPC can have

haircolor = ['Black','Brown','Blonde','Pink','Green','Purple','Orange','Red','Blue']
#list of hair colors that an NPC can have

superpower = ['Night Vision','Teleportation','Invisibility','Invicibility','Telekinesis','Super Strength','Flight','Time Travel']
#list of superpowers that an NPC can have

race = ['African','Asian','Hispanic','American']
#list of races that an NPC can have

numberofnpc = 0
while numberofnpc < 10:
    numberofnpc +=1
#makes it repeat 10 times    

    name1 = input('\nEnter name of NPC: ')
    print('Age:',random.choice(age))
    print('Height:',random.choice(height))
    print('Hair Color:',random.choice(haircolor))
    print('Super Power:',random.choice(superpower))
    print('Race:',random.choice(race))
#asks for name and prints additional random attributes
