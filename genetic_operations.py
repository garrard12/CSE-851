import numpy as np 
import random


## TODO Make were they can favor up and lower mutation possible 

class BaseOperations:
    def __init__(self,
                 *,
                 constants = None,
                 variables = None,
                 operations = None,
                 seed = None

                ):
        if seed is not None:
            np.random.seed(seed)
            random.seed(seed)
     
        ## TODO Make sure these being regular list don't cause some kind of problems
        self.constants = constants or [i for i in range(-5,6)]

        self.operations = operations or ["+","-","*","/"] # To handle artery could do {+:(np.add,2)}
        
        self.variables = variables or  ["x","y","z"]

    def get_operations(self):
        return self.operations 
    
    def get_variables(self):
        return self.variables

    def get_constants(self):
        return self.constants 


##########################################################################################
## Mutations 
##########################################################################

## TODO DO I make it were there is something in the init class have know the mutation prob
## DONE? possible
class Mutation(BaseOperations):
    def __init__(self,
                 *,
                 mutation_prob = None,
                 constants = None,
                 variables = None,
                 operations = None,
                 seed = None
                ):        
        super().__init__(constants=constants, variables=variables, operations = operations, seed=seed)

        self.mutation_operations = { 
            "swap" : self.swap_mutation,
            #"single_point" : self.single_point_mutation,
            "scramble" : self.scramble_mutation,
            "inversion" : self.inversion_mutation,
            "custom" : self.custom_mutation
        }

        self.mutation_probs = mutation_prob or  {
            "swap" : .1,
            "single_point" : .1,
            "scramble" : .1,
            "inversion" : .1,
            "custom" : .1
        }

    def __call__(self,mutation_type=None,*args, **kwds):
        if mutation_type == None:
            raise ValueError("No mutation type was defined")
        if mutation_type not in self.mutation_operations:
            print(f"Unknown mutation type: {mutation_type}")
            raise ValueError(f"Unknown mutation type: {mutation_type}")

        return self.mutation_operations[mutation_type](*args) if random.random() < self.mutation_probs[mutation_type] else args[0]


    # For the function below I already know I am doing the mutation
    # TODO 
    # def single_point_mutation(self,program):

    #     ## TODO When working with artirty this is the only one that will need to be updated 
    #     mutation_point = random.randint(0,len(program) - 1)  
    #     program[mutation_point] = random.choice(self.operations + self.constants) 
    #     return program
    
    # NOTE Works
    def swap_mutation(self,program):
        if len(program) < 2: 
            print("Swap need at least length 2")
            return program 

       # print(f"Program before swap {program}")
        index_one = random.randint(1,len(program) - 1) 
        index_two = random.randint(1,len(program) - 1)

        ## NOTE: Should I delete the below cause it make sure a mutation is happening but it is adding in more 
        # human involvement    
        while index_two == index_one: 
            index_one = random.randint(0,len(program) - 1) 

        # Swap the index values
        program[index_one], program[index_two] = program[index_two], program[index_one]
        #print(f"Program after swap {program}")
        return program

    # NOTE Works 
    def scramble_mutation(self,program):
        ''''
        Since Iam not keeping track of the arity at the moment 5:13 pm this 
        Will have low lickely of actually making anything helpful
        '''
        if len(program) < 2:
            print("Swap need at least length 2")
            return program

        upper_bound = random.randint(1,len(program) - 1)
        lower_bound = random.randint(0,upper_bound)
        #print(f"program before scramble {program}")
        program_segment = program[lower_bound:upper_bound]
        random.shuffle(program_segment)  
        program[lower_bound:upper_bound] = program_segment  
        #print(f"program after scramble {program}")
        return program 
    
    # NOTE WORKS 
    def inversion_mutation(self,program):
        if len(program) < 2:
            print("inversion need at least length 2")
            return program 

        upper_bound = random.randint(0,len(program) - 1)
        lower_bound = random.randint(0,upper_bound)

       # print(f"program before inversion {program}")
        program_segment = program[lower_bound:upper_bound]
        reversed_program = program_segment[::-1]
        program[lower_bound:upper_bound] = reversed_program
        #print(f"program after inversion {program}")
        return program

    def custom_mutation(self,program):
        '''
        Make sure each name is unquie when making them 
        '''
        pass 

##########################################################################
# Cross Over 
#########################################################################


class CrossOver(BaseOperations):
    def __init__(self,
                 *,
                 operations = None,
                 cross_prob = None,
                 constants = None,
                 variables = None,
                 seed = None,
                 ):
        super().__init__(constants=constants, variables=variables, operations = operations, seed=seed)
    
        self.cross_operations = {
            "single" : self.single_point_cross,
            "multi" : self.multi_point_cross
        }
        
        self.cross_prob = cross_prob or {
            "single" : .1,
            "multi" : .1 
        }

    def __call__(self, cross_type = None, *args, **kwds):
        if cross_type is None:
            raise ValueError()
        if cross_type not in self.cross_operations:
            raise ValueError("Operations not in Cross")

        print("return statment \n", self.cross_operations[cross_type](*args) if random.random() < self.cross_prob[cross_type] else (args[0],args[0]) )

        return self.cross_operations[cross_type](*args) if random.random() < self.cross_prob[cross_type] else (args[0],args[0]) 

    #NOTE Works
    def single_point_cross(self,program_one,program_two):



        max_cross_point = min(len(program_one),len(program_two))
        if max_cross_point <= 1:
            print("In valid cross point")
            return program_one,program_two

        cross_point = random.randint(1,max_cross_point - 1)

        #print(f"before single cross {program_one} {program_two}")

        off_spring_one = program_one[:cross_point] + program_two[cross_point:]
        off_spring_two = program_two[:cross_point] + program_one[cross_point:]

        #print(f"After single cross {off_spring_one} {off_spring_two}")
        print("in single cross point")
        return off_spring_one, off_spring_two

    #NOTE WORks
    def multi_point_cross(self,program_one,program_two):

        '''
        There is no min for the number to swaped so it could just do a single point swap  
        
        '''        
        max_cross_point = min(len(program_one), len(program_two))
        if max_cross_point <= 1:
            print("In valid cross point")
            return program_one,program_two


        upper_cross = random.randint(1, max_cross_point)
        lower_cross = random.randint(upper_cross, max_cross_point)

        print(f"before multi cross {program_one} {program_two}")

        off_spring_one = program_one[:upper_cross] + program_two[upper_cross:lower_cross] + program_one[lower_cross:]
        off_spring_two = program_two[:upper_cross] + program_one[upper_cross:lower_cross] + program_two[lower_cross:]
        print(f"After multi cross {off_spring_one} {off_spring_two}")

        return off_spring_one,off_spring_two

    def custom_cross(self):
        pass

