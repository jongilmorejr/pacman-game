import pygame
import random
import time
from player import Player
from enemy import Enemy
from collectible import Gem, PowerUp
from game_map import GameMap
from sound_manager import SoundManager

class Game:
    def __init__(self):
        # Screen dimensions
        self.SCREEN_WIDTH = 1024
        self.SCREEN_HEIGHT = 768
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Pacman-Style Game")
        
        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.YELLOW = (255, 255, 0)
        
        # Game state
        self.score = 0
        self.start_time = time.time()
        self.game_duration = 120  # 2 minutes in seconds
        self.game_over = False
        self.power_up_active = False
        self.power_up_start_time = 0
        self.power_up_duration = 10  # 10 seconds
        
        # Initialize game map
        self.game_map = GameMap(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        
        # Initialize sound manager
        self.sound_manager = SoundManager()
        
        # Initialize player
        start_pos = self.game_map.get_player_start_position()
        self.player = Player(start_pos[0], start_pos[1])
        
        # Initialize enemies
        self.enemies = []
        enemy_positions = self.game_map.get_enemy_start_positions()
        for pos in enemy_positions:
            self.enemies.append(Enemy(pos[0], pos[1]))
        
        # Initialize collectibles
        self.gems = []
        self.power_ups = []
        self._spawn_collectibles()
        
        # Font for UI
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Start background music
        self.sound_manager.start_background_music()
        
        # Power-up sound management
        self.power_up_sound_playing = False
    
    def _spawn_collectibles(self):
        """Spawn gems and power-ups at random valid positions"""
        valid_positions = self.game_map.get_valid_positions()
        
        # Spawn 20 gems
        for _ in range(20):
            if valid_positions:
                pos = random.choice(valid_positions)
                valid_positions.remove(pos)
                self.gems.append(Gem(pos[0], pos[1]))
        
        # Spawn 4 power-ups
        for _ in range(4):
            if valid_positions:
                pos = random.choice(valid_positions)
                valid_positions.remove(pos)
                self.power_ups.append(PowerUp(pos[0], pos[1]))
    
    def update(self):
        """Update game state"""
        # Check if game time is up
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= self.game_duration:
            self.game_over = True
            # Stop power-up when game ends
            self.power_up_active = False
            self.power_up_sound_playing = False
            return
        
        # Check if all collectibles are collected
        if not self.gems and not self.power_ups:
            self.game_over = True
            # Stop power-up when game ends
            self.power_up_active = False
            self.power_up_sound_playing = False
            return
        
        # Handle power-up timer
        if self.power_up_active:
            if time.time() - self.power_up_start_time >= self.power_up_duration:
                self.power_up_active = False
                self.power_up_sound_playing = False
        else:
            if self.power_up_sound_playing:
                self.power_up_sound_playing = False
        
        # Update player
        keys = pygame.key.get_pressed()
        self.player.update(keys, self.game_map, self.power_up_active)
        
        # Update enemies
        for enemy in self.enemies:
            enemy.update(self.player.x, self.player.y, self.game_map, self.power_up_active)
        
        # Check collisions with gems
        for gem in self.gems[:]:
            if self.player.collides_with(gem):
                self.gems.remove(gem)
                self.score += 100
                self.sound_manager.play_gem_sound()
        
        # Check collisions with power-ups
        for power_up in self.power_ups[:]:
            if self.player.collides_with(power_up):
                self.power_ups.remove(power_up)
                self.power_up_active = True
                self.power_up_start_time = time.time()
                self.sound_manager.play_powerup_sound()
                self.power_up_sound_playing = True
        
        # Check collisions with enemies
        for enemy in self.enemies[:]:
            if self.player.collides_with(enemy):
                if self.power_up_active:
                    # Player destroys enemy
                    self.enemies.remove(enemy)
                    self.score += 200
                else:
                    # Enemy destroys player
                    self.game_over = True
                    # Stop power-up when player dies
                    self.power_up_active = False
                    self.power_up_sound_playing = False
    
    def draw(self):
        """Draw everything on screen"""
        self.screen.fill(self.BLACK)
        
        # Draw game map
        self.game_map.draw(self.screen)
        
        # Draw collectibles
        for gem in self.gems:
            gem.draw(self.screen)
        
        for power_up in self.power_ups:
            power_up.draw(self.screen)
        
        # Draw player
        self.player.draw(self.screen)
        
        # Draw enemies
        for enemy in self.enemies:
            enemy.draw(self.screen, self.power_up_active)
        
        # Draw UI
        self._draw_ui()
        
        # Draw game over screen if needed
        if self.game_over:
            self._draw_game_over()
        
        pygame.display.flip()
    
    def _draw_ui(self):
        """Draw the user interface"""
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, self.WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw timer
        elapsed_time = time.time() - self.start_time
        remaining_time = max(0, self.game_duration - elapsed_time)
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)
        timer_text = self.font.render(f"Time: {minutes:02d}:{seconds:02d}", True, self.WHITE)
        self.screen.blit(timer_text, (10, 50))
        
        # Draw power-up status
        if self.power_up_active and not self.game_over:
            power_remaining = self.power_up_duration - (time.time() - self.power_up_start_time)
            # Ensure we don't show negative values
            power_remaining = max(0, power_remaining)
            power_text = self.font.render(f"POWER UP: {power_remaining:.1f}s", True, self.YELLOW)
            self.screen.blit(power_text, (10, 90))
        
        # Draw collectibles remaining
        collectibles_text = self.small_font.render(f"Gems: {len(self.gems)} | Power-ups: {len(self.power_ups)}", True, self.WHITE)
        self.screen.blit(collectibles_text, (10, 130))
    
    def _draw_game_over(self):
        """Draw game over screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(self.BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game over text
        game_over_text = self.font.render("GAME OVER", True, self.WHITE)
        text_rect = game_over_text.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2 - 40))
        self.screen.blit(game_over_text, text_rect)
        
        # Final score
        final_score_text = self.font.render(f"Final Score: {self.score}", True, self.WHITE)
        score_rect = final_score_text.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2))
        self.screen.blit(final_score_text, score_rect)
        
        # Restart instruction
        restart_text = self.small_font.render("Press R to restart", True, self.WHITE)
        restart_rect = restart_text.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2 + 40))
        self.screen.blit(restart_text, restart_rect)
