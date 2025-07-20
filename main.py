import pygame
import sys
import time
from game import Game

def main():
    """Main entry point for the Pacman-style game"""
    pygame.init()
    
    # Initialize the game
    game = Game()
    
    # Game loop
    clock = pygame.time.Clock()
    running = True
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game.game_over:
                    # Restart game
                    game = Game()
        
        # Update game state
        if not game.game_over:
            game.update()
        
        # Draw everything
        game.draw()
        
        # Control frame rate
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
