# Paper-Rock-Scissors Game

## Description

Paper-Rock-Scissors is a game for two players. Each player simultaneously opens his/her hand to
display a symbol:

- Fist equals rock
- Open hand equals paper
- Showing the index and middle finger equals scissors.

The winner is determined by the following schema:

- paper beats (wraps) rock
- rock beats (blunts) scissors
- scissors beats (cuts) paper.

Application plays Paper-Scissors-Rock between the computer and a real player.
You are able to play the game ```n``` times before the program exits.

## Setup

### Prerequisites

Before running the project, ensure that you have the following software installed on your system:

- Python (version 3.7 or higher)
- Pip (Python package installer)
- Make (build automation tool)

### Installing make

#### On macOS

If you have Homebrew installed, you can easily install make by running:

```bash
brew install make
````

#### Running application:

To use the app, run the following command(s):

1. Create a virtual environment and install all project dependencies:
    ```bash
    make
    ```

2. Run the application:
   ```bash
   make run
   ```

## Tests

Execute the following command to run the app tests:
   ```bash
   make test
   ```

## Contributing

This project is an open source project, and contributions are gladly welcomed!
To submit your changes please check pull request rules and open a pull request.
