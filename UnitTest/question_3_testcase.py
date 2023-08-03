import unittest
import question_3


class Test(unittest.TestCase):
    """
    Test cases for question 4
    """

    question = question_3.Question3()

    def test_0(self):
        input_list = [6, 5, 1, 2, 3]
        input_barriers = [
            [2, 2],
            [2, 1],
            [1, 10],
            [2, 8],
            [2, 4],
            [1, 2]
        ]
        expected_output = 5
        self.assertEqual(self.question.barriers_broken_by_batman(input_list, input_barriers), expected_output)

    def test_1(self):
        input_list = [1, 4, 2, 5, 1]
        input_barriers = [
            [2, 0],
        ]
        expected_output = 1
        self.assertEqual(self.question.barriers_broken_by_batman(input_list, input_barriers), expected_output)

    def test_2(self):
        input_list = [6, 5, 1, 2, 0]
        input_barriers = [
            [2, 2],
            [2, 1],
            [1, 10],
            [2, 8],
            [2, 4],
            [1, 2]
        ]
        expected_output = 0
        self.assertEqual(self.question.barriers_broken_by_batman(input_list, input_barriers), expected_output)

    def test_3(self):
        input_list = [0, 5, 1, 2, 3]
        input_barriers = []
        expected_output = 0
        self.assertEqual(self.question.barriers_broken_by_batman(input_list, input_barriers), expected_output)


if __name__ == '__main__':
    unittest.main()
