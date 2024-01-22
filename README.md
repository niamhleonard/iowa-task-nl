The project includes the implementation of the DeckFileReader and TrialParticipant classes to create a functional Iowa Gambling Task.

Base Requirements
The project began by addressing errors in the code from previous assignments and incorporating feedback on the 
DeckFileReader and TrialParticipant classes. The participant Python file was modified to meet assignment requirements, 
including changes from class to instance variables. Various methods, such as string representation and getter/setter methods,
were improved for enhanced functionality.

The TrialParticipant class interacts heavily with the DeckFileReader class,
allowing access to deck information during initialization. The DeckFileReader class ensures correct dictionary 
outputs for different methods, utilizing a 'key' variable for proper formatting.

Additional Features
Feature 1: Changing the Decks
A new set of decks is offered after completing the task with the initial set. 
Users can choose to continue with new decks or terminate the task. The 
implementation avoids manual creation of new text files by shuffling line numbers from the
existing file to create varied decks.

Inheritance and method overriding concepts are demonstrated in the DeckFileReader class, 
where properties and behaviors are inherited from the FileReader superclass, allowing customization 
for the new deck requirements.

Feature 2: Changing the Loan Amount
To incentivize continued participation, the loan amount is 
increased by €1000 each time the user chooses to continue.
This variable is flexible and reusable for different intentions, 
iterations, and projects.

Areas for Improvement
While the code handles basic errors well, there is room for improvement through additional 
user testing and unit testing, particularly for file reading and deck generation. The author 
expresses a desire to deepen their understanding of method overriding and inheritance for future 
enhancements. Despite contentment with the code's simplicity, there is an aspiration to
create something applicable in real-world scenarios.
