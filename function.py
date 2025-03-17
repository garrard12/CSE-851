import numpy as np 


## TODO Make this a class

# This could be adding the value for each like add ect or just do I do what GPlearn did with the function class becuase it so clean 

class Function:
    def __init__(self,
                *,
                function_set = None
                ):
        
        self.function_set = function_set or {
            "add" : self.add,
            "sub" : self.sub,
            "mul" : self.mul,
            "max" : self.max,
            "min" : self.min,
            #"log" : self.protected_log,
            #"sqrt" : self.protected_square_root,
            #"inv" : self.protected_inverse,
            "div" : self.protected_division
        }    

    def __call__(self, function = None, *args, **kwds):
        # TODO check to see if there is to full fill the artery
        if function == None:
            print("No function type was defined")
            return -1 
        if function not in self.function_set:
            print(f"Unknown function type: {function}")
            return -1

        return self.function_set[function](*args,**kwds)


    def add(self,x,y):
        return np.add(x,y)
    
    def sub(self,x,y):
        return np.subtract(x,y)
    
    def mul(self,x,y):
        return np.multiply(x,y)
    
    def max(self,x,y):
        return np.maximum(x,y)
    
    def min(self,x,y):
        return np.minimum(x,y)

    def protected_division(self,numerator,denominator):
        return np.where(np.abs(denominator) > .001, np.divide(numerator,denominator),numerator)  


    ## TODO To add these will some way to keep track of artery of the program
    # def protected_log(self,x):
    #     return np.where(np.abs(x) > .001, np.log(x),0) 

    # def protected_square_root(self,x):
    #     return np.sqrt(np.abs(x))

    # def protected_inverse(self,x):
    #     return np.invert(np.abs(x))

    def custom_function(self):
        pass


if __name__ == "__main__":
    print("hello")



