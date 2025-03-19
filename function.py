import numpy as np 



# This could be adding the value for each like add ect or just do I do what GPlearn did with the function class becuase it so clean 

class Function:
    def __init__(self,
                *,
                function_set = None
                ):
        
        temp = function_set
        # so Ill unpack to which one is the problem and from there 
        self.function_set = function_set or {
            "add" : (self.add, 2 ), 
            "sub" : (self.sub, 2),
            "mul" : (self.mul, 2),
            "max" : (self.max, 2),
            "min" : (self.min, 2),
            "div" : (self.protected_division, 2),
           # "log" : (self.protected_log, 1),
            "sqrt" : (self.protected_square_root, 1),
            "inv" : (self.protected_inverse, 1)
        }    

    def __call__(self, function = None, *args, **kwds):
        # TODO check to see if there is to full fill the artery
        if function == None:
            print("No function type was defined")
            return -1 
        if function not in self.function_set:
            print(f"Unknown function type: {function}")
            return -1
        
        func, artery_count = self.function_set[function]

        if len(args) != artery_count:
            print("Artery do not match")
            return -1 
        
        return func(*args)


    def get_function_set(self):
        return self.function_set.copy()

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

    # Had to get rid of np.where because it does all the operatio first then check which to chose from 
    def protected_division(self,numerator,denominator):
        return np.divide(numerator, denominator) if np.abs(denominator) > 0.001 else 0

    def protected_log(self,x):
        return np.log(x) if np.abs(x) > .01 else 0

    def protected_square_root(self,x):
        return np.sqrt(np.abs(x))

    def protected_inverse(self,x):
        return x * -1 

    def custom_function(self):
        pass


if __name__ == "__main__":
    print("hello")
    f = Function()
    print(f("add", 3, 5))  # correct 
    print(f("div", 4, 0))  # divide by zero error 
    print(f("sqrt", -16))  
    print(f("log",0))
    
    # # Adding a custom function
    # f.add_custom_function("pow", lambda x, y: x ** y, 2)
    # print(f("pow", 2, 3))  
    print("-------------")
    # Testing wrong arity
    print(f("add", 2))



