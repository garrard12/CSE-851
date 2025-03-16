
import numpy as np

from function import *


TEMP_metric = []
TEMP_FUNCTION_SET = []
 
class LGP:
    def __init__(self,
                 *, # Following arguments need to be passed by key arguments 
                 population_size = 10, 
                 generation = 20,
                 stopping_criteria = .01, 
                 metric = TEMP_metric,
                 ## TODO this should change to a dic or make it were all those values become each thing 
                 p_crossover = .05,
                 p_mutation = .03,  

                 function_set = TEMP_FUNCTION_SET,  # this might be add back in to later 
                 constants = None, 
                 # This will be used to make the gp at first 
                 # maybe it should not surpassed the max
                 min_length = 0,
                 max_length = None,
                 seed = None

                 # Would be nice to add if I have time 
                 # parsimony_coefficient = .01,
                 # tournament_size = 5
                 # warm_start = False
                 # random_state = False
                 ):
       
        self.population_size = population_size
        self.generation = generation
        self.stopping_criteria = stopping_criteria 
        self.function_set = function_set  
        self.metric = metric
        self.p_crossover = p_crossover
        self.p_mutation = p_mutation 
        self.constants = constants
        self.min_length = min_length
        self.max_length = max_length
        self.seed = seed 


        #self.parsimony_coefficient = parsimony_coefficient
        #self.tournament_size =  tournament_size
        #self.warm_start = warm_start
        #self.random_state = random_state
    

    def run_program():
        # runs all of the 
        pass

    def generate_program(self,):
        # what is need to make the program 
        # the min length
        # max length 
        # what values for constraints 
        program = []
        for _ in range(self.min_length,self.max_length):
            pass


        return program
    

    def create_population():
        # how many pop are need for this 
        pass 

    # def fitness_models():
    #     # MSE - Means squared  error 
    #     # Normalized fitness 
    #     # classification accuracy 
    #     # RMSE 
    #     # Sum of squared Error 
    #     # Possible make it where they can add there own 
    #     pass 

    def interpert():
        # this pretty much run the program 
        # this might be replaced with run program 
        pass
    # def cross_over():
    #     # Is this going to be single point 
    #     # multiple point 
    #     # going to need to need to take
    #     pass 

    # def mutation(): 
    #     # what style of mutation will be used 
    #     # is this going to be changing constants or just the function 
    #     # Do I want to favor random or towards the font/end 
    #     pass

    def make_fitness_function():
        #look into how this is being checked 
        # is this a higher value better or lower better GPlearn use a boolean
        pass     

    # def make_function():
    #     # This allow user to add custom function, add sub etc to the set 
    #     # intake arteries  
    #     # Is the function a real thing  
    #     pass     

    # def protect_function():
    #     # this should be in it only file and make each of the function safe to be used 
    #     pass

    def print_program(self,message):
        # the program 
        # is this going to be the best 
        # the whole populations 
        # 
        print(message)

    


class fitness: 
    def __init__(self):
        pass

    

if __name__ == '__main__':
    test = LGP()
    test.print_program("this is a class")
    print("hello worlds ")

    print(np.__version__)
