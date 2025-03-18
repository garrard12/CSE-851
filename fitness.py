
import numpy as np 

class Fitness:
    def __init__(self,
                #  *,
                #  fitness = None,
                 ):
        self.all_fitness = {
            "mse" : self.mean_square_error,
            "rmse" : self.root_mean_square_error,
            "sse" : self.sum_squared_error,
            "normalized" : self.normalized
        }

    def __call__(self,fitness = None ,*args, **kwds):
        if fitness == None:
            print("Please assign a fitness")
            return -1 
        if fitness not in self.all_fitness:
            print(f"Invalid fitness function ", fitness)
            return -1

        return self.all_fitness[fitness](*args,**kwds)

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
        return (fitness_list - min_fitness) / (fitness_list - max_fitness)
