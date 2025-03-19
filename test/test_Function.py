
# import unittest

# from lgp_system import function 

# ### TODO Write some Test case to make sure the code actual works
# ## TODO add comments on to everything 

# class TestFIle(unittest.TestCase):

#     def setUp(self):
#         self.lgp = Function()

#     def test_add(self):
#             self.assertEqual(self.f("add", 3, 5), 8)

#     def test_div(self):
#         self.assertEqual(self.f("div", 4, 0), 4)

#     def test_sqrt(self):
#         self.assertEqual(self.f("sqrt", -16), 4)

#     # def test_add_custom_function(self):
#     #     self.f.add_custom_function("pow", lambda x, y: x ** y, 2)
#     #     self.assertEqual(self.f("pow", 2, 3), 8)

#     def test_wrong_arity(self):
#         result = self.f("add", 2)
#         self.assertEqual(result, -1)

#     def test_unknown_function(self):
#         result = self.f("unknown", 2, 3)
#         self.assertEqual(result, -1)

#     def test_missing_function(self):
#         result = self.f(None, 2, 3)
#         self.assertEqual(result, -1)

# if __name__ == "__main__":
#     unittest.main()
   