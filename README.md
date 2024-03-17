# gemini-ai-games

An application containing a compilation of games with Google Gemini AI integrated into them.

# Pre-Installed Games

| Name                   | Author                                                          | Latest Version |
|------------------------|-----------------------------------------------------------------|----------------|
| Gemini Number Guessing | [GlobalCreativeApkDev](https://github.com/GlobalCreativeApkDev) | 1              |

# Games Requiring Installation

| Name           | Author                                                          | Latest Version |
|----------------|-----------------------------------------------------------------|----------------|
| Gemini Pro RPG | [GlobalCreativeApkDev](https://github.com/GlobalCreativeApkDev) | 1.2            |

# How to Add a Game?

1. Enter the name of your game on a new line in the file games.txt.
2. Ensure that the name of the game you entered is already available as a PyPi project, with the format containing 
at least like below, where [your_package_name] is the name of your package and [entry_point_name] is the name
of the entry point of your package.

[your_package_name]
├── [your_package_name]
│   └── [entry_point_name].py
└── setup.py

3. Create a fork or a new branch and then merge it to **master** branch of this repository.
4. Add the game to either **Pre-Installed Games** or **Games Requiring Installation** section of this document, 
depending on the category of your game.

# Source Code

The source code of the application **Gemini AI Games** is found in

# Installation

```
pip install gemini-ai-games
```

# How to Use the Application?

Pre-requisites:

1. [Python](https://www.python.org/downloads/) installed in your device.
2. .env file in the same directory as <GEMINI_AI_GAMES_DIRECTORY> and has the value of GEMINI_API_KEY.

First, open a Terminal or Command Prompt window and run the following commands.

```
cd <GEMINI_AI_GAMES_DIRECTORY>
python3 main.py
```

**Note:** Replace <GEMINI_AI_GAMES_DIRECTORY> with the path to the directory of the application **Gemini AI Games**.

Then, the application will start with something looking like in the screenshot below.
