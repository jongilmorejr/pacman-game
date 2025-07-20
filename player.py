import pygame
import math

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 15
        self.speed = 3
        self.power_speed = 4.5  # Faster speed during power-up
        self.color = (255, 255, 0)  # Yellow
        
        # Movement
        self.dx = 0
        self.dy = 0
    
    def update(self, keys, game_map, power_up_active):
        """Update player position based on input"""
        # Determine movement direction
        self.dx = 0
        self.dy = 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.dx = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.dx = 1
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.dy = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.dy = 1
        
        # Apply speed based on power-up status
        current_speed = self.power_speed if power_up_active else self.speed
        
        # Calculate new position
        new_x = self.x + self.dx * current_speed
        new_y = self.y + self.dy * current_speed
        
        # Check if new position is valid (not colliding with walls)
        if game_map.is_valid_position(new_x, new_y, self.radius):
            self.x = new_x
            self.y = new_y
    
    def draw(self, screen):
        """Draw the player"""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        
        # Draw a small mouth to make it look more like Pacman
        mouth_angle = 30  # degrees
        start_angle = math.radians(-mouth_angle // 2)
        end_angle = math.radians(mouth_angle // 2)
        
        # Create mouth based on movement direction
        if self.dx > 0:  # Moving right
            start_angle = math.radians(-mouth_angle // 2)
            end_angle = math.radians(mouth_angle // 2)
        elif self.dx < 0:  # Moving left
            start_angle = math.radians(180 - mouth_angle // 2)
            end_angle = math.radians(180 + mouth_angle // 2)
        elif self.dy > 0:  # Moving down
            start_angle = math.radians(90 - mouth_angle // 2)
            end_angle = math.radians(90 + mouth_angle // 2)
        elif self.dy < 0:  # Moving up
            start_angle = math.radians(270 - mouth_angle // 2)
            end_angle = math.radians(270 + mouth_angle // 2)
        
        # Draw the mouth (a small pie slice)
        if self.dx != 0 or self.dy != 0:  # Only draw mouth if moving
            mouth_points = [(int(self.x), int(self.y))]
            for angle in [start_angle, end_angle]:
                mouth_x = self.x + math.cos(angle) * self.radius
                mouth_y = self.y + math.sin(angle) * self.radius
                mouth_points.append((int(mouth_x), int(mouth_y)))
            
            if len(mouth_points) >= 3:
                pygame.draw.polygon(screen, (0, 0, 0), mouth_points)
    
    def collides_with(self, other):
        """Check collision with another object"""
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return distance < (self.radius + other.radius)
