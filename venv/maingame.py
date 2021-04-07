# Notes from game:
# I tried to use dictionary which was unnecessary. Strings in a list would have made more sense.
# Combining if statements makes the code look much cleaner.
# Board object made sense, player and opponent did not have clearly defined methods.

from launchgame import welcome_player
from random import randint

class Board:
    def __init__(self):
    # create the board
    # create dictionary of all the slots to enter
        self.top_left={'entry': ' '}
        self.top_center = {'entry':' '}
        self.top_right={'entry': ' '}
        self.mid_left={'entry': ' '}
        self.mid_center = {'entry':' '}
        self.mid_right={'entry': ' '}
        self.bottom_left={'entry': ' '}
        self.bottom_center = {'entry':' '}
        self.bottom_right ={'entry': ' '}

    #board_spaces = [top_left,top_center,top_right,
    #               mid_left,mid_center,mid_right,
    #               bottom_left,bottom_center,bottom_right]

    # create a function to print the board
    def print_board(self):
        print("%s|%s|%s" % (self.top_left['entry'], self.top_center['entry'], self.top_right['entry']))
        print("-----")
        print("%s|%s|%s" % (self.mid_left['entry'], self.mid_center['entry'], self.mid_right['entry']))
        print("-----")
        print("%s|%s|%s" % (self.bottom_left['entry'], self.bottom_center['entry'], self.bottom_right['entry']))

    # check if the space has already been selected

    # create a function to update the dictionary based on player selection
    def update_board(self, selection, player_select):
        if player_select== True:
            if selection == "TopL" and self.top_left=={'entry': ' '}:
                self.top_left={'entry': 'X'}
            elif selection == "TopC" and self.top_center =={'entry': ' '}:
                self.top_center={'entry': 'X'}
            elif selection == "TopR" and self.top_right =={'entry': ' '}:
                self.top_right={'entry': 'X'}
            elif selection == "MidL" and self.mid_left =={'entry': ' '}:
                self.mid_left={'entry': 'X'}
            elif selection == "MidC" and self.mid_center =={'entry': ' '}:
                self.mid_center={'entry': 'X'}
            elif selection == "MidR" and self.mid_right =={'entry': ' '}:
                self.mid_right={'entry': 'X'}
            elif selection == "BotL" and self.bottom_left =={'entry': ' '}:
                self.bottom_left={'entry': 'X'}
            elif selection == "BotC" and self.bottom_center =={'entry': ' '}:
                self.bottom_center={'entry': 'X'}
            elif selection == "BotR" and self.bottom_right =={'entry': ' '}:
                self.bottom_right={'entry': 'X'}
            else:
                print('This space is taken. Please select another space.')
                player_selection()
        elif player_select== False:
            if selection == "TopL" and self.top_left=={'entry': ' '}:
                self.top_left={'entry': 'O'}
            elif selection == "TopC" and self.top_center =={'entry': ' '}:
                self.top_center={'entry': 'O'}
            elif selection == "TopR" and self.top_right =={'entry': ' '}:
                self.top_right={'entry': 'O'}
            elif selection == "MidL" and self.mid_left =={'entry': ' '}:
                self.mid_left={'entry': 'O'}
            elif selection == "MidC" and self.mid_center =={'entry': ' '}:
                self.mid_center={'entry': 'O'}
            elif selection == "MidR" and self.mid_right =={'entry': ' '}:
                self.mid_right={'entry': 'O'}
            elif selection == "BotL" and self.bottom_left =={'entry': ' '}:
                self.bottom_left={'entry': 'O'}
            elif selection == "BotC" and self.bottom_center =={'entry': ' '}:
                self.bottom_center={'entry': 'O'}
            elif selection == "BotR" and self.bottom_right =={'entry': ' '}:
                self.bottom_right={'entry': 'O'}
            else:
                opponent_selection()
        else:
            print('There was an error with the selection. Critical failure.')
            exit()

    # check to see if a player has won
    def check_if_win(self, game_running):
        if (self.top_left == {'entry': 'X'} and self.top_center == {'entry': 'X'} and self.top_right == {'entry': 'X'} or
            self.mid_left == {'entry': 'X'} and self.mid_center == {'entry': 'X'} and self.mid_right == {'entry': 'X'} or
            self.bottom_left == {'entry': 'X'} and self.bottom_center == {'entry': 'X'} and self.bottom_right == {'entry': 'X'} or
            self.top_left == {'entry': 'X'} and self.mid_left == {'entry': 'X'} and self.bottom_left == {'entry': 'X'} or
            self.top_center == {'entry': 'X'} and self.mid_center == {'entry': 'X'} and self.bottom_center == {'entry': 'X'} or
            self.top_right == {'entry': 'X'} and self.mid_right == {'entry': 'X'} and self.bottom_right == {'entry': 'X'} or
            self.top_left == {'entry': 'X'} and self.mid_center == {'entry': 'X'} and self.bottom_right == {'entry': 'X'} or
            self.top_right == {'entry': 'X'} and self.mid_center == {'entry': 'X'} and self.bottom_left == {'entry': 'X'}):
            self.print_board()
            print("You won!")
            exit()

        elif (self.top_left == {'entry': 'O'} and self.top_center == {'entry': 'O'} and self.top_right == {'entry': 'O'} or
            self.mid_left == {'entry': 'O'} and self.mid_center == {'entry': 'O'} and self.mid_right == {'entry': 'O'} or
            self.bottom_left == {'entry': 'O'} and self.bottom_center == {'entry': 'O'} and self.bottom_right == {'entry': 'O'} or
            self.top_left == {'entry': 'O'} and self.mid_left == {'entry': 'O'} and self.bottom_left == {'entry': 'O'} or
            self.top_center == {'entry': 'O'} and self.mid_center == {'entry': 'O'} and self.bottom_center == {'entry': 'O'} or
            self.top_right == {'entry': 'O'} and self.mid_right == {'entry': 'O'} and self.bottom_right == {'entry': 'O'} or
            self.top_left == {'entry': 'O'} and self.mid_center == {'entry': 'O'} and self.bottom_right == {'entry': 'O'} or
            self.top_right == {'entry': 'O'} and self.mid_center == {'entry': 'O'} and self.bottom_left == {'entry': 'O'}):
            self.print_board()
            print("You lost!")
            exit()

    # check to see if the board is full
    def tie_check(self, game_running):
        if (self.top_left !=  {'entry': ' '} and
            self.top_center !=  {'entry': ' '} and
            self.top_right !=  {'entry': ' '} and
            self.mid_left != {'entry': ' '} and
            self.mid_center !=  {'entry': ' '} and
            self.mid_right !=  {'entry': ' '} and
            self.bottom_left !=  {'entry': ' '} and
            self.bottom_center !=  {'entry': ' '} and
            self.bottom_right !=  {'entry': ' '}):
            self.print_board()
            print("Looks like you tied...try again!")
            exit()

# create a player class
class Player:
    def __init__(self):
        player_name = input("Please enter your name.")
        while len(player_name) < 1:
            player_name = input("Please enter a valid player name")
        else:
            welcome_player(player_name)

    # create a function for a player to make their selection
def player_selection():
    selection = input("Please select a space: TopL, TopC, TopR, MidL, MidC, MidR, BotL, BotM, BotR")
    player_select = True
    if (selection == 'TopL' or
        selection == 'TopC' or
        selection == 'TopR' or
        selection == 'MidL' or
        selection == 'MidC' or
        selection == 'MidR' or
        selection == 'BotL' or
        selection == 'BotC' or
        selection == 'BotR'):
        game_board.update_board(selection, player_select)
    else:
        print('Please type the space as follows: TopL, TopC, TopR, MidL, MidC, MidR, BotL, BotM, BotR')
        player_selection()


# create an opponent class

class Opponent:
    def __init__(self):
        self.name_select = randint(1,3)
        if self.name_select == 1:
            self.opponent_name = "Ranger"
        elif self.name_select == 2:
            self.opponent_name = "Oaklee"
        elif self.name_select == 3:
            self.opponent_name = "Tito"

        print("Your opponent this round is %s." % self.opponent_name)

# create a function for the opponent to select a space
def opponent_selection():
    player_select = False
    selection_number = randint(1,9)
    if selection_number == 1:
        selection = 'TopL'
    elif selection_number == 2:
        selection = 'TopC'
    elif selection_number == 3:
        selection = 'TopR'
    elif selection_number == 4:
        selection = 'MidL'
    elif selection_number == 5:
        selection = 'MidC'
    elif selection_number == 6:
        selection = 'MidR'
    elif selection_number == 7:
        selection = 'BotL'
    elif selection_number == 8:
        selection = 'BotM'
    elif selection_number == 9:
        selection = 'BotR'
    else:
        print("Not sure how this got here...Critical failure")
        exit()
    game_board.update_board(selection, player_select)

# function for each game turn
def game_turn():
    game_board.print_board()
    player_selection()
    game_board.check_if_win(game_running)
    game_board.tie_check(game_running)
    opponent_selection()
    game_board.check_if_win(game_running)
    game_board.tie_check(game_running)

# initialize the game
game_board = Board()
game_player = Player()
game_opponent = Opponent()

# run the game
game_running = True
while game_running == True:
    game_turn()







