"""
A FILE EXAMPLE TO TEST IT USE Pylint
To install Pylint use: pip install pylint
(u probably also need to update it if installed: pip install pylint --upgrade)
To execute Pylint use: pylint file_to_test.py
"""

class Player():

    """
    Basic func that calls when we creating a new player
    [also informs us about new player registered with his name]
    """
    def __init__(self, player_name, player_lvl, player_job):
        self.player_name = player_name
        self.player_job = player_job
        self.player_lvl = player_lvl
        print(f'New player registered: {self.player_name}!')

    """
    Basic func that calls when we want to get string param of Player
    """
    def __str__(self):
        return f'Player: {self.player_name} | Job: {self.player_job} | LVL: {self.player_lvl}'

    """
    Basic func that calls when we want to get length (int) param of Player
    returns Player lvl instead of length of name
    """
    def __len__(self):
        return self.player_lvl

if __name__ == '__main__':
    spylestia = Player('Spylestia', 'Farmer', 3)
