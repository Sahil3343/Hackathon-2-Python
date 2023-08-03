import unittest
import question_1


class Test(unittest.TestCase):
    """
    Test cases for question 1
    """

    question = question_1.Question1()

    def test_0(self):
        input_list = [1, 4, 5, 6, 6, 5, 3, 5, 1, 6, 4, 6]
        expected_output = [6, 6, 6, 6, 5, 5, 5, 1, 1, 4, 4, 3]
        self.assertEqual(self.question.arranging_list(input_list), expected_output)

    def test_1(self):
        input_list = [1]
        expected_output = [1]
        self.assertEqual(self.question.arranging_list(input_list), expected_output)

    def test_2(self):
        input_list = [2, 2, 1, 1]
        expected_output = [1, 1, 2, 2]
        self.assertEqual(self.question.arranging_list(input_list), expected_output)

    def test_3(self):
        input_list = []
        expected_output = []
        self.assertEqual(self.question.arranging_list(input_list), expected_output)

    def test_4(self):
        input_list = [1, 1, 1, 1]
        expected_output = [1, 1, 1, 1]
        self.assertEqual(self.question.arranging_list(input_list), expected_output)

    def test_5(self):
        input_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
        expected_output = [5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1]
        self.assertEqual(self.question.arranging_list(input_list), expected_output)


if __name__ == '__main__':
    unittest.main()
