from pathlib import Path
from textwrap import fill
from importlib import import_module
import sys

def main():
    print("Welcome to the retro arcade!")
    games = [p.name for p in Path('games').iterdir()]
    while True:
        print('=' * 80)
        game = get_choice(games, "Which game would you like to play?")
        description = (Path("games") / game / "description.txt").read_text()
        print()
        print(game)
        print('-' * 80)
        print(fill(description, width=80))
        if get_choice(["Play", "Go back"]) == "Play":
            play_game(game)
        
def get_choice(choices, prompt=None):
    if prompt:
        print(prompt)
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
    while True:
        selection = input("> ")
        try:
            return choices[int(selection) - 1]
        except (ValueError, IndexError):
            print("That's not a valid choice.")

def play_game(game):
    try:
        sys.path.append("games/" + game)
        module = import_module("games." + game + ".play")
        module.main()
        sys.path.pop()
    except KeyboardInterrupt:
        print("You ended the game.")
    except:
        print("Uh oh, the game crashed!")

if __name__ == '__main__':
    main()
