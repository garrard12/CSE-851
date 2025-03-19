
import unittest

from self_LGP_system import *


### TODO Write some Test case to make sure the code actual works
## TODO add comments on to everything 

class TestFIle(unittest.TestCase):

    def setUp(self):
        self.lgp = LGP()

    def test_default_values(self):
        self.assertEqual(self.lgp.population_size, 10)
        self.assertEqual(self.lgp.generation, 20)
        self.assertEqual(self.lgp.stopping_criteria, 0.01)
        self.assertEqual(self.lgp.p_crossover, 0.05)
        self.assertEqual(self.lgp.p_mutation, 0.03)
        self.assertEqual(self.lgp.function_set, [])
        self.assertEqual(self.lgp.metric, [])
    
    def test_custom_value(self): 
        new_lgp = LGP(population_size=100, generation=50, stopping_criteria=0.001, p_crossover=0.1, p_mutation=0.02)
        self.assertEqual(new_lgp.population_size, 100)
        self.assertEqual(new_lgp.generation, 50)
        self.assertEqual(new_lgp.stopping_criteria, 0.001)
        self.assertEqual(new_lgp.p_mutation, 0.02)
        self.assertEqual(new_lgp.p_crossover, 0.1)
        self.assertEqual(new_lgp.function_set, [])
        self.assertEqual(new_lgp.metric, [])


    

    
if __name__ == '__main__':
    unittest.main()