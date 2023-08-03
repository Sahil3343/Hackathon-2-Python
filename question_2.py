"""
Question 2
Input - This is a sample string, where chars are rotated by 3 keys on right side.
Expected output - Ilqg qg f gfcedy giuqxk, tlyuy nlfug fuy uwifiyh zo 3 syog wx uqkli gqhy.

Time Complexity Achieved - O(n)
Time Complexity Reasoning - As we have one loop that iterates through n characters
"""


class Question2:
    """Class for question 2"""

    qwerty_lower = {
        'qwertyuiop': 'qwertyuiop',
        'asdfghjkl': 'asdfghjkl',
        'zxcvbnm': 'zxcvbnm'
    }

    qwerty_upper = {
        'QWERTYUIOP': 'QWERTYUIOP',
        'ASDFGHJKL': 'ASDFGHJKL',
        'ZXCVBNM': 'ZXCVBNM',
    }

    def encrypt_string(self, input_string, n):
        """
        Function to encrypt a string
        :param input_string:
        :param n:
        :return result:
        """
        # Initializing result string
        result = ""

        for char in input_string:
            # Checking if current char is alphabet or not
            if char.isalpha():
                # Checking if current char is lower or upper
                if char.islower():
                    # Finding the corresponding row for current char
                    for row in self.qwerty_lower.values():
                        if char in row:
                            # Finding the position of the char
                            char_position = row.index(char)

                            # Moving char by n to the right
                            n_position = (char_position + n) % len(row)

                            # Finding encrypted char according to n position calculated
                            encrypted_char = row[n_position]

                            # Appending encrypted char to result string
                            result += encrypted_char
                elif char.upper():
                    # Finding the corresponding row for current char
                    for row in self.qwerty_upper.values():
                        if char in row:
                            # Finding the position of the char
                            char_position = row.index(char)

                            # Moving char by n to the right
                            n_position = (char_position + n) % len(row)

                            # Finding encrypted char according to n position calculated
                            encrypted_char = row[n_position]

                            # Appending encrypted char to result string
                            result += encrypted_char
            else:
                result += char

        return result


if __name__ == '__main__':
    inp_str = "This is a sample string, where chars are rotated by 3 keys on right side."
    inp_n = 3
    question = Question2()
    # print("Input list - " + str(inp_list))
    print("Output list - " + str(question.encrypt_string(inp_str, inp_n)))
