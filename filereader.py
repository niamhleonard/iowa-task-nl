import random
class FileReader:

    def __init__(self, filename):
        self.__filename = filename
        print("instance of FileReader class created!")
    
    def read_all(self):
        try:
            file_1 = open(self.__filename)
            lines = file_1.readlines()
            file_1.close()
            return lines
        except:
            print("file not opened. Terminating method")
            return False

    def line_count(self):
        lines = self.read_all()
        line_amount = len(lines)
        return line_amount   

    def get_filename(self):
        return self.__filename

    def set_filename(self, new_filename):
        self.__filename = new_filename 

class DeckFileReader(FileReader):

    def __init__(self, filename):
        #each method in the parent class should work for this child class using super 
        super().__init__(
            filename
        )
        print("instance of DeckFileReader class created!")
        #added for random decks method
        # self.start = 1
        # self.stop <= self.line_count

    def __str__(self):
        return f"{self.__class__.__name__}('{self.get_filename}')"

    def all_decks(self):
        # file = open('Decks.txt','r')
        # content = file.readlines()
        content = self.read_all() #decided to call parent method instead
        file_dict = {}
        key = 0
        #for each line in the file, (after the first),
        for line in content[1:]:
            #strip and split, so there are no /n values and the lines are seperated by comma
            amount = line.strip().split(",")
            #the key will be the line number, which will go up after every line iteration
            key += 1
            #the position of the A, B, C, and D amounts, specified here
            WinLoseA = amount[0:2]
            WinLoseB = amount[2:4]
            WinLoseC = amount[4:6]
            WinLoseD= amount[6:8]
            #creating the nested dictionary, line num as main key, then A, B, etc as nested keys
            file_dict[key] = {"A":WinLoseA, "B":WinLoseB, "C":WinLoseC, "D":WinLoseD}

        # file.close() #close file or flush to close the file stream :)
        return file_dict #return your new nested dictionary!

    def get_decks_at(self, line_nums_list):
        #calling all decks to access dict
        all_decks = self.all_decks()
        #creating a new dictionary for this method
        selected_decks = {}
        key = 0
        #for each number specified in line_nums_list
        for line_num in line_nums_list:
        
            key += 1
            #the key will go up for each line iteration, the values are gotten from each line in the dict
            selected_decks[key] = all_decks.get(line_num)

        return selected_decks


    def get_range(self, ran):
        #if ran is not a list and doesn't have 2 values, error
        if not isinstance(ran, list) and len != 2:
            print("Error: Please enter a list with two values.")
            return
        
        #start and stop values in ran
        start = int(ran[0])
        stop = int(ran[1])

        #if start greater than stop and both less than 0, error 
        if start > stop or start < 0 or stop < 0:
            print("Error: Please enter the lower value first, and make sure it is greater than 0")
            return

        #call methiod to use dict
        all_decks = self.all_decks()
        
        #if stop no is greater than the amount of lines in all_decks, error
        if stop >= len(all_decks):
            print("Error: There are not that many decks!")
            return
        #make new dictionary
        selected_range = {}
        key = 0
        #for numbers specified in ran, added to new dict with key num 
        for num in range(start, stop + 1):
            key += 1
            selected_range[key] = all_decks.get(num)

        return selected_range


    def exclude_decks(self, line_nums_list):
        all_decks = self.all_decks()

        selected_decks = {}
        key = 0

        for line_num, deck in all_decks.items():
             if line_num not in line_nums_list:
                 key += 1
                 selected_decks[key] = deck
                 
        return selected_decks
    
    def exclude_range(self, deck_range):
        #check deck_range is list with 2 integers
        if not isinstance(deck_range, list) or len(deck_range) != 2 or not all(isinstance(num, int) for num in deck_range):
            print("Error: Please enter list with two integers")
            return

        #start and stop
        start, stop = deck_range

        all_decks = self.all_decks()

        #check if numbers in list are in file
        if start not in all_decks or stop not in all_decks:
            print("Error: numbers not in decks dictionary")
            return

        selected_decks = {}
        key = 0

        #exclude decks in range
        selected_decks = {line_num: deck for line_num, deck in all_decks.items() if not (start <= line_num <= stop)}
        
        print("Original decks:", all_decks)
        print(f"Excluding decks in range {start} to {stop}")
        print("Selected decks:", selected_decks)
        return selected_decks
    
    #FEATURE 1
    def random_decks(self):
        all_decks = self.all_decks()

        # Get a list of line numbers
        line_numbers = list(all_decks.keys())

        # Shuffle the line numbers to randomize the order
        random.shuffle(line_numbers)

        # Create a new dictionary with randomized decks
        randomized_deck = {num: all_decks[num] for num in line_numbers}

        return randomized_deck
    



# file_1 = DeckFileReader("Decks.txt")
# print(file_1.all_decks())