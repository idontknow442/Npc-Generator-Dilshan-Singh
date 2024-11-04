# Npc-Generator

## Highlights

 If you are looking for an npc generator, this is what I made.

 This code was made by "idontknow442"
  
 I made a project that generates 10 npcs which include 6 different attributes.
 
 I made this npc generator using python code.
 
 This project consists of a short 28 lines and gets the job done.

## Overview

I made a generator that makes 10 npcs with random attributes using python. I used [while loop](#While-Loop-Explained) to make 10 npcs.

This generator I made consists of 6 attributes which are listed below

 - [Name](#Name-Explained)
 
 - [Age](#Age-Explained)
 
 - [Height](#Height-Explained)
 
 - [Hair Color](#Hair-Color-Explained)
 
 - [Super Power](#Super-Power-Explained)
 
 - [Race](#Race-Explained)

### While Loop Explained

 I made a while loop to make the code repeat 10 times. I did this by making a variable called "numberofnpc" equal to 0. Then I made it so
 if the value of the variable was less than 10, than it would repeat and everytime the loop repeats, the value of the variable adds by 1 until 10.
     
        numberofnpc = 0
    while numberofnpc < 10:
        numberofnpc +=1

### Name Explained

 I simply just made an input for the name of the npc as shown.

     name1 = input('\nEnter name of NPC: ')

### Age Explained

 For the age, the first thing I did was make a list of ages and put it into a variable.

     age = [14,53,12,43,93,29,49,19,29,59,96,95,43,12,5,1,6,34,19,20]

 Then inside the while loop, I made it print a random age from the list for the npc.

     print('Age:',random.choice(age))

 ### Height Explained
 
 For the height I made a list of heights and put it into a variable.

     height = [5.0,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,5.10,5.11,6.0,6.1,6.2,6.3,6.4,6.5,6.6]

 Then inside the while loop, I made it print a random height from the list for the npc.

     print('Height:',random.choice(height))

 ### Hair Color Explained

 For the hair color, I made a list of different hair colors and put it into a variable called haircolor.

     haircolor = ['Black','Brown','Blonde','Pink','Green','Purple','Orange','Red','Blue']
 
 Then inside the while loop, I made it print a random hair color from the list for the npc.

     print('Hair Color:',random.choice(haircolor))

 ### Super Power Explained

 For the super power, I made a list of different super powers and put it into a variable.

     superpower = ['Night Vision','Teleportation','Invisibility','Invicibility','Telekinesis','Super Strength','Flight','Time Travel']
 
 Then inside the while loop, I made it print a random super power from the list for the npc.

     print('Super Power:',random.choice(superpower))

 ### Race Explained

 For the race, I made a list that contained 4 different races and put it into a variable.

     race = ['African','Asian','Hispanic','American']
 
 Then inside the while loop, I made it print a random race from the list for the npc.

     print('Race:',random.choice(race))

 ## I Hope You Enjoyed!
