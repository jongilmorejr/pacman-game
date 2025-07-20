# Developer Setup Guide

## For Your Son (New Developer)

### Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/jongilmorejr/pacman-game.git
   cd pacman-game
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the game**
   ```bash
   python main.py
   ```

### Development Workflow

#### Creating a New Feature

1. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   # Example: git checkout -b feature/new-enemy-type
   ```

2. **Make your changes**
   - Edit the relevant files
   - Test your changes by running `python main.py`
   - Make sure all imports still work

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add descriptive commit message"
   ```

4. **Push your branch**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request**
   - Go to GitHub.com
   - Click "Compare & pull request"
   - Describe what you changed
   - Request review from Dad (@jongilmorejr)

#### Working on Issues

1. **Check the Issues tab** on GitHub for tasks
2. **Assign yourself** to an issue you want to work on
3. **Create a branch** named after the issue (e.g., `issue-15-fix-sound-bug`)
4. **Follow the development workflow above**

### Code Style Guidelines

- Use descriptive variable names
- Add comments for complex logic
- Keep functions small and focused
- Test your changes before committing

### File Structure

```
pacman-game/
├── main.py              # Entry point
├── game.py              # Main game logic
├── player.py            # Player character
├── enemy.py             # Enemy AI
├── collectible.py       # Gems and power-ups
├── game_map.py          # Map and collision detection
├── sound_manager.py     # Sound effects
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── .github/workflows/  # CI/CD pipeline
└── sounds/             # Generated sound files (auto-created)
```

### Tips for Collaboration

1. **Always pull before starting work**
   ```bash
   git pull origin master
   ```

2. **Keep commits small and focused**
   - One feature or fix per commit
   - Write clear commit messages

3. **Test everything**
   - Make sure the game runs without errors
   - Test your new features thoroughly
   - Check that existing features still work

4. **Ask questions**
   - Use GitHub Issues for questions
   - Add comments in Pull Requests for discussion
   - Don't be afraid to experiment!

### Common Commands

```bash
# Check what branch you're on
git branch

# Switch to master branch
git checkout master

# Update your local master
git pull origin master

# See what files changed
git status

# See what changed in detail
git diff

# View commit history
git log --oneline
```

### Troubleshooting

**Game won't start?**
- Make sure you activated the virtual environment
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Make sure you're running Python 3.8 or higher

**Import errors?**
- Make sure you're in the project directory
- Check that all required files exist
- Try reinstalling dependencies

**Git issues?**
- Make sure you're in the right directory
- Check your branch with `git branch`
- Ask for help in GitHub Issues!
