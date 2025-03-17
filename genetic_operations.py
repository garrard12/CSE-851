import numpy as np 


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
     
        ## TODO Make sure these being regular list don't cause some kind of problems
        self.constants = constants or [i for i in range(-5,6)]

        self.operations = operations or ["+","-","*","/"] # To handle artery could do {+:(np.add,2)}
        
        self.variables = variables or  ["x","y","z"]


##########################################################################################
## Mutations 
##########################################################################

## TODO DO I make it were there is something in the init class have know the mutation prob

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
            "single_point" : self.single_point_mutation,
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
            print("No mutation type was defined")
            return -1 
        if mutation_type not in self.mutation_operations:
            print(f"Unknown mutation type: {mutation_type}")
            return -1 

        # TODO Make sure this is a return orn
        # see if it should do the mutation or not this might git mover to fit functions later  
        return self.mutation_operations[mutation_type](*args, **kwds) if np.random.rand() < self.mutation_probs[mutation_type] else -1 


    # For the function below I already know I am doing the mutation
    def single_point_mutation(self,program):

        ## TODO When working with artirty this is the only one that will need to be updated 
        mutation_point = np.random.randint(0,len(program))  
        program[mutation_point] = np.random.choice(self.operations + self.constants) 
        return program

    def swap_mutation(self,program):
        if len(program) < 2: 
            print("Swap need at least length 2")
            return -1 

        index_one = np.random.randint(0,len(program)) 
        index_two = np.random.randint(0,len(program))

        ## NOTE: Should I do the below cause it make sure a mutation is happening but it is adding in more 
        # human involvement    
        while index_two == index_one: 
            index_one = np.random.randint(0,len(program)) 

        # Swap the index values
        program[[index_one, index_two]] = program[[index_two,index_one]]

        return program

    def scramble_mutation(self,program):
        ''''
        Since Iam not keeping track of the arity at the moment 5:13 pm this 
        Will have low lickely of actually making anything helpful
        '''
        if len(program) < 2:
            print("Swap need at least length 2")
            return -1 

        upper_bound = np.random.randint(0,len(program))
        lower_bound = np.random.randint(0,upper_bound)

        program_segment = program[lower_bound:upper_bound]
        np.random.shuffle(program_segment)
        program[lower_bound:upper_bound] = program_segment
        return program 

    def inversion_mutation(self,program):
        if len(program) < 2:
            print("Swap need at least length 2")
            return -1 

        upper_bound = np.random.randint(0,len(program))
        lower_bound = np.random.randint(0,upper_bound)

        program_segment = program[lower_bound:upper_bound]
        reversed_program = program_segment[::-1]
        program[lower_bound:upper_bound] = reversed_program

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
            print("Please select a cross type")
            return -1 
        if cross_type not in self.cross_operations:
            print("Operations not in Cross")
            return -1 
        
        return self.cross_operations[cross_type](*args, **kwds) if np.random.rand() < self.cross_prob[cross_type] else -1 

    def single_point_cross(self,program_one,program_two):

        max_cross_point = min(len(program_one),len(program_two))
        cross_point = np.random.randint(1,max_cross_point)

        off_spring_one = program_one[:cross_point] + program_two[cross_point:]
        off_spring_two = program_two[:cross_point] + program_one[cross_point:]

        return off_spring_one,off_spring_two


    def multi_point_cross(self,program_one,program_two):
        
        max_cross_point = min(len(program_one), len(program_two))

        upper_cross = np.random.randint(1, max_cross_point)
        lower_cross = np.random.randint(upper_cross, max_cross_point)

        off_spring_one = program_one[:upper_cross] + program_two[upper_cross:lower_cross] + program_one[lower_cross:]
        off_spring_two = program_two[:upper_cross] + program_one[upper_cross:lower_cross] + program_two[lower_cross:]

        return off_spring_one,off_spring_two

    def custom_cross(self):
        pass

