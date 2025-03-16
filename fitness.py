
import numpy as np 

## TODO Make this a class



def check_numpy_array(x):
    if isinstance(x, np.ndarray):
        return x
    return np.array(x)

def mean_square_error(true,pred):
    true = check_numpy_array(true)
    pred = check_numpy_array(pred)
    return np.mean((true-pred)**2)

def root_mean_square_error(true,pred):
    true = check_numpy_array(true)
    pred = check_numpy_array(pred)
    return np.sqrt(np.mean((true-pred)**2))

def sum_squared_error(true, pred):
    true = check_numpy_array(true)
    pred = check_numpy_array(pred)
    return np.sum((true - pred) ** 2)

def normalized(fitness_list):
    '''
    A list of fitness from the GP model
    fitness_list: numpy array
    '''
    fitness_list = check_numpy_array(fitness_list)
    min_fitness = np.min(fitness_list)
    max_fitness = np.max(fitness_list)
    return (fitness_list - min_fitness) / (fitness_list - max_fitness)
