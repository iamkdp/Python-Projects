# XOXO Game (Tic-Tac-Toe) implementation

# Function to print the game board
def print_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n-------------")

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

# Function to play the game
def play_game():
    # Initialize the game board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False
    
    # Main game loop
    while not game_over:
        # Print the board
        print_board(board)
        
        # Get the current player's move
        print("Player", current_player + "'s turn")
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        
        # Update the board with the move
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move! Try again.")
            continue
        
        # Check if the current player has won
        if check_win(board, current_player):
            print("Player", current_player, "wins!")
            game_over = True
        elif all(cell != " " for row in board for cell in row):
            # Check if it's a tie (board is full)
            print("It's a tie!")
            game_over = True
        else:
            # Switch to the next player
            current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
