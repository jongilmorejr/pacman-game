# Pacman-Style Game

A Python game inspired by Pacman, built with Pygame. Control a yellow circle character to collect gems and power-ups while avoiding enemies!

## Features

- **Player Character**: Yellow circle that can navigate the map
- **Gems**: Green collectibles worth 100 points each
- **Power-ups**: Star-shaped collectibles that give temporary invincibility (10 seconds)
- **Enemies**: 4 colored enemies that chase the player
- **Sound Effects**: 
  - Pleasant chime sound when collecting gems
  - Rising sweep sound when activating power-ups
  - Generated dynamically using Pygame and NumPy
- **Game Mechanics**:
  - Enemies are slightly faster than the player normally
  - During power-up, player becomes faster than enemies
  - Enemies change color (blue) when player has power-up
  - Player can destroy enemies during power-up (200 points each)
  - Game ends if enemies touch player without power-up
  - 2-minute time limit
  - Game ends when all collectibles are collected

## Controls

- **Arrow Keys** or **WASD**: Move the player
- **R**: Restart game (when game over)

## Installation

1. Make sure you have Python installed (3.7 or higher)
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## How to Run

```
python main.py
```

## Game Rules

1. **Objective**: Collect all gems and power-ups before time runs out
2. **Scoring**:
   - Gems: 100 points each
   - Destroying enemies during power-up: 200 points each
3. **Power-up Effects**:
   - Lasts 10 seconds
   - Player moves faster
   - Enemies turn blue and move slower
   - Player can destroy enemies by touching them
4. **Game Over Conditions**:
   - Time limit reached (2 minutes)
   - All collectibles collected
   - Player touched by enemy without power-up

## File Structure

- `main.py`: Entry point and main game loop
- `game.py`: Main game class that coordinates all components
- `player.py`: Player character class
- `enemy.py`: Enemy AI and behavior
- `collectible.py`: Gem and power-up classes
- `game_map.py`: Map layout and collision detection
- `sound_manager.py`: Sound effects generation and management
- `requirements.txt`: Python dependencies

## Tips

- Use power-ups strategically to clear enemies and gain points
- Learn the enemy movement patterns
- Plan your route to collect items efficiently
- Remember that enemies move faster than you normally, so use walls for protection

Enjoy the game!
