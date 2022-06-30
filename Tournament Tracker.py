#Tournament Tracker
from os import remove

#create a function to populate an empty dictionary
def dict_function (number):
    dictionary = {}
    names = None
    slot = None

    for i in range (1, number + 1):
        dictionary.update({i : names})

    return(dictionary) 

#Promt User for number of participants
numUsers = int(input("How many participants will there be?: "))
print(f"\nThere are {numUsers} participants slots ready for sign-ups\n")


#initalize empty dictionary and populate txt file with its contents
participantsDict = dict_function(numUsers)

with open("participants.csv", "w") as f:
                for key, value in participantsDict.items():
                    f.write('%s:%s\n' % (key,value))


restartLoop = "y"

while restartLoop == "y":

    print("Participant Menu \n================ \n1. Sign Up \n2. Cancel Sign Up \n3. View Participants \n4. Save Changes \n5. Exit")
    MenuChoice = int(input("\nChoose a number 1-5: "))

    #Sign Up
    if MenuChoice == 1:
        print("\nParticipant Sign Up \n================== \n")
        tempName = str(input("Participant Name: "))
        tempSlot = int(input(f"\n{tempName}'s starting slot: "))

        if participantsDict.get(tempSlot) == None:
            # participantsDict.key = tempSlot
            # participantsDict.value = tempName
            participantsDict.update({tempSlot: tempName})
            print(f"Success: \n{tempName} has been signed up in starting slot #{tempSlot}")

        else:    
            print(f"Error: \nSlot {tempSlot} is filled. Please try again.")
            restartLoop = "y"

    #Cancel Sign Up
    elif MenuChoice == 2:
        tempName = str(input("Participant Name: "))
        tempSlot = int(input("\nSlot #: "))

        if tempSlot in participantsDict.keys():
            print(f"Removing {tempName} from the tournament")
            participantsDict.pop(tempSlot)

        else: 
            print("This participant does not exist") 
    
    #View Participants
    elif MenuChoice == 3:
        tempSlot = int(input(f"Starting slot #[1-{numUsers}]: "))
        tempMin = tempSlot - 6
        tempMax = tempSlot + 5

        #displays range of participants
        if tempMin >= 0 & tempMax <= numUsers: 
            with open("participants.csv", "r") as f:
                lines = f.readlines()[tempSlot-6 : tempSlot+5]
                print(*lines, sep = '\n')
        elif tempMin < 0 & tempMax <= numUsers:
            with open("participants.csv", "r") as f:
                lines = f.readlines()[0:tempSlot+5]
                print(*lines, sep = '\n')
        elif tempMin > 0 & tempMax > numUsers:
            with open("participants.csv", "r") as f:
                lines = f.readlines()[tempSlot-6:numUsers]
                print(*lines, sep = '\n')
        else:
            with open("participants.csv", "r") as f:
                lines = f.readlines()
                print(*lines, sep = '\n')

    #Save Changes
    elif MenuChoice == 4:
        SaveChanges = str(input("Would you like to save your changes to CSV> [y/n]"))
        
        if SaveChanges == "y":
            print("Saving your changes!\n")

            #save the items in dictionary to txt file
            with open("participants.csv", "w") as f:
                for key, value in participantsDict.items():
                    f.write('%s:%s\n' % (key,value))
        
        elif SaveChanges == "n":
            print("will not save")

        else:
            print("Invalid Entry!\n")
            
    #Exit    
    elif MenuChoice == 5:
        print("Exit \n===== \nAny unsaved changes will be lost! \n")
        exitLoop = str(input("Are you sure you want exit? [y/n]: "))

        if exitLoop == "y":
            restartLoop = "n"
        
        elif exitLoop == "n":
            print("\nReturning to the main menu\n")
            restartLoop = "y"
        
        else:
            print("\nInvalid Entry! \n")
            restartLoop = "y"

    #Catch invalid menu choices
    else:
        print("\nInvalid Entry!\n")

else: 
    print("\nGoodbye!")
    restartLoop = "n"
