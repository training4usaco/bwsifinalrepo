import numpy as np
import math 
import random
from sklearn.neighbors import KNeighborsClassifier

class Particle:
    
    def __init__(self, params, dimensions, bounds, c1, c2, w):
        self.n = dimensions
        # self.bounds = bounds
        self.c1 = c1  
        self.c2 = c2  
        self.inertia = w    

        self.positions = np.array([[random.uniform(bounds[i][0], bounds[i][1]) for i in range(dimensions)] for _ in range(num_particles)])
        self.velocities = np.zeros((dimensions))
        self.best_positions = self.positions
        self.best_neighbor_positions = self.best_positions
        self.Us = np.random()
        self.accelerations = [1,1]
        self.n = dimensions
        self.cost = cf.customCost()
    def updateCost(self):
        self.cost = cf.customCost()


    def stepAlgorithm(self):
        
        
        for i in range(len(self.velocities)):
            inertia =  self.inertia*self.velocities[i] 
            cognitive = self.acceleration[0]*self.Us[0]*(self.best_positions[i]-self.positions[i])
            social = self.acceleration[1]*self.Us[1]*(self.best_neighbor_positions - self.positions[i])

            self.velocities[i] = inertia + cognitive + social

            self.positions[i] += self.velocities[i]


    def updateUs(self):
        for j in range(self.Us):
            for i in range(self.n):
                self.Us[j] = np.diag(np.random.rand(self.dimensions))

    

class Swarm:
    def __init__(self, particleList, dimensions, bounds = [0,math.pi]):
        self.particles = particleList
        self.num_particles = len(particleList)
        self.dims = dimensions
        self.bounds = [bounds*self.dims]
        self.lowestCosts = []

    def find_closest_neighbors(particle_positions, query_position, n_neighbors):
        X = np.array(particle_positions)
        y = np.zeros(X.shape[0])
        
        knn = KNeighborsClassifier(n_neighbors=n_neighbors)
        knn.fit(X, y)
        
        distances, indices = knn.kneighbors([query_position], n_neighbors=n_neighbors)
        
        closest_neighbors = [(X[i], distances[0][j]) for j, i in enumerate(indices[0])]
        
        return closest_neighbors

    def updateBestNeighbors(self):
        for particle in self.particles:
            particle_positions = [p.positions for p in self.particles]
            n_neighbors = self.num_particles 
            neighbors = self.find_closest_neighbors(particle_positions, particle.positions, n_neighbors)
            
            
            costs = []
            for neighbor in neighbors:
                neighbor_position = neighbor[0]  
                cost = self.calculate_cost(neighbor_position)
                costs.append(cost)
        
            best_neighbor_index = np.argmin(costs)
            best_neighbor_position = neighbors[best_neighbor_index][0]
            
             
            if best_neighbor_index != 0: 
                particle.best_neighbor_positions = best_neighbor_position
            
            particle.updateCost()
            self.lowestCosts.append(particle.cost)
    
    
    def stepAlgorithm(self):        
        for i in self.particles:
            i.stepAlgorithm()
