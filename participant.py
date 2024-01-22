
# Class to represent a participant in the iowa gambling task
class TrialParticipant: 

    # No. of participants
    instances_of_participants = 0 
    
    # Initialise variables for participant
    def __init__(self, fullname="John Doe",position = 1, winnings=2000, decks= None):
        self.fullname = fullname
        self.participant_num = TrialParticipant.instances_of_participants
        self.keypresses = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.position = position
        self.winnings = winnings
        self.decks = decks

    # String representation of participant info 
    def __str__(self):
        return f"Participant {self.participant_num}: {self.fullname}, Position: {self.position}, Winnings: {self.winnings}, Keypresses: {self.keypresses}"

    # Shows participant no., name and bank total
    def display_winnings(self): 
        print(f"\nParticipant: {self.participant_num}, Name: {self.fullname}, Bank: {self.winnings}")
    
    # Changes deck position as needed
    def increment_position(self): 

        # Increment position
        self.position += 1 

        # If position greater than or equal decks available, stop method
        if self.position >= len(self.decks): 
            return False
        
        # If position less than decks available, keep incrementing
        return True 
    
    # Gets deck position
    def get_position(self): 
        return self.position

    '''FEATURE 1 METHOD'''
    #Sets decks for new decks option
    def set_decks(self, decks): 
        self.decks = decks
    
    # Returns value for deck user has chosen
    def choose_deck(self, deck): 

        # Deck changed to uppercase for method to read
        deck = deck.upper()

        # If Deck is in one of the four options, the value of that character in that deck position is returned
        if deck in ["A", "B", "C", "D"]:
            return self.decks[self.get_position()][deck]
        
        # If a character that isn't valid is entered, error message displayed - no value added or lost to bank
        else:
            print("\n" + "Please enter A, B, C or D to continue" + "\n")

            # Position reset back by 1
            self.reset()
            return [0, 0]
        
    # Updates winnings based on win/lose amount
    def update_bank(self, win_lose): 
        self.winnings += int(win_lose[0])
        self.winnings -= int(win_lose[1])

        # Displays win/lose amount clearly
        print("\n" + "You won:", win_lose[0])
        print("\n" + "You lost:", win_lose[1])

        return self.winnings
    
    '''FEATURE 2 METHOD'''
    # Method used to update winnings when new decks are called
    def update_winnings(self, new_winnings=1000):
        self.winnings += new_winnings
        print(f"\nThank you for continuing, here is a gift of {new_winnings}!\nBank updated to {self.winnings}.")

    # Returns list of keypresses
    def get_keypresses(self):
        keypresses_list = [(char, count) for char, count in self.keypresses.items()]
        return keypresses_list

    # Resets deck position
    def reset(self):
        #Goes back by 1 position each time an invalid char is pressed (as shown in choose_deck)
        self.position -= 1
        
    '''FEATURE 1 METHOD'''
    #Resets position to 1 for new deck option
    def reset_position(self):
        self.position = 1


    # Records character pressed into keypresses dictionary
    def record_key(self, char_pressed):

        # Character pressed is changed to lower case
        char_pressed = char_pressed.lower() 

        # If char pressed is in list, added to kp dict
        if char_pressed in ["a", "b", "c", "d"]: 
            self.keypresses[char_pressed.lower()] += 1 

        # If char pressed invalid, code is interrupted with error
        else:
            print("Invalid key pressed. Use 'a', 'b', 'c', or 'd'.") 
            exit

    # Records the largest amount of keys pressed in [a, b, c, or d]
    def most_frequent_keys(self):

        # Stores max count as variable from keypress dict
        max_count = max(self.keypresses.values())

        # Stores character with max count in most_freq_chars variable to be returned
        most_frequent_chars = [(char, count) for char, count in self.keypresses.items() if count == max_count]
        return most_frequent_chars

    # Records the least amount of keys pressed in [a, b, c, or d]
    def least_frequent_keys(self):
        min_count = min(self.keypresses.values())
        least_frequent_chars = [(char, count) for char, count in self.keypresses.items() if count == min_count]
        return least_frequent_chars

    # Returns full name
    def get_full_name(self):
        return f"{self.fullname}"

    # Sets full name and returns it
    def set_full_name(self, full_name):
        full_name = self.fullname
        return f"{self.fullname}"
    
    # Property variable 
    full_name = property(get_full_name, set_full_name)

    
