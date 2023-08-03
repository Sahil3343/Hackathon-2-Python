import unittest
import question_6


class Test(unittest.TestCase):
    """
    Test cases for question 6
    """

    question = question_6.Question6()

    def test_0(self):
        input_list = ['5C', '2D', '10C', '4S', '6S', '2H', '1S', '8D', '4C', '6C', '8H', '5S', '1H', '3C']
        expected_output = ['3C', '4C', '5C', '6C']
        self.assertEqual(self.question.finding_longest_continuous_numbers(input_list), expected_output)

    def test_1(self):
        input_list = ['5C']
        expected_output = ['5C']
        self.assertEqual(self.question.finding_longest_continuous_numbers(input_list), expected_output)

    def test_2(self):
        input_list = []
        expected_output = []
        self.assertEqual(self.question.finding_longest_continuous_numbers(input_list), expected_output)

    def test_3(self):
        input_list = ['14C', '2D', '10C', '4S', '6S', '2H', '1S', '8D', '4C', '6C', '8H', '5S', '1H', '3C']
        expected_output = ['4S', '5S', '6S']
        self.assertEqual(self.question.finding_longest_continuous_numbers(input_list), expected_output)

    def test_4(self):
        input_list = ['3C', '4C', '5C', '6C']
        expected_output = ['3C', '4C', '5C', '6C']
        self.assertEqual(self.question.finding_longest_continuous_numbers(input_list), expected_output)


if __name__ == '__main__':
    unittest.main()
