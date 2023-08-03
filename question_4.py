"""
Question 4
Input - python programming
Expected output - 2

Time Complexity Achieved - O(n)
Time Complexity Reasoning - As we have one for loop to iterate
every single character in the string
"""


class Question4:
    """Class for question 4"""

    vowels = [
        'a', 'e', 'i', 'o', 'u'
    ]

    def find_vowels_score(self, input_string):
        """
        Function to find the number of vowels and respective score
        :param input_string:
        :return result_score:
        """
        # Converting string to lowercase
        input_string = input_string.casefold()

        # Splitting input string into a word list
        words = input_string.split()

        # Declaring count & score
        count = 0
        result_score = 0

        # Iterating each word to find number of vowels and calculate score accordingly
        for word in words:
            for char in word:
                # If char is vowel then incrementing count
                if char in self.vowels:
                    count += 1

            # Checking if even vowels or not
            if (count % 2) == 0:
                result_score += 2
            else:
                result_score += 1

            count = 0

        return result_score


if __name__ == '__main__':
    inp_str = "python programming"
    question = Question4()
    print("Input string - " + str(inp_str))
    print("Output - " + str(question.find_vowels_score(inp_str)))
