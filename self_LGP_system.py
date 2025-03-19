''''
TODO Find an example problem to test the code 
TODO Make it were the code actually runs 
TODO Based on the Current layout there is not way to tell if it should be a min or max fitness 
    - This could be done in the fitness class when defining like the arity 
TODO Make a .ibpy file showing everything that this program can do 
TODO Need to print the program and which one is the best 
TODO Comment all of the code 
TODO Fix the inputs it seems right now that I am having to hard code some of it
TODO There are many area that I return one sine it is invaled input so Ill need to change that 

TODO Think about a way to find a program that work


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
                 ## TODO this should change to a dic or make it were all those values become each thing 
                 crossover_prob = None,
                 mutation_prob = None,  

                 # The reasons that these are none is that I define this in the class 
                 function_set = None,   
                 constants = None,
                 #variables = None, 
                 # This will be used to make the gp at first 
                 # maybe it should not surpassed the max
                 min_length = 0,
                 max_length = 25,
                 seed = None

                 # Would be nice to add if I have time 
                 # parsimony_coefficient = .01,
                 # tournament_size = 5
                 # warm_start = False
                 # random_state = False
                 ):
        

       
        # self.population_size = population_size
        # self.generation = generation
        # self.stopping_criteria = stopping_criteria 
        # self.function_set = function_set  
        # self.metric = metric
        # self.p_crossover = crossover_prob
        # self.min_length = min_length
        # self.max_length = max_length
        # self.seed = seed 

        # These will need there values for the class 


        self.function_class = Function()

        self.fitness_class = Fitness()

        self.mutation_class = Mutation(mutation_prob=mutation_prob,
                                       constants=constants,
                                      # variables=variables,
                                       operations=self.function_class.get_function_set(),
                                       seed=seed
                                       )
        
        self.cross_over_class = CrossOver(cross_prob=crossover_prob,
                                       constants=constants,
                                      # variables=variables,
                                       operations=self.function_class.get_function_set(),
                                       seed=seed
                                       )
        
        

        self.population_size = population_size
        self.generation = generation
        self.stopping_criteria = stopping_criteria 
        self.function_set = self.function_class.get_function_set() 
        self.fitness_set = self.fitness_class.get_all_fitness()
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


    def fit(self,):
        '''
        This is main function call to run the program 
        '''

        population = self.create_population()
        print("Population,",population)
        print("Population length", len(population))
        
        for _ in range(self.generation):
            
            value = self.interpreter(population=population)
            

        
                
        return None


    def next_generation(self,population):
        '''
        
        '''
        new_population = []
        for _ in range(len(population) // 2):
            #TODO make a torment selection 
            program_one, program_two = np.random.choice(population,size=2,replace=False)

            temp_one = self.mutation_class(program_one,mutation_type="single")
            temp_two = self.mutation_class(program_two,mutation_type="single")
            off_spring_one,off_spring_two = self.cross_over_class(temp_one,temp_two,cross_type="single")
            
            new_population.append(off_spring_one)
            new_population.append(off_spring_two)
            # TODO check to see if return -1 
        
        return new_population


    def find_fitness(self,population):
        '''
        
        
        '''
        # TODO this wont work for normalized since it returns a list not a int and if could fix but there gotta be a 
        # better way
        all_fitness = []
        for program in population:
            all_fitness.append(self.fitness_class(self.metric,program))

        if all_fitness == -1:
            return -1 
        return all_fitness
    
    def generate_program(self):
        ''''
        

        '''
        program_length = np.random.randint(self.min_length,self.max_length)
        program = []
        for _ in range(program_length): 
            operation = np.random.choice(list(self.function_set.keys()))
            x = np.random.choice(list(self.function_set.keys()), size=1, replace=True) # This is in an np array and it is going to cuase a problem
            # print("x",x)
            values_to_pick = self.cross_over_class.get_constants() #+ self.cross_over_class.get_variables()
            if operation in ["log","sqrt","inv"]:
                # TODO Make this Dynamic for custom fucntions
                # [0] is to ignore the type picked
                x = np.random.choice(values_to_pick, size=1, replace=False)[0]
                program.append([operation,x])
            else:
                x,y = np.random.choice(values_to_pick, size=2, replace=True)
                program.append([operation,x,y])
            # print("ind",program)
        return program
    

    ## left off here asking if need vaible aand ['log', array(['0'], dtype='<U21')] is this made when running a single operation

    def create_population(self):
        '''
        Makes the population of programs tha is decided in initiation of class  
        '''
        population = [self.generate_program() for _ in range(self.population_size)]
        return population

    def interpreter(self,population):
        '''
        
        '''
        all_result = []
        for program in population:
            result = 0
            for ind in program:
                function_name, *args = ind
                # print(function_name)
                # print(*args)
                # print(self.function_class(function_name,*args))
                result += self.function_class(function_name,*args) 
                # print()
            all_result.append(result)
            # print("Program result",result) 
        return result
    
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
