"""
Question 6
Input - ['5C', '2D', '10C', '4S', '6S', '2H', '1S', '8D', '4C', '6C', '8H', '5S', '1H', '3C']
Expected output - ['3C', '4C', '5C', '6C']

Time Complexity Achieved -
Time Complexity Reasoning -
"""
import re


class Question6:
    """Class for question 6"""
    shapes = {
        'H': [],
        'C': [],
        'D': [],
        'S': []
    }

    def finding_longest_continuous_numbers(self, input_list):
        """
        Function to find the longest continuous cards
        :param input_list:
        :return longest_continuous_cards:
        """

        if len(input_list) == 1:
            return input_list

        if len(input_list) == 0:
            return []

        # Creating regex patter
        pattern = r'^([1-9]|1[0-3])([HCDS])$'

        # Iterating through the input cards
        for item in input_list:
            match = re.search(pattern, item)

            # Checking if the item matches the correct format
            if match:
                digits = match.group(1)
                shape = match.group(2)

                # Appending the card number to the dictionary
                if shape in self.shapes:
                    temp_list = self.shapes.get(shape[0])
                    temp_list.append(int(digits))
                    self.shapes[shape[0]] = temp_list

        # Sorting the lists in the dictionary
        for shape in self.shapes:
            self.shapes[shape[0]].sort()

        # Initializing variables for storing the longest sequence and current sequence
        longest_sequence = []
        current_sequence = []

        # Iterating through each list in the dictionary for finding the longest sequence
        for shape in self.shapes.keys():

            if len(self.shapes[shape]) != 0:
                # Adding the first integer to the current sequence
                current_sequence = [f"{self.shapes[shape][0]}{shape}"]

                for i in range(1, len(self.shapes[shape])):
                    # Checking if current interation the increment of previous iteration
                    if self.shapes[shape][i] == self.shapes[shape][i - 1] + 1:
                        current_sequence.append(f"{self.shapes[shape][i]}{shape}")
                    else:
                        # Checking if the current sequence is greater than
                        # the longest sequence or not
                        if len(current_sequence) > len(longest_sequence):
                            # Copying current sequence to longest sequence
                            longest_sequence = current_sequence.copy()
                        current_sequence = [f"{self.shapes[shape][i]}{shape}"]

                # Final check to make sure that longest sequence is the longest
                if len(current_sequence) > len(longest_sequence):
                    longest_sequence = current_sequence

        return longest_sequence


if __name__ == '__main__':
    inp_list = ['5C', '2D', '10C', '4S', '6S', '2H', '1S', '8D', '4C', '6C', '8H', '5S', '1H', '3C']
    question = Question6()
    print("Input list - " + str(inp_list))
    print("Output list - " + str(question.finding_longest_continuous_numbers(inp_list)))
