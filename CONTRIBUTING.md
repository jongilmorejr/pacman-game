# Contributing to Pacman-Style Game

Thanks for your interest in contributing to our family Pacman game project! 🎮

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git installed on your computer

### Setting Up Your Development Environment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jongilmorejr/pacman-game.git
   cd pacman-game
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv game_env
   # On Windows:
   game_env\Scripts\activate
   # On macOS/Linux:
   source game_env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Test the game:**
   ```bash
   python main.py
   ```

## Development Workflow

We use a simple Git workflow that's perfect for learning:

### 1. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
# Example: git checkout -b feature/add-high-scores
```

### 2. Make Your Changes
- Edit the code
- Test your changes by running `python main.py`
- Make sure the game still works

### 3. Commit Your Changes
```bash
git add .
git commit -m "Add a clear description of what you changed"
# Example: git commit -m "Add high score tracking and display"
```

### 4. Push Your Branch
```bash
git push origin feature/your-feature-name
```

### 5. Create a Pull Request
- Go to GitHub
- Click "Compare & pull request"
- Describe what you changed and why
- Request review from a family member

## Code Style Guidelines

- Use clear, descriptive variable names
- Add comments to explain complex logic
- Keep functions small and focused
- Test your changes before submitting

## Ideas for Contributions

### Easy (Great for Learning):
- [ ] Add new sound effects
- [ ] Change colors or visual effects
- [ ] Add more gems or power-ups to the map
- [ ] Adjust game speeds or timing

### Medium:
- [ ] Add a high score system
- [ ] Create different difficulty levels
- [ ] Add new types of collectibles
- [ ] Implement a lives system

### Advanced:
- [ ] Add multiple game levels
- [ ] Create different enemy AI behaviors
- [ ] Add multiplayer support
- [ ] Implement save/load game state

## Testing Your Changes

Before submitting a pull request:

1. **Run the game and test your feature:**
   ```bash
   python main.py
   ```

2. **Check for Python syntax errors:**
   ```bash
   python -m py_compile *.py
   ```

3. **Make sure all imports work:**
   ```bash
   python -c "from game import Game; print('All imports successful')"
   ```

## Getting Help

- Ask questions in pull request comments
- Create GitHub issues for bugs or feature requests
- Family Slack/Discord for quick questions

## Pull Request Process

1. Make sure your code works and doesn't break existing functionality
2. Update the README.md if you add new features
3. Write a clear pull request description
4. Be patient and respond to review feedback
5. Celebrate when your PR is merged! 🎉

## Learning Resources

### Git/GitHub:
- [GitHub's Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)

### Python Game Development:
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Real Python Pygame Tutorial](https://realpython.com/pygame-a-primer/)

### General Programming:
- [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

Remember: Making mistakes is part of learning! Don't be afraid to experiment and ask questions. 💪
