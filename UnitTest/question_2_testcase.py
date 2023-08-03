import unittest
import question_2


class Test(unittest.TestCase):
    """
    Test cases for question 2
    """

    question = question_2.Question2()

    def test_0(self):
        inp_str = "This is a sample string, where chars are rotated by 3 keys on right side."
        inp_n = 3
        expected_output = "Ilqg qg f gfcedy giuqxk, tlyuy nlfug fuy uwifiyh zo 3 syog wx uqkli gqhy."
        self.assertEqual(self.question.encrypt_string(inp_str, inp_n), expected_output)

    def test_1(self):
        inp_str = "123456"
        inp_n = 3
        expected_output = "123456"
        self.assertEqual(self.question.encrypt_string(inp_str, inp_n), expected_output)

    def test_2(self):
        inp_str = "hello! welcome to this awesome code!!!"
        inp_n = 5
        expected_output = "siggr! uigzrbi pr psej huijrbi zrki!!!"
        self.assertEqual(self.question.encrypt_string(inp_str, inp_n), expected_output)

    def test_3(self):
        inp_str = ""
        inp_n = 3
        expected_output = ""
        self.assertEqual(self.question.encrypt_string(inp_str, inp_n), expected_output)

    def test_4(self):
        inp_str = "PYTHON IS COOL"
        inp_n = 3
        expected_output = "EOILWX QG NWWD"
        self.assertEqual(self.question.encrypt_string(inp_str, inp_n), expected_output)


if __name__ == '__main__':
    unittest.main()
