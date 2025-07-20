import pygame
import math
import random

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 12
        self.speed = 3.2  # Slightly faster than player's normal speed
        self.scared_speed = 2.5  # Slower when player has power-up
        
        # Colors
        self.normal_colors = [(255, 0, 0), (255, 165, 0), (255, 192, 203), (0, 255, 255)]  # Red, Orange, Pink, Cyan
        self.scared_color = (0, 0, 255)  # Blue when scared
        self.color_index = random.randint(0, len(self.normal_colors) - 1)
        
        # AI behavior
        self.target_x = x
        self.target_y = y
        self.direction_change_timer = 0
        self.direction_change_interval = 60  # Change direction every 60 frames when scared
    
    def update(self, player_x, player_y, game_map, player_has_power_up):
        """Update enemy position and AI behavior"""
        if player_has_power_up:
            # Run away from player
            self._flee_from_player(player_x, player_y, game_map)
            current_speed = self.scared_speed
        else:
            # Chase player
            self._chase_player(player_x, player_y, game_map)
            current_speed = self.speed
        
        # Calculate direction to target
        dx = self.target_x - self.x
        dy = self.target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        if distance > 0:
            # Normalize direction
            dx /= distance
            dy /= distance
            
            # Calculate new position
            new_x = self.x + dx * current_speed
            new_y = self.y + dy * current_speed
            
            # Check if new position is valid
            if game_map.is_valid_position(new_x, new_y, self.radius):
                self.x = new_x
                self.y = new_y
            else:
                # If can't move toward target, try alternative directions
                self._try_alternative_movement(game_map, current_speed)
    
    def _chase_player(self, player_x, player_y, game_map):
        """Set target to chase the player"""
        self.target_x = player_x
        self.target_y = player_y
    
    def _flee_from_player(self, player_x, player_y, game_map):
        """Set target to flee from the player"""
        self.direction_change_timer += 1
        
        if self.direction_change_timer >= self.direction_change_interval:
            self.direction_change_timer = 0
            
            # Calculate direction away from player
            dx = self.x - player_x
            dy = self.y - player_y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            
            if distance > 0:
                # Normalize and extend the flee direction
                dx /= distance
                dy /= distance
                
                # Set target far away from player
                flee_distance = 200
                self.target_x = self.x + dx * flee_distance
                self.target_y = self.y + dy * flee_distance
                
                # Clamp target to screen bounds
                self.target_x = max(self.radius, min(game_map.width - self.radius, self.target_x))
                self.target_y = max(self.radius, min(game_map.height - self.radius, self.target_y))
    
    def _try_alternative_movement(self, game_map, speed):
        """Try moving in alternative directions when blocked"""
        directions = [
            (speed, 0),   # Right
            (-speed, 0),  # Left
            (0, speed),   # Down
            (0, -speed)   # Up
        ]
        
        random.shuffle(directions)
        
        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy
            
            if game_map.is_valid_position(new_x, new_y, self.radius):
                self.x = new_x
                self.y = new_y
                break
    
    def draw(self, screen, player_has_power_up):
        """Draw the enemy"""
        if player_has_power_up:
            color = self.scared_color
        else:
            color = self.normal_colors[self.color_index]
        
        # Draw main body
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
        
        # Draw simple eyes
        eye_offset = 4
        eye_radius = 2
        eye_color = (255, 255, 255)
        pupil_color = (0, 0, 0)
        
        # Left eye
        left_eye_x = int(self.x - eye_offset)
        left_eye_y = int(self.y - eye_offset)
        pygame.draw.circle(screen, eye_color, (left_eye_x, left_eye_y), eye_radius)
        pygame.draw.circle(screen, pupil_color, (left_eye_x, left_eye_y), 1)
        
        # Right eye
        right_eye_x = int(self.x + eye_offset)
        right_eye_y = int(self.y - eye_offset)
        pygame.draw.circle(screen, eye_color, (right_eye_x, right_eye_y), eye_radius)
        pygame.draw.circle(screen, pupil_color, (right_eye_x, right_eye_y), 1)
