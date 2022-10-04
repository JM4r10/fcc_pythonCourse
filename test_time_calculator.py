import unittest
import time_calculator

class Test_time_calculator(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None: #runs before anything else
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None: #runs after everything else
        print('teardownClass')    

    def setUp(self): #runs before every single test
        pass

    def tearDown(test): #runs after every single test
        pass    

    def test_add_time(self):
        print('test_add_time')
        self.assertEqual(time_calculator.add_time("8:16 PM", "466:02", "tuesday"),"6:18 AM, Monday (20 days later)") 
        self.assertEqual(time_calculator.add_time("8:16 PM", "466:02"),"6:18 AM (20 days later)")
        self.assertEqual(time_calculator.add_time("8:16 PM", "1:44", "tuesday"),"10:00 PM, Tuesday")  

if __name__ == '__main__':
    unittest.main()

#running it directly on terminal
# python –m unittest test_calc.py    

