import numpy as np 


## TODO Make this a class

# This could be adding the value for each like add ect or just do I do what GPlearn did with the function class becuase it so clean 


# class Function:
    # def __init__(self,
    #              *,
    #              function_set = None
    #              ):
    #     self.function_set = function_set or {
    #         "add" : np.add(x,y),
    #         "sub" : np.subtract(),
    #         "div" : self.protected_division

    #     }
        
 
        # pass 

def __call__(self, *args, **kwds):
    pass

def protected_division(self,numerator,denominator):
    return np.where(np.abs(denominator) > .001, np.divide(numerator,denominator),numerator)  

def protected_log(self,x):
    return np.where(np.abs(x) > .001, np.log(x),0) 

def protected_square_root(self,x):
    return np.sqrt(np.abs(x))

def protected_inverse(self,x):
    return np.invert(np.abs(x))



if __name__ == "__main__":
    print("hello")



