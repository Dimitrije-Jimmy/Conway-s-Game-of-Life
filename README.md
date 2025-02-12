# Conway's Game of Life

This project is an implementation of Conway's Game of Life with an interactive GUI for cellular automata simulation. The GUI is built using the Tkinter library and includes user interaction and visualization features. Additionally, I learned about web scraping using Beautiful Soup to fetch preset examples from the website playgameoflife.com and integrate them into the game.

## Features

- Interactive GUI for simulating Conway's Game of Life
- User interaction for starting, stopping, and resetting the simulation
- Visualization features for observing the evolution of cellular automata
- Web scraping functionality to fetch and use preset examples from the playgameoflife.com lexicon

## Getting Started

### Prerequisites

- Python 3.9.x
- Tkinter library (usually comes with Python)
- Beautiful Soup 4
- Requests library

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Dimitrije-Jimmy/Conway-s-Game-of-Life.git
   cd game_of_life
2. Install the required libraries:
   ```bash
   pip install beautifulsoup4 requests
3. Run the game:
   ```bash
   python game_of_life_final.py

## Web Scraping with Beautiful Soup

In this project, I also explored web scraping to fetch preset examples from the website [playgameoflife.com](https://playgameoflife.com/). The `game_of_life10.py` script includes the code for scraping the website and saving the preset examples. Unfortunately it does not work exactly as I wanted it and requires revision.

## Future Updates

Might revisit project and rebuild it in C++, Python makes for slow calculations and low framerates.

## License
The contents of the repository are licensed under a [MIT License][MIT].

[![MIT License][MIT-shield]][MIT]

[MIT]: https://opensource.org/license/mit
[MIT-shield]: https://img.shields.io/badge/license-MIT-blue.svg

## Acknowledgements
* John Conway for creating the Game of Life
* [playgameoflife.com](https://playgameoflife.com/)
