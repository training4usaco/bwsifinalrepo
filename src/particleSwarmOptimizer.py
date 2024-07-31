import numpy as np
import random
from sklearn.neighbors import KNeighborsClassifier

class PSO:
    def __init__(self, num_particles, dimensions, bounds):
        self.particles = [self.Particle(dimensions, bounds) for _ in range(num_particles)]


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


    def closest_neighbor(particle_positions, query_position, n_neighbors):
        X = np.array(particle_positions)
        y = np.zeros(X.shape[0])


        knn = KNeighborsClassifier(n_neighbors=n_neighbors)
        knn.fit(X, y)
            

        distances, indices = knn.kneighbors([query_position], n_neighbors=n_neighbors)
            
        closest_neighbors = [(X[i], distances[0][j]) for j, i in enumerate(indices[0])]
            
        return closest_neighbors
    
    def update_position(self, particles):
        particle_positions = [p.positions for p in particles if p is not self]

        neighbors = self.find_closest_neighbors(particle_positions, self.positions, n_neighbors=self.num_particles - 1)
        
        costs = [self.calculate_cost(neighbor[0]) for neighbor in neighbors]


        best_neighbor_index = np.argmin(costs)
        best_neighbor_position = neighbors[best_neighbor_index][0]

        self.positions = best_neighbor_position
        


        


    

