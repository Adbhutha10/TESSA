import math

class Environment:
    def __init__(self, width=100, height=100):
        self.width = width
        self.height = height
        
        # Global nutrients for Phase 2 (simplification)
        # In the future, this will be a 2D array for spatial diffusion
        self.nutrients = {
            "glucose": 100.0,
            "oxygen": 100.0,
            "toxicity": 0.0
        }
    
    def get_attribute(self, attribute_name):
        """Fetches a global environmental attribute."""
        return self.nutrients.get(attribute_name, 0.0)

    def is_within_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def calculate_distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
