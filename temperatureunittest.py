from temperaturebase import Temperature
from unittest import TestCase, main
#1 = 1 
#273.15 + 3 = 276.15
#(3 - 32) * 5 / 9 + 273.15 = 258.15
class pythonUnitTest(TestCase):
    def testKelvin(self):
        self.assertEqual(Temperature(1).kelvin, 1)

    def testCelsius(self):
        self.assertEqual(Temperature(celsius=3).kelvin, 276.15)

    def testFahrenheit(self):
        self.assertEqual(Temperature(fahrenheit=5).kelvin, 258.15)

    def testValues(self):
        self.assertFalse(Temperature(3).kelvin is float)
    
    def testValues(self):
        self.assertFalse(Temperature(7).kelvin is str)
if __name__ == '__main__':
    main()