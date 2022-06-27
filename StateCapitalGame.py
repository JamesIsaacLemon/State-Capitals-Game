import random

states = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}
capitals = {v: k for k, v in states.items()}

chimplist = ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
             'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
             'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
             'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina',
             'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
             'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
             'Wisconsin', 'Wyoming')
capital_list = ('Montgomery', 'Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver', 'Hartford', 'Dover',
                'Tallahassee', 'Atlanta', 'Honolulu', 'Boise', 'Springfield', 'Indianapolis', 'Des Moines', 'Topeka',
                'Frankfort', 'Baton Rouge', 'Augusta', 'Annapolis', 'Boston', 'Lansing', 'Saint Paul', 'Jackson',
                'Jefferson City', 'Helena', 'Lincoln', 'Carson City', 'Concord', 'Trenton', 'Santa Fe', 'Albany',
                'Raleigh', "Bismarck", 'Columbus', 'Oklahoma City', 'Salem', 'Harrisburg', 'Providence', 'Columbia',
                'Pierre', 'Nashville', 'Austin', 'Salt Lake City', 'Montpelier', 'Richmond', 'Olympia', 'Charleston',
                'Madison', 'Cheyenne')

still_playing = True
score = 0
freebie_count = 0


def menu():
    game_input = int(input("Type 1 for the State Game, or 2 for the Capital Game: "))
    if game_input == 1:
        play_capital_game()
    else:
        play_state_game()


def get_score():
    global score
    return "Score: " + str(score) + "! "


def score_values():
    if score == 10:
        print("You're on fire! " + get_score())
    elif score == 20:
        print("You're crazy! " + get_score())
    elif 22 < score <= 24:
        print("Wow nearly halfway now. " + get_score())
    elif score == 25:
        print("Halfway! " + get_score())
    elif score == 26:
        print("Over the hump now! " + get_score())
    elif score == 30:
        print("This dude knows their fuckin U.S. geography. " + get_score())
    elif score == 40:
        print("You're fuckin nuts you're almost there! " + get_score())
    elif 45 <= score <= 49:
        print("You're so close! " + get_score())
    elif score == 50:
        print("God damn you've done it. Congratulations." + get_score())
        quit()
    else:
        print("Correct! " + get_score())


def play_state_game():
    freebie_limit = 3
    global freebie_count
    global still_playing
    global score
    global chimplist

    for state in chimplist:
        chimplist = list(states.keys())
        balls = len(chimplist)
        state = random.choice(chimplist)
        answer = states.get(state).lower()
        chimplist.remove(state)
        states.pop(state)
        if freebie_count < freebie_limit:
            guess = input("What is the capital of " + state + "? ").lower()
            if guess == answer:
                score += 1
                score_values()
            elif guess == "X" or guess == "x":
                print("Quitting game. Thanks for playing!")
                quit()
            elif guess == "R" or guess == "r":
                print(str(balls) + " states remaining.")
            elif guess == "Q" or guess == "q":
                print("Going back to menu.")
                menu()
            else:
                freebie_count += 1
                print("That is incorrect. You have used " + str(freebie_count) + " out of 3 freebies.")
                still_playing = False
        else:
            print("Sorry you are out of freebies, please play again! ")
            still_playing = False
            quit()


def play_capital_game():
    freebie_limit = 3
    global freebie_count
    global still_playing
    global score
    global capital_list
    global capitals
    global chimplist

    for capital in capital_list:
        chimplist = list(states.keys())
        capital_list = list(capitals.keys())
        balls = len(capital_list)
        capital = random.choice(capital_list)
        answer = capitals.get(capital)
        answer = answer.lower()
        capital_list.remove(capital)
        capitals.pop(capital)
        if freebie_count < freebie_limit:
            guess = input("Which state is " + capital + " the capital of? ").lower()
            if guess == answer:
                score += 1
                score_values()
            elif guess == "R" or guess == "r":
                print(str(balls) + " states remaining.")
            elif guess == "Q" or guess == "q":
                print("Going back to menu.")
                menu()
            elif guess == "X" or guess == "x":
                print("Quitting game. Thanks for playing!")
                quit()
            else:
                freebie_count += 1
                print("That is incorrect. You have used " + str(freebie_count) + " out of 3 freebies.")
        else:
            print("Sorry you are out of freebies, please play again! ")
            quit()


print("Hello! Welcome to the State/Capital game! (title pending)")
print("Once the game begins you may:")
print("Type R to see how many states remain.")
print("Type X to quit the game.")
print("Type Q to return to this menu.")

while still_playing:
    menu()

if not states:
    print("That's all of them! Your final score was: " + str(score) + "! ")
    quit()
if not capitals:
    print("That's all of them! Your final score was: " + str(score) + "! ")
    quit()
