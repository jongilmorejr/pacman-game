import pygame
import random

class GameMap:
    """Handles the game map, walls, and collision detection"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wall_thickness = 20
        self.walls = []
        
        # Colors
        self.wall_color = (0, 0, 255)  # Blue walls
        self.background_color = (0, 0, 0)  # Black background
        
        self._create_walls()
    
    def _create_walls(self):
        """Create the wall layout for the map with wider passages"""
        # Border walls
        self.walls.extend([
            # Top wall
            pygame.Rect(0, 0, self.width, self.wall_thickness),
            # Bottom wall
            pygame.Rect(0, self.height - self.wall_thickness, self.width, self.wall_thickness),
            # Left wall
            pygame.Rect(0, 0, self.wall_thickness, self.height),
            # Right wall
            pygame.Rect(self.width - self.wall_thickness, 0, self.wall_thickness, self.height)
        ])
        
        # Inner walls with wider passages (minimum 60 pixels between walls for character movement)
        wall_configs = [
            # Horizontal walls - with gaps for movement
            (100, 120, 180, self.wall_thickness),  # Gap at 280-320
            (340, 120, 180, self.wall_thickness),  # Gap at 520-560
            (580, 120, 180, self.wall_thickness),  # Gap at 760-800
            (820, 120, 100, self.wall_thickness),
            
            (160, 220, 140, self.wall_thickness),  # Gap at 300-360
            (380, 220, 160, self.wall_thickness),  # Gap at 540-580
            (600, 220, 140, self.wall_thickness),  # Gap at 740-780
            (800, 220, 120, self.wall_thickness),
            
            (120, 320, 160, self.wall_thickness),  # Gap at 280-340
            (360, 320, 140, self.wall_thickness),  # Gap at 500-560
            (580, 320, 160, self.wall_thickness),  # Gap at 740-780
            (800, 320, 120, self.wall_thickness),
            
            (140, 420, 180, self.wall_thickness),  # Gap at 320-380
            (400, 420, 140, self.wall_thickness),  # Gap at 540-600
            (620, 420, 160, self.wall_thickness),  # Gap at 780-820
            
            (100, 520, 160, self.wall_thickness),  # Gap at 260-320
            (340, 520, 180, self.wall_thickness),  # Gap at 520-580
            (600, 520, 140, self.wall_thickness),  # Gap at 740-800
            (820, 520, 100, self.wall_thickness),
            
            (180, 620, 160, self.wall_thickness),  # Gap at 340-400
            (420, 620, 140, self.wall_thickness),  # Gap at 560-620
            (640, 620, 160, self.wall_thickness),  # Gap at 800-840
            
            # Vertical walls - with gaps for movement
            (180, 60, self.wall_thickness, 140),   # Gap at 200-260
            (180, 280, self.wall_thickness, 120),  # Gap at 400-460
            (180, 480, self.wall_thickness, 120),
            
            (320, 80, self.wall_thickness, 120),   # Gap at 200-240
            (320, 260, self.wall_thickness, 140),  # Gap at 400-480
            (320, 500, self.wall_thickness, 100),
            
            (460, 60, self.wall_thickness, 140),   # Gap at 200-260
            (460, 280, self.wall_thickness, 120),  # Gap at 400-460
            (460, 480, self.wall_thickness, 120),
            
            (600, 80, self.wall_thickness, 120),   # Gap at 200-240
            (600, 260, self.wall_thickness, 140),  # Gap at 400-480
            (600, 500, self.wall_thickness, 100),
            
            (740, 60, self.wall_thickness, 140),   # Gap at 200-260
            (740, 280, self.wall_thickness, 120),  # Gap at 400-460
            (740, 480, self.wall_thickness, 120),
            
            (880, 80, self.wall_thickness, 120),   # Gap at 200-240
            (880, 260, self.wall_thickness, 140),  # Gap at 400-480
            (880, 500, self.wall_thickness, 100),
        ]
        
        for x, y, w, h in wall_configs:
            if x + w < self.width - self.wall_thickness and y + h < self.height - self.wall_thickness:
                self.walls.append(pygame.Rect(x, y, w, h))
    
    def is_valid_position(self, x, y, radius):
        """Check if a position is valid (not colliding with walls)"""
        # Check screen boundaries
        if x - radius < 0 or x + radius > self.width:
            return False
        if y - radius < 0 or y + radius > self.height:
            return False
        
        # Check wall collisions
        entity_rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        
        for wall in self.walls:
            if entity_rect.colliderect(wall):
                return False
        
        return True
    
    def get_valid_positions(self):
        """Get a list of valid positions for spawning collectibles"""
        valid_positions = []
        step = 50  # Larger grid step for better spacing
        
        for x in range(step, self.width - step, step):
            for y in range(step, self.height - step, step):
                if self.is_valid_position(x, y, 20):  # Use larger radius for more spacing
                    valid_positions.append((x, y))
        
        return valid_positions
    
    def get_player_start_position(self):
        """Get a safe starting position for the player"""
        # Start in a safe area (left side of the map)
        for x in range(60, 150, 20):
            for y in range(60, 150, 20):
                if self.is_valid_position(x, y, 20):
                    return (x, y)
        
        # Fallback position
        return (80, 80)
    
    def get_enemy_start_positions(self):
        """Get starting positions for enemies"""
        positions = []
        
        # Try to place enemies in different areas of the map with better spacing
        candidate_areas = [
            (self.width - 200, 60, self.width - 60, 180),      # Top right
            (self.width - 200, self.height - 180, self.width - 60, self.height - 60),  # Bottom right
            (60, self.height - 180, 200, self.height - 60),     # Bottom left
            (self.width // 2 - 80, self.height // 2 - 80, self.width // 2 + 80, self.height // 2 + 80)  # Center
        ]
        
        for i, (min_x, min_y, max_x, max_y) in enumerate(candidate_areas):
            if len(positions) >= 4:
                break
                
            # Try to find a valid position in this area
            for attempt in range(100):  # More attempts
                x = random.randint(min_x, max_x)
                y = random.randint(min_y, max_y)
                
                if self.is_valid_position(x, y, 20):  # Larger spacing check
                    # Make sure it's not too close to other enemies
                    too_close = False
                    for existing_pos in positions:
                        distance = ((x - existing_pos[0]) ** 2 + (y - existing_pos[1]) ** 2) ** 0.5
                        if distance < 80:  # Minimum distance between enemies
                            too_close = True
                            break
                    
                    if not too_close:
                        positions.append((x, y))
                        break
        
        # If we couldn't place all 4 enemies, use fallback positions
        fallback_positions = [
            (self.width - 100, 100),
            (self.width - 100, self.height - 100),
            (100, self.height - 100),
            (self.width // 2, self.height // 2)
        ]
        
        while len(positions) < 4:
            fallback_pos = fallback_positions[len(positions)]
            if self.is_valid_position(fallback_pos[0], fallback_pos[1], 15):
                positions.append(fallback_pos)
            else:
                # Emergency fallback
                positions.append((200 + len(positions) * 100, 200))
        
        return positions[:4]
    
    def draw(self, screen):
        """Draw the map"""
        # Draw walls
        for wall in self.walls:
            pygame.draw.rect(screen, self.wall_color, wall)
