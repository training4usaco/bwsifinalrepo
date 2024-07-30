import numpy as np
import random

class Particle:
    
    def __init__(self, num_particles, dimensions, bounds, c1, c2, w):
        self.num_particles = num_particles
        self.dimensions = dimensions
        self.bounds = bounds
        self.c1 = c1  
        self.c2 = c2  
        self.w = w    

        self.positions = np.array([[random.uniform(bounds[i][0], bounds[i][1]) for i in range(dimensions)] for _ in range(num_particles)])
        self.velocities = np.zeros((num_particles, dimensions))
        self.p_best_positions = self.positions.copy()
        
        self.g_best_position = None


    

