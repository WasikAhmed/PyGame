# Space Battle

This repository contains a 2D space battle game built using PyGame. The game features two spaceships controlled by players, who can move around the screen, shoot bullets, and try to hit each other. The game includes health tracking, bullet collision detection, and a winner announcement.

## Features

- **Spaceship Movement**: Players can move their spaceships in four directions using specific keys.
- **Bullet Shooting**: Players can shoot bullets, and the game handles bullet movement and collision detection.
- **Health Tracking**: Each spaceship has health points that decrease when hit by a bullet.
- **Winner Announcement**: The game announces the winner when one spaceship's health reaches zero.

## Technologies Used

- **Python**: The primary programming language used for the game logic.
- **PyGame**: A set of Python modules designed for writing video games, used for handling graphics, sound, and game events.
- **Assets**: Images and sounds used in the game are stored in the `Assets` directory.

## Project Structure

- `main.py`: Contains the main game logic, including functions for handling movement, bullets, drawing the game window, and determining the winner.
- `Assets`: Directory containing image and sound files used in the game.
- `requirements.txt`: Lists the dependencies required to run the project, including specific versions of PyGame, setuptools, and wheel.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: Provides an overview of the project and its purpose.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/WasikAhmed/space-battle.git
    cd space-battle
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## How to Run

1. Ensure you have the required dependencies installed.
2. Run the game:
    ```sh
    python main.py
    ```

## Controls

- **Yellow Spaceship**:
  - Move Left: `A`
  - Move Right: `D`
  - Move Up: `W`
  - Move Down: `S`
  - Shoot: `Left Shift`

- **Red Spaceship**:
  - Move Left: `J`
  - Move Right: `L`
  - Move Up: `I`
  - Move Down: `K`
  - Shoot: `Right Shift`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project is inspired by various PyGame tutorials and resources available online.

Enjoy the game and happy coding!