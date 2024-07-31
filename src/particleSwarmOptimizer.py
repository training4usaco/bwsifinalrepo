import numpy as np
import math 
import random
<<<<<<< HEAD
from sklearn.neighbors import KNeighborsClassifier

class PSO:
    def __init__(self, num_particles, dimensions, bounds):
        self.particles = [self.Particle(dimensions, bounds) for _ in range(num_particles)]
=======
import costfunc as cf
>>>>>>> 08bb20a464df2457519cf568b861869f00daf257


class Particle:
    
    def __init__(self, params, dimensions, bounds, c1, c2, w):
        self.n = dimensions
        # self.bounds = bounds
        self.c1 = c1  
        self.c2 = c2  
        self.inertia = w    

        self.positions = np.array([[random.uniform(bounds[i][0], bounds[i][1]) for i in range(dimensions)] for _ in range(num_particles)])
<<<<<<< HEAD
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
        


        
=======
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
>>>>>>> 08bb20a464df2457519cf568b861869f00daf257

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

    def updateBestNeighbors(self):
        #set position to best neighbor positions (lowest cost positions)
        #append costs to lowestCosts
        pass
    def stepAlgorithm(self):        
        for i in self.particles:
            i.stepAlgorithm()

    
