"""
The main file used to run the main functionalities of "Gemini AI Games".
Author: GlobalCreativeApkDev
"""

# Importing necessary libraries


import os
import sys


# Creating static functions


def install_game(game_name):
    # type: (str) -> bool
    games_file = open("games.txt", 'r')
    games: list = [game.strip() for game in games_file]
    if game_name not in games:
        return False

    os.system("pip3 install " + str(game_name))
    os.system("pip3 install " + str(game_name) + " --target installed/" + str(game_name))
    return True


def uninstall_game(game_name):
    # type: (str) -> bool
    installed_games = [game for game in os.listdir("installed") if os.path.isdir(os.path.join("installed", game))]
    if game_name not in installed_games:
        return False

    os.system("pip3 uninstall " + str(game_name))
    if sys.platform.startswith('win'):
        os.system("rmdir -r installed/" + str(game_name))  # For Windows System
    else:
        os.system("rm -r installed/" + str(game_name))  # For Linux System
    return True


def play_installed_game(game_name):
    # type: (str) -> bool
    installed_games = [game for game in os.listdir("installed") if os.path.isdir(os.path.join("installed", game))]
    if game_name not in installed_games:
        return False

    clear()
    os.system("python3 installed/" + str(game_name) + "/" + str(game_name) + "/" + str(game_name) + ".py")
    return True


def play_pre_installed_game(game_name):
    # type: (str) -> bool
    pre_installed_games = [game for game in os.listdir("pre-installed") if
                           os.path.isdir(os.path.join("pre-installed", game))]
    if game_name not in pre_installed_games:
        return False

    clear()
    os.system("python3 pre-installed/" + str(game_name) + "/main.py")
    return True


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


# Creating main function used to run the application.


def main() -> int:
    """
    The main function used to run the application.
    :return: an integer
    """

    print("Welcome to 'Gemini AI Games' by 'GlobalCreativeApkDev'.")
    print("This application allows you to play pre-installed games or download and install online games and play them!")

    while True:
        print("Enter \"PLAY PRE-INSTALLED GAME\" to play a pre-installed game.")
        print("Enter \"INSTALL GAME\" to install a game.")
        print("Enter \"PLAY INSTALLED GAME\" to play an installed game.")
        print("Enter \"UNINSTALL GAME\" to uninstall a game.")
        allowed: list = ["PLAY PRE-INSTALLED GAME", "INSTALL GAME", "PLAY INSTALLED GAME", "UNINSTALL GAME"]
        action: str = input("What do you want to do? ")
        while action not in allowed:
            clear()
            print("Enter \"PLAY PRE-INSTALLED GAME\" to play a pre-installed game.")
            print("Enter \"INSTALL GAME\" to install a game.")
            print("Enter \"PLAY INSTALLED GAME\" to play an installed game.")
            print("Enter \"UNINSTALL GAME\" to uninstall a game.")
            action = input("Sorry, invalid input! What do you want to do? ")

        if action == "PLAY PRE-INSTALLED GAME":
            clear()
            pre_installed_games = [game for game in os.listdir("pre-installed") if
                                   os.path.isdir(os.path.join("pre-installed", game))]
            print("Below is a list of pre-installed games:\n")
            for i in range(len(pre_installed_games)):
                print(str(i + 1) + ". " + str(pre_installed_games[i]))

            game_index: int = int(input("Please enter the index of the game you want to "
                                        "play (1 - " + str(len(pre_installed_games)) + "): "))
            while game_index < 1 or game_index > len(pre_installed_games):
                game_index = int(input("Sorry, invalid input! Please enter the index of the game you want to "
                                       "play (1 - " + str(len(pre_installed_games)) + "): "))

            game_to_uninstall: str = pre_installed_games[game_index - 1]
            play_pre_installed_game(game_to_uninstall)
        elif action == "INSTALL GAME":
            clear()
            games_file = open("games.txt", 'r')
            games: list = [game.strip() for game in games_file]
            print("Below is a list of games you can install:\n")
            for i in range(len(games)):
                print(str(i + 1) + ". " + str(games[i]))

            game_index: int = int(input("Please enter the index of the game you want to "
                                        "install (1 - " + str(len(games)) + "): "))
            while game_index < 1 or game_index > len(games):
                game_index = int(input("Sorry, invalid input! Please enter the index of the game you want to "
                                       "install (1 - " + str(len(games)) + "): "))

            game_to_install: str = games[game_index - 1]
            install_game(game_to_install)
        elif action == "PLAY INSTALLED GAME":
            clear()
            installed_games = [game for game in os.listdir("installed") if os.path.isdir(os.path.join("installed", game))]
            print("Below is a list of installed games:\n")
            for i in range(len(installed_games)):
                print(str(i + 1) + ". " + str(installed_games[i]))

            game_index: int = int(input("Please enter the index of the game you want to "
                                        "play (1 - " + str(len(installed_games)) + "): "))
            while game_index < 1 or game_index > len(installed_games):
                game_index = int(input("Sorry, invalid input! Please enter the index of the game you want to "
                                       "play (1 - " + str(len(installed_games)) + "): "))

            game_to_uninstall: str = installed_games[game_index - 1]
            play_installed_game(game_to_uninstall)
        elif action == "UNINSTALL GAME":
            clear()
            installed_games = [game for game in os.listdir("installed") if os.path.isdir(os.path.join("installed", game))]
            print("Below is a list of installed games:\n")
            for i in range(len(installed_games)):
                print(str(i + 1) + ". " + str(installed_games[i]))

            game_index: int = int(input("Please enter the index of the game you want to "
                                        "uninstall (1 - " + str(len(installed_games)) + "): "))
            while game_index < 1 or game_index > len(installed_games):
                game_index = int(input("Sorry, invalid input! Please enter the index of the game you want to "
                                       "uninstall (1 - " + str(len(installed_games)) + "): "))

            game_to_uninstall: str = installed_games[game_index - 1]
            uninstall_game(game_to_uninstall)

        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_using: str = input("Do you want to continue using \"Gemini AI Games\"? ")
        if continue_using != "Y":
            return 0


if __name__ == '__main__':
    main()
