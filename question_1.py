"""
Question 1
Input - [1, 4, 5, 6, 6, 5, 3, 5, 1, 6, 4, 6]
Expected output - [6, 6, 6, 6, 5, 5, 5, 1, 1, 4, 4, 3]

Time Complexity Achieved - O(n log n)
Time Complexity Reasoning - As we are sorting a dictionary and also a single
for loop it will result to the above
"""
import traceback


class Question1:
    """Question 1 Class"""
    def arranging_list(self, input_list):
        """
        Function to Arrange List according to the times they repeat in the list
        :param input_list:
        :return result:
        """
        try:
            # Declaring flag & result
            flag = True
            result = []

            # Checking if the length of InputArray is 1 or not
            if len(input_list) == 1:
                result = input_list
                flag = False

            if flag:
                # Creating dicitonary to store frequencies
                unique_values_frequencies = {}

                # Finding Unique numbers in the list
                unique_values = list(set(input_list))

                # Iterating list and finding repetitions
                for number in unique_values:
                    unique_values_frequencies[number] = input_list.count(number)

                # Sorting the dictionary
                sorted_dictionary = sorted(unique_values_frequencies.items(),
                                           key=lambda x: x[1], reverse=True)

                for key, element in enumerate(sorted_dictionary):
                    frequency = element[1]
                    for count in range(0, frequency):
                        result.append(element[0])

            return result
        except:  # pylint: disable=bare-except
            print(traceback.print_exc())
            return "Error"


if __name__ == '__main__':
    inp_list = [1, 4, 5, 6, 6, 5, 3, 5, 1, 6, 4, 6]
    question = Question1()
    print("Input list - " + str(inp_list))
    print("Output list - " + str(question.arranging_list(inp_list)))
