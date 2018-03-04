# Print welcome...
print "Welcome To:"
print "The SUPER EASY Game! Python 2.7.14 Edition"
print ""
oooh = raw_input("Press Enter To Initiate Play Mode...") # Get Secret Code And/Or Play
print ""
print "Select An Option"
import random # Import Random Number Ability
rannum = random.randint(1,138841) # Generate Random Number For TRUE WIN!
if oooh == "69420": # Checks For Secret Code If Valid, Then Change Random Number Value
    rannum = 69421
if rannum == 69421: # Show WIN and lose if code isnt valid and Show WIN, lose and TRUE WIN! if code is valid
    print "1. WIN 2. lose 3. TRUE WIN!"
else:
    print "1. WIN 2. lose"
print ""
opti = raw_input("Your Option Is ") # Get Option
import time # Allow Code To Sleep
if opti == "1": # Prints "YOU WIN!"
    print "YOU WIN!"
elif opti == "2": # Prints "you lose"
    print "you lose"
elif opti == "3": # TRUE WIN Option
    if rannum == 69421: # If Code Is Valid
        print "YOU TRULY WIN!"
    else: # If Code Isnt Valid
        print "Error! Option Outside Allowed Space!"
        print "Force-Closing Script In 3"
        time.sleep(1)
        print "2"
        time.sleep(1)
        print "1"
        time.sleep(1)
        quit()
else: # Invalid Option
    print "Error! Option Outside Allowed Space!"
    print "Force-Closing Script In 3"
    time.sleep(1)
    print "2"
    time.sleep(1)
    print "1"
    time.sleep(1)
    quit()
# Script Shutdown
print "Closing Script In 3"
time.sleep(1)
print "2"
time.sleep(1)
print "1"
time.sleep(1)
quit()
