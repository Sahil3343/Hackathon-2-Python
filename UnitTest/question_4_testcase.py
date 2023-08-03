import unittest
import question_4


class Test(unittest.TestCase):
    """
    Test cases for question 4
    """

    question = question_4.Question4()

    def test_0(self):
        input_string = "python programming"
        expected_output = 2
        self.assertEqual(self.question.find_vowels_score(input_string), expected_output)

    def test_1(self):
        input_string = "rubiks cube"
        expected_output = 4
        self.assertEqual(self.question.find_vowels_score(input_string), expected_output)

    def test_2(self):
        input_string = ""
        expected_output = 0
        self.assertEqual(self.question.find_vowels_score(input_string), expected_output)

    def test_3(self):
        input_string = "aeiou aeiou"
        expected_output = 2
        self.assertEqual(self.question.find_vowels_score(input_string), expected_output)

    def test_4(self):
        input_string = "welcome to seneca global"
        expected_output = 5
        self.assertEqual(self.question.find_vowels_score(input_string), expected_output)

    def test_5(self):
        input_string = "e"
        expected_output = 1
        self.assertEqual(self.question.find_vowels_score(input_string), expected_output)


if __name__ == '__main__':
    unittest.main()
