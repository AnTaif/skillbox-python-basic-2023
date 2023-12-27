class Cell:
    def __init__(self, number):
        self.number = number
        self.is_taken = False
        self.symbol = None

class Board:
    def __init__(self):
        self.cells = [Cell(i + 1) for i in range(9)]

    def change_cell_state(self, cell_number, symbol):
        cell = self.cells[cell_number - 1]
        if not cell.is_taken:
            cell.is_taken = True
            cell.symbol = symbol
            return True
        else:
            return False

    def check_game_end(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]

        for combo in winning_combinations:
            symbols = [self.cells[i].symbol for i in combo]
            if all(symbol == 'X' for symbol in symbols) or all(symbol == 'O' for symbol in symbols):
                return True

        return False


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0

    def make_move(self):
        try:
            move = int(input(f"{self.name}, enter the number of the cell you want to mark (1-9): "))
            if 1 <= move <= 9:
                return move
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
                return self.make_move()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return self.make_move()


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player_index = 0

    def play_one_turn(self):
        player = self.players[self.current_player_index]
        move = player.make_move()
        if self.board.change_cell_state(move, 'X' if player.name == "Player 1" else 'O'):
            if self.board.check_game_end():
                print(f"{player.name} wins!")
                player.wins += 1
                return True
            self.current_player_index = (self.current_player_index + 1) % 2
            return False
        else:
            print("Cell is already taken. Try again.")
            return self.play_one_turn()

    def play_one_game(self):
        self.board = Board()
        while not self.play_one_turn():
            pass

    def play_games(self):
        while True:
            self.play_one_game()
            print("Current score:")
            for player in self.players:
                print(f"{player.name}: {player.wins} wins")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break

player1 = Player("Player 1")
player2 = Player("Player 2")
game = Game(player1, player2)
game.play_games()
