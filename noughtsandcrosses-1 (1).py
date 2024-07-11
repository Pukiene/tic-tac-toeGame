import random
import os.path
import json
random.seed()


def draw_board(board):
    # develop code to draw the board
    for row in board:
        print('|'.join(row))
        print('-' * 5)
    #print(board)

def welcome(board):
    # prints the welcome message
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    # display the board by calling draw_board(board)
    draw_board(board)

def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    board = [ [' ',' ',' '],\
              [' ',' ',' '],\
              [' ',' ',' ']]
    return board
    
def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    row = None
    col = None

    print('\t\t\t\t\t 1 2 3')
    print('\t\t\t\t\t 4 5 6')
    move = input('Choose your square: 7 8 9:')
    match move:
        case '1':
            row = 0
            col = 0
            #return row, col
        case '2':
            row = 0
            col = 1
            #return row, col
        case '3':
            row = 0
            col = 2
            #return row, col            
        case '4':
            row = 1
            col = 0
           # return row, col            
        case '5':
            row = 1
            col = 1
            #return row, col
        case '6':
            row = 1
            col = 2
            #return row, col
        case '7':
            row = 2
            col = 0
            #return row, col
        case '8':
            row = 2
            col = 1
            #return row, col
        case '9':
            row = 2
            col = 2  
            #return row, col
        case _:
            row = 0
            col = 0 
    if board[row][col] == ' ':
        move = 'X'  # Replace selected number with 'x'
        board[row][col] = move
        draw_board(board)
    elif board[row][col] != ' ':
        print('Square not empty.')
        return get_player_move(board)

    return row, col
 
    # Update the board and return the move
    #return row, col
def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    def predict_win_move(board, mark1):
    # Check rows
        for i in range(3):
            if board[i].count(mark1) == 2 and board[i].count(' ') == 1:
                return i, board[i].index(' ')  # Return the row and column index

        # Check columns
        for i in range(3):
            col = [board[j][i] for j in range(3)]
            if col.count(mark1) == 2 and col.count(' ') == 1:
                return col.index(' '), i  # Return the row and column index

        # Check diagonals
        d1 = [board[i][i] for i in range(3)]
        d2 = [board[i][2 - i] for i in range(3)]
        if d1.count(mark1) == 2 and d1.count(' ') == 1:
            index = d1.index(' ')
            return index, index  # Return the row and column index for diagonal1
        elif d2.count(mark1) == 2 and d2.count(' ') == 1:
            index = d2.index(' ')
            return index, 2 - index  # Return the row and column index for diagonal2

        return None  # Return None if no winning move is found

    def potential_winning_move(board, mark):
    # Check rows
        for i in range(3):
            if board[i].count(mark) == 1 and board[i].count(' ') == 2:
                col_index = board[i].index(' ')
                return i, col_index  # Return the row and column index of potential winning move

        # Check columns
        for i in range(3):
            col = [board[j][i] for j in range(3)]
            if col.count(mark) == 1 and col.count(' ') == 2:
                row_index = col.index(' ')
                return row_index, i  # Return the row and column index of potential winning move

        # Check diagonals
        d1 = [board[i][i] for i in range(3)]
        d2 = [board[i][2 - i] for i in range(3)]
        if d1.count(mark) == 1 and d1.count(' ') == 2:
            index = d1.index(' ')
            return index, index  # Return the row and column index of potential winning move for diagonal1
        elif d2.count(mark) == 1 and d2.count(' ') == 2:
            index = d2.index(' ')
            return index, 2 - index  # Return the row and column index of potential winning move for diagonal2

        return None  # Return None if no potential winning move is found

      


    winning_move = predict_win_move(board, 'O')
    if winning_move == None:
        winning_move = predict_win_move(board, 'X')
    if winning_move == None:
        winning_move = potential_winning_move(board, 'O')
    if winning_move == None:
        winning_move = potential_winning_move(board, 'X')
    if winning_move:
        row, col = winning_move
        if board[row][col] == ' ':
                move = 'O'  # Replace selected number with 'O'
                board[row][col] = move
                draw_board(board)
                return row, col
    
    #winning_move = potential_winning_move(board, 'O')    
    #if winning_move:
     #   row, col = winning_move
      #  if board[row][col] == ' ':
      #          move = 'O'  # Replace selected number with 'x'
       #         board[row][col] = move
       #         draw_board(board)
        #        return row, col
    else:
     # Generate a random computer move
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)

            
            if board[row][col] == ' ':
                move = 'O'  # Replace selected number with 'x'
                board[row][col] = move
                draw_board(board)
                return row, col


def check_for_win(board, mark):

    # Check if the specified mark has won
    for row in range(3):
        if all(board[row][col] == mark for col in range(3)):
            return True

    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == mark for i in range(3)):
        return True

    if all(board[i][2 - i] == mark for i in range(3)):
        return True

    return False  # Game is not over yet


def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    # Check if all cells are occupied
    for row in board:
        if ' ' in row:
            return False  # Found an empty space
    return True 


        
def play_game(board):
    score = 0
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    board = initialise_board(board)
    
    # then draw the board
    draw_board(board)

    # then in a loop, get the player move, update and draw the board
   
    game = True
    while game == True:
        row, col = get_player_move(board)
        mark = board[row][col]
        # check if the player has won by calling check_for_win(board, mark),
        if check_for_win(board, mark) == True:
            print('Player won')
            game = False
            return 1
                # Declare the player as the winner and save the score

        # if so, return 1 for the score
        # if not check for a draw by calling check_for_draw(board)

        # if is False   
        if  check_for_draw(board) == True:
            # Declare the game as a draw
            print('gmae is a draw')
            game = False
            return 0
                    

        # if drawn, return 0 for the score
        # if not, then call choose_computer_move(board)
        row, col = choose_computer_move(board)
        mark = board[row][col]
        # Declare the computer as the winner and assign a negative score

        # to choose a move for the computer
        # update and draw the board
        # check if the computer has won by calling check_for_win(board, mark),
        if check_for_win(board, mark) == True:
            print('Player won')
            game = False
            return -1
        # if so, return -1 for the score
        # if not check for a draw by calling check_for_draw(board)
        if  check_for_draw(board) == True:
            # Declare the game as a draw
            print('gmae is a draw')
            game = False
            return 0
        # if drawn, return 0 for the score
        #repeat the loop
    

def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program

    print('When prompted, enter the number corresponding to the square you want.\nEnter one of the following options:')
    print('\t1 - Play the game')
    print('\t2 - Save your score in the leaderboard')
    print('\t3 - Load and display the leaderboard')
    print('\tq - End the program')
    
    choice = input('1, 2, 3 or q?')
    if choice == 'q':
        return choice
    if choice == '1':
        return choice
    if choice == '2':
        return choice
    if choice == '3':
        return choice
    if choice == '5':
        return 'q'
    

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    # Initialize an empty dictionary to store the leaderboard scores
 # Initialize an empty dictionary to store the leaderboard scores

    # Open the leaderboard file in read mode

    leaders = {}

    # Open the leaderboard file in read mode
    with open('leaderboard.txt', 'r') as file:
        # Read the content of the file
        file_content = file.read()

        # Convert the JSON string to a Python dictionary
        leaders = json.loads(file_content)

    # Return the dictionary of leaderboard scores
    return leaders

# Call the function to load leaderboard scores
loaded_scores = load_scores()
print(loaded_scores)  # Print the loaded scores
    
def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    player_name = input("What is your name? ")

    # Load existing scores
    leaders = load_scores()
    
    # Add or update the player's score
    leaders[player_name] = score

    # Write updated scores back to the file
    with open('leaderboard.txt', 'w') as file:
        json.dump(leaders, file)
    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    print("The current leaderboard is:")
    print("    Name    Score")
    for player, score in leaders.items():
        print(f"    {player:<10} {score}")

def load_scores_from_file(filename):
    # Function to load leaderboard scores from a text file
    # Takes the filename as input and returns the scores in a dictionary
    
    with open(filename, 'r') as file:
        leaderboard_data = file.read()
        leaderboard_dict = eval(leaderboard_data)
        return leaderboard_dict

# Load leaderboard scores from the text file
file_scores = load_scores_from_file('leaderboard.txt')

# Display the leaderboard scores using the function
display_leaderboard(file_scores)
    

