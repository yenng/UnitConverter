import mp2
import unittest

class Testing(unittest.TestCase):

    def test_converter_number_system(self):
        """Make sure converter successfully convert decimal 97 to hexadecimal 61."""
        
        input_values = [0,0,2,'97']

        output = []
        expected_result = "Result: 97 Dec equals to 61 Hex"

        def mock_input(s):
            output.append(s)
            return input_values.pop(0)

        mp2.input = mock_input
        mp2.print = lambda s:output.append(s)
        mp2.main()
        self.assertEqual(output[-1],expected_result)

    def test_converter_temperature(self):
        """Make sure converter successfully convert 36°C to 96.8°F."""
        
        input_values = [1,0,1,'36']

        output = []
        expected_result = "Result: 36 Celsius(°C) equals to 96.8 Fahrenheit(°F)"

        def mock_input(s):
            output.append(s)
            return input_values.pop(0)

        mp2.input = mock_input
        mp2.print = lambda s:output.append(s)
        mp2.main()
        self.assertEqual(output[-1],expected_result)

    def test_converter_weight(self):
        """Make sure converter successfully convert 2kg to 4.41 lbs."""
        
        input_values = [2,0,2,'2']

        output = []
        expected_result = "Result: 2 Kilogram(kg) equals to 4.41 Pound(lbs)"

        def mock_input(s):
            output.append(s)
            return input_values.pop(0)

        mp2.input = mock_input
        mp2.print = lambda s:output.append(s)
        mp2.main()
        self.assertEqual(output[-1],expected_result)

    def test_converter_length(self):
        """Make sure converter successfully convert 2000m to 1.24 Mile(mi)."""
        
        input_values = [3,0,3,'2000']

        output = []
        expected_result = "Result: 2000 Meter(m) equals to 1.24 Mile(mi)"

        def mock_input(s):
            output.append(s)
            return input_values.pop(0)

        mp2.input = mock_input
        mp2.print = lambda s:output.append(s)
        mp2.main()
        self.assertEqual(output[-1],expected_result)

    def test_converter_area(self):
        """Make sure converter successfully convert 20 m^2 to 215.29 ft^2."""
        
        input_values = [4,0,1,'20']

        output = []
        expected_result = "Result: 20 Square meter(m^2) equals to 215.29 Square foot(ft^2)"

        def mock_input(s):
            output.append(s)
            return input_values.pop(0)

        mp2.input = mock_input
        mp2.print = lambda s:output.append(s)
        mp2.main()
        self.assertEqual(output[-1],expected_result)

    def test_converter_angle(self):
        """Make sure converter successfully convert 90° to 1.57rad."""
        
        input_values = [5,0,2,'90']

        output = []
        expected_result = "Result: 90 Degree(°) equals to 0.5 Pi Radian(π rad)"

        def mock_input(s):
            output.append(s)
            return input_values.pop(0)

        mp2.input = mock_input
        mp2.print = lambda s:output.append(s)
        mp2.main()
        self.assertEqual(output[-1],expected_result)

    

if __name__ == '__main__':
    unittest.main()
    
