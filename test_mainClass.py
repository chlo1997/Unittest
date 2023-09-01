
import unittest
from mainClass import Calculator, Aquarium
from pyunitreport import HTMLTestRunner

class TestCalculator(unittest.TestCase):
   
   
    def setUp(self): # Preparation code that run before each Test.
        self.calc = Calculator()
    
    def tearDown(self): # Clean-up all the registry and modification after each test completes
        self.calc = Calculator()
 
    def setUpModule(self):
        self.calc = Calculator()
        pass

    def tearDownModule():
        pass

    def test_addition(self):
        actual =  self.calc.addition(2,2)
        expected = 4
        self.assertEqual(actual, expected)  # Assert is the method of class that do the TesCase
  
    def test_addition2(self):
        actual =  2
        expected = 4
        self.assertTrue(self.calc.addition(actual,actual), expected)

    @unittest.skip("demonstrating skipping")
    def test_addition3(self):
        self.assertTrue(2, 2) 

    def test_subtraction(self):
        value1 =  5
        value2 =  2
        expected = 3
        self.assertEqual(self.calc.subtraction(value2, value1),-3)

class TestAddFishToAquarium(unittest.TestCase):
   
    def setUp(self): # Preparation code that run before each Test
        self.aqua = Aquarium()
    
    def tearDown(self): # Clean-up all the registry and modification after each test completes
        self.aqua = Aquarium()

    def test_add_fish_to_aquarium_success(self):
        actual = self.aqua.add_fish_to_aquarium(fish_list=["shark", "tuna"])
        expected = {"tank_a": ["shark", "tuna"]}
        self.assertEqual(actual, expected)

    def test_add_fish_to_aquarium_success2(self):
        actual = self.aqua.add_fish_to_aquarium(fish_list=["shark", "tuna"])
        expected = {"tank_a": ["error", "tuna"]}
        self.assertEqual(actual, expected)  
    
    def test_add_fish_to_aquarium_exception(self): # This test intend to cause exception at the function, but a specific one, so here the test its ok if the assert its true
        too_many_fish = ["shark"] * 25
        with self.assertRaises(ValueError) as exception_context:
            self.aqua.add_fish_to_aquarium(fish_list=too_many_fish)
        self.assertEqual(str(exception_context.exception),
                         "A maximum of 10 fish can be added to the aquarium")              

if __name__ == '__main__':
    unittest.main (verbosity=2)
    #unittest.main (verbosity=2,testRunner=HTMLTestRunner(output='C:/Git/Unittest'))