import pygame
import math

class Collectible:
    """Base class for collectible items"""
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.animation_time = 0
    
    def draw(self, screen):
        """Draw the collectible with animation"""
        self.animation_time += 0.1
        
        # Pulsing effect
        pulse = math.sin(self.animation_time) * 0.2 + 1
        current_radius = int(self.radius * pulse)
        
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), current_radius)

class Gem(Collectible):
    """Gem collectible worth 100 points"""
    def __init__(self, x, y):
        super().__init__(x, y, radius=8, color=(0, 255, 0))  # Green gems
    
    def draw(self, screen):
        """Draw gem with sparkle effect"""
        self.animation_time += 0.15
        
        # Main gem
        pulse = math.sin(self.animation_time) * 0.3 + 1
        current_radius = int(self.radius * pulse)
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), current_radius)
        
        # Inner sparkle
        sparkle_color = (150, 255, 150)
        sparkle_radius = max(1, int(current_radius * 0.5))
        pygame.draw.circle(screen, sparkle_color, (int(self.x), int(self.y)), sparkle_radius)

class PowerUp(Collectible):
    """Power-up collectible that gives temporary invincibility"""
    def __init__(self, x, y):
        super().__init__(x, y, radius=12, color=(255, 0, 255))  # Magenta power-ups
    
    def draw(self, screen):
        """Draw power-up with special effects"""
        self.animation_time += 0.2
        
        # Rotating star effect
        star_points = 8
        outer_radius = self.radius
        inner_radius = self.radius * 0.5
        
        points = []
        for i in range(star_points * 2):
            angle = (i * math.pi / star_points) + self.animation_time
            if i % 2 == 0:
                # Outer point
                radius = outer_radius
            else:
                # Inner point
                radius = inner_radius
            
            x = self.x + math.cos(angle) * radius
            y = self.y + math.sin(angle) * radius
            points.append((int(x), int(y)))
        
        # Draw star
        if len(points) >= 6:
            pygame.draw.polygon(screen, self.color, points)
        
        # Draw pulsing center
        pulse = math.sin(self.animation_time * 2) * 0.5 + 1
        center_radius = int(self.radius * 0.3 * pulse)
        center_color = (255, 255, 255)  # White center
        pygame.draw.circle(screen, center_color, (int(self.x), int(self.y)), center_radius)
