''''
TODO Find an example problem to test the code 
TODO Make it were the code actually runs 

TODO Make a .ibpy file showing everything that this program can do 
TODO Need to print the program and which one is the best 
TODO Comment all of the code 
TODO Fix the inputs it seems right now that I am having to hard code some of it
TODO There are many area that I return one sine it is invaled input so Ill need to change that 

TODO Think about a way to find a program that work
TODO I have no way have acess toa a true programs 

# EXTRA 
TODO Make it were you can add your own custom function 
    - Cross over 
    - Mutation 
    - fitness 
    - functions
TODO make it were the pip works 
'''

'''
Question to ask why do we have varible?

'''



import numpy as np
import random 

from .function import *
from .fitness import * 
from .genetic_operations import *

TEMP_metric = []
TEMP_FUNCTION_SET = []
 
class LGP:
    ## TODO Make sure these have the correct pre set values not none
    ## TODO I switch between function set and operation standizes  this
    def __init__(self,
                 *, # Following arguments need to be passed by key arguments 
                 population_size = 4, 
                 generation = 5,
                 stopping_criteria = .01, 
                 metric = "mse",
                 crossover_prob = None,
                 mutation_prob = None,  

                 # The reasons that these are none is that I define this in the class 
                 function_set = None,   
                 constants = None,
                 variables = None, 
                 # This will be used to make the gp at first 
                 # maybe it should not surpassed the max
                 min_length = 1,
                 max_length = 25,
                 seed = None

                 # Would be nice to add if I have time 
                 # parsimony_coefficient = .01,
                 # tournament_size = 5
                 # warm_start = False
                 # random_state = False
                 ):


        self.function_class = Function()

        self.fitness_class = Fitness()

        self.mutation_class = Mutation(mutation_prob=mutation_prob,
                                       constants=constants,
                                       variables=variables,
                                       operations=self.function_class.get_function_set(),
                                       seed=seed
                                       )
        
        self.cross_over_class = CrossOver(cross_prob=crossover_prob,
                                       constants=constants,
                                       variables=variables,
                                       operations=self.function_class.get_function_set(),
                                       seed=seed
                                       )
        
        if seed:
            np.seed(seed)
            random.seed(seed)

        self.population_size = population_size
        self.generation = generation
        self.stopping_criteria = stopping_criteria 
        self.function_set = self.function_class.get_function_set() 
        self.fitness_set = self.fitness_class.get_all_fitness()
        #self.variables_set = self.mutation_class.get_variables()
        self.metric = metric
        self.p_crossover = crossover_prob
        self.min_length = min_length
        self.max_length = max_length
        self.seed = seed

        #self.parsimony_coefficient = parsimony_coefficient
        #self.tournament_size =  tournament_size
        #self.warm_start = warm_start
        #self.random_state = random_state

    def __call__(self, *args, **kwds):
        print("in call for LGP")

        pass


    def print_all_program(self,population,str ):
        for i in population:
            print(str,i)


    def simple_tournament(self, population,pop_fitness,tournament_size=3):
        temp = []
        for i in range(len(population)):
            temp.append([population[i],pop_fitness[i]])

        # for i in range(len(population)):
        #     print(f"Simple tourment pop {population[i]} \n pop_fitness {pop_fitness[i]} \n {temp[i]}")
        
        contenders = random.sample(temp,tournament_size)
        # self.print_all_program(contenders,"contenders")
        

        fitness_contender = [contender[1] for contender in contenders]

        best_ind_fitness = 0
        if self.fitness_set[self.metric][1]:
            best_ind_fitness = max(fitness_contender)
        else:
            best_ind_fitness = min(fitness_contender)

        # print(best_ind_fitness)
        # self.print_all_program(fitness_contender,"fitness_contender")
        for contender in contenders:
            if contender[1] == best_ind_fitness:
                best_ind = contender
                break 

       # print(best_ind_fitness)
        # self.print_all_program(fitness_contender,"fitness_contender")
        # print("best_ind",best_ind)
        return best_ind

    def fit(self,):
        '''
        This is main function call to run the program 
        '''

        population = self.create_population()
        print("Population,",population)
        print("Population length", len(population))
        
        for _ in range(self.generation):
            
            population_values = self.interpreter(population=population)
            population_fitness = self.find_fitness(population_values)

            population = self.next_generation(population,population_fitness)
            print(f"New population  {population}")
            # run a toroment maybe do a normalition of the function
            #still need to create a new population
                
        return None


    def next_generation(self,population,population_fitness):
        '''
        
        '''
        new_population = []
        #i = 0 
        while len(new_population) < self.max_length:
            #TODO make a torment selection 
            parent1, _ = self.simple_tournament(population, population_fitness)
            parent2, _ = self.simple_tournament(population, population_fitness)

            temp_one = self.mutation_class("scramble",parent1)
            temp_two = self.mutation_class("scramble",parent2)

            #print(f"temp one {temp_one}")
            #print(f"number of values ",self.cross_over_class("single",temp_one, temp_two))


            offspring_one, offspring_two = self.cross_over_class("single",temp_one, temp_two)
            #print(f"offspring one {offspring_one} \n")
            # See if the programs are the same if so just add one the population and not both 
            if offspring_one == offspring_two:
                new_population.append(offspring_one)
            else:
                new_population.append(offspring_one)
                new_population.append(offspring_two)
            #print(f"new popuilation {new_population}")
            # print(f"{i} out of  {self.max_length}")
            # i+=1
            # new_population.append(offspring_one)
            # new_population.append(offspring_two)
            # new_population.append(temp_one)
        return new_population


    def find_fitness(self,population_value):
        '''
        
        
        '''
        # TODO this wont work for normalized since it returns a list not a int and if could fix but there gotta be a 
        # better way
        all_fitness = []
        for program_value in population_value:
            all_fitness.append(self.fitness_class(self.metric,1,program_value))
        return all_fitness
    
    def generate_program(self):
        ''''
        

        '''
        program_length = random.randint(self.min_length,self.max_length)
        program = []
        for _ in range(program_length): 
            operation = random.choice(list(self.function_set.keys()))
            x = random.choice(list(self.function_set.keys()))
            values_to_pick = self.cross_over_class.get_constants()# + self.cross_over_class.get_variables()
            
            if operation in ["log","sqrt","inv"]:
                # TODO Make this Dynamic for custom Functions
                x = random.choice(values_to_pick)
                program.append([operation,x])
            else:
                x,y = random.sample(values_to_pick,2)
                program.append([operation,x,y])
            # print("ind",program)
        return program
    
    def create_population(self):
        '''
        Makes the population of programs tha is decided in initiation of class  
        '''
        population = [self.generate_program() for _ in range(self.population_size)]
        return population

    def interpreter(self,population):
        '''
        
        '''
        #TODO to make this work with varibles 

        all_result = []
        for program in population:
            result = 0
            for ind in program:
                function_name, *args = ind
                result += self.function_class(function_name,*args) 
            all_result.append(result)
            # print("Program result",result) 
        return all_result
    
    def print_program(self,message):
        '''
        

        '''
        # the program 
        # is this going to be the best 
        # the whole populations 
        # 
        print(message)

    
if __name__ == '__main__':
    test = LGP()
    test.print_program("this is a class")
    print("hello worlds ")

    print(np.__version__)
