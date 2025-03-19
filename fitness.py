
import numpy as np 





class Fitness:
    def __init__(self,
                #  *,
                #  fitness = None,
                 ):
        
        # TODO comment about what the true or false are for 
        # True is to Max the fitness, False is to Mini
        self.all_fitness = {
            "mse" : (self.mean_square_error,False),
            "rmse" : (self.root_mean_square_error,False),
            "sse" : (self.sum_squared_error,False),
            "normalized" : (self.normalized,False),
        }

    def __call__(self,fitness = None ,*args, **kwds):
        if fitness == None:
            print("Please assign a fitness")
            return -1 
        if fitness not in self.all_fitness:
            print(f"Invalid fitness function ", fitness)
            return -1

        print("*args",*args)
        return self.all_fitness[fitness](*args)

    def get_all_fitness(self):
        return self.all_fitness.copy()

    def check_numpy_array(self,x):
        if isinstance(x, np.ndarray):
            return x
        return np.array(x)

    def mean_square_error(self,true,pred):
        true = self.check_numpy_array(true)
        pred = self.check_numpy_array(pred)
        return np.mean((true-pred)**2)

    def root_mean_square_error(self,true,pred):
        true = self.check_numpy_array(true)
        pred = self.check_numpy_array(pred)
        return np.sqrt(np.mean((true-pred)**2))

    def sum_squared_error(self,true, pred):
        true = self.check_numpy_array(true)
        pred = self.check_numpy_array(pred)
        return np.sum((true - pred) ** 2)

    def normalized(self,fitness_list):
        '''
        A list of fitness from the GP model
        fitness_list: numpy array
        '''
        fitness_list = self.check_numpy_array(fitness_list)
        min_fitness = np.min(fitness_list)
        max_fitness = np.max(fitness_list)
        return (fitness_list - min_fitness) / (max_fitness - min_fitness)