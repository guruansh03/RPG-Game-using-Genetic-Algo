# Adaptive AI for Turn-Based RPG Combat

## Project Status

**Python**

**License**

### Overview

This project implements an adaptive AI for a turn-based RPG combat simulator. Built with Python, Pygame, and NumPy, the AI uses a genetic algorithm (GA) to dynamically adapt to player actions (e.g., clicking to attack, heal, or defend), creating a challenging and engaging gaming experience. The system features a graphical interface with customizable themes and difficulty levels.

The AI evolves its behavior parameters (attack, heal, special attack probabilities, and heal threshold) to counter player strategies, ensuring varied and strategic combat. This project demonstrates the application of evolutionary algorithms in game AI, with potential extensions to other domains.

### Features

- **Adaptive AI**: Responds to player clicks with dynamic counter-strategies, optimized by a genetic algorithm.
- **Turn-Based Combat**: Control two characters (Hero, Mage) against two enemies (Goblin, Wolf) with actions like Attack, Heal, Defend, and Special.
- **Graphical Interface**: Pygame-based GUI with animations (shake, glow, particles) and themes (Light, Dark, Retro, Cyberpunk, Fantasy).
- **Difficulty Levels**: Easy, Medium, and Hard modes adjust enemy stats and AI aggression.
- **Genetic Algorithm**: Evolves AI behavior every 5 turns, balancing battle duration, player health reduction, and action variety.

### Prerequisites

- **Python**: 3.9
- **Libraries**: Pygame 2.5.2, NumPy 1.24.3
- **Hardware**: 4GB RAM, 2GHz processor, 500MB storage, 1600x960 display
- **OS**: Windows 10/11, Linux, or macOS

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/[your-username]/adaptive-ai-rpg-combat.git
   cd adaptive-ai-rpg-combat
    ```
Install Dependencies:

```bash

pip install pygame==2.5.2 numpy==1.24.3
```
Verify Python Version:

```bash
python --version
```
Ensure Python 3.9 is installed.

Usage
Run the Game:

```bash

python main.py
```
### Gameplay:

**Training Phase:** The AI trains for 2 generations (shown with a progress bar).

**Battle Phase: **Click action buttons (Attack, Special, Heal, Defend) to control Hero and Mage against Goblin and Wolf.

**Customize: **Use dropdowns to select themes (e.g., Cyberpunk) and difficulty levels (Easy, Medium, Hard).

**AI Adaptation:** The AI adjusts its strategy based on your clicks, countering frequent attacks or healing with appropriate actions.

### Controls
Click action buttons to select moves.

Use theme/difficulty dropdowns in the top-right corner.

### Project Structure
```bash

adaptive-ai-rpg-combat/
├── main.py           # Main game script with game logic, AI, and GUI
├── README.md        # Project documentation
├── assets/          # (Optional) Images, fonts, or sounds for GUI
└── docs/            # Project report and user manual (if included)
```
