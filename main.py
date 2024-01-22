from filereader import DeckFileReader
from participant import TrialParticipant

# Instantiate DeckFileReader to be used with decks file
file_1 = DeckFileReader("Decks.txt")

# Calls the get_filename method
print(file_1.get_filename())  

# Initialise participant info
trial_participant = TrialParticipant("John Doe", 1, 2000, file_1.all_decks())


'''

WELCOME AND CONSENT

'''

# Welcome and consent messages before task begins
welcome_message = "Welcome to the Iowa Gambling Task. Each round you will be asked to select A, B, C, or D, each corresponds to a winning or losing amount."
consent = "Do you wish to participate? Please input Yes or No: "

# User enters whether they consent or not
user_input = input(welcome_message + "\n" + consent).lower()


'''

EXPERIMENT

'''

# If no consent, task terminated
if user_input != "yes":
    print("You did not consent to participate. Exiting the program.")

# If consent given, task starts
else:
    run_experiment = True

    instructions = "Enter one of the following characters to choose your winnings:\n\n---->A   B   C   D<----"
    exit_message = "If you wish to exit task, enter 'q'"

    # Continue message for when first deck dict has finished
    continue_message = "Task has completed, would you like a new set of decks?"

    while run_experiment:
        # Blank space to help readability
        print("\n" * 1)

        # Calls display winnings method
        trial_participant.display_winnings()

        # Calls get_position method
        position = trial_participant.get_position()

        # Display deck position
        print("The deck position is: ", position)

        # Create variable for user response to instructions, include instructions on how to exit
        response = input("\n" + exit_message + "\n\n" + instructions + "\n\n").lower()
        
        # If user enters q, task terminated
        if response.lower() == 'q':
            print("\nFinal winnings:" + str(winnings))
            run_experiment = False

        
        # If user exceeds amount of decks option to continue or terminate 
        elif trial_participant.increment_position() == False:
            new_response = input("\n" + continue_message + "\n\n")
            
            if new_response.lower() == "yes":
             
                # ** Generate a new randomized deck (FEATURE 1) **
                # Calls random_decks from DeckFileReader
                randomized_deck = file_1.random_decks()

                # ** Set new decks (FEATURE 1) **
                trial_participant.set_decks(randomized_deck)

                # ** Update the winnings amount (FEATURE 2) **
                trial_participant.update_winnings()

                # ** Reset position for new decks (FEATURE 1) **
                trial_participant.reset_position()
                print("New set of decks generated.")

            else:
                # User chooses to end - Final winnings shown and task terminated
                print("\nFinal winnings:" + str(winnings))
                run_experiment = False

        else:
            # Store deck chosen from user input in win_lose variable
            win_lose = trial_participant.choose_deck(response)

            # Store winnings in variable, update bank with win, lose amount
            winnings = trial_participant.update_bank(win_lose)
            
            # Record participant's keypresses
            trial_participant.record_key(response)
         
    '''

    EXIT MESSAGE

    '''
    print("Task has completed")
    print("Iowa task terminated.")


'''
Most of the TrialParticipant methods are called above
So I will call the filereader methods below :)

DECKFILEREADER METHODS
'''
# Calls the get_decks_at method
selected_decks = file_1.get_decks_at([1, 3, 5]) 

# Calls the get_range method
selected_range = file_1.get_range([2, 4]) 

# Calls the exclude_decks method
excluded_decks = file_1.exclude_decks([1, 3, 5])  

# Calls the exclude_range method
excluded_range = file_1.exclude_range([2, 4])  

 # Calls the random_decks method
randomized_deck = file_1.random_decks() 