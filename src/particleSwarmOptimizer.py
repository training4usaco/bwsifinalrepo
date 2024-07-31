import numpy as np
import math 
import random
import costfunc as cf


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
        self.

    def updateBestNeighbors(self):
        #set position to best neighbor positions (lowest cost positions)
        #append costs to lowestCosts
        pass
    def stepAlgorithm(self):        
        for i in self.particles:
            i.stepAlgorithm()

    
