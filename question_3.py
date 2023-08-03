"""
Question 3
Input -
Expected output -

Time Complexity Achieved -
Time Complexity Reasoning -
"""

class Question3:
    """Class for question 3"""
    def barriers_broken_by_batman(self, input_data, input_barriers):
        """
        Function to find how many barriers batman can break
        :param input_data:
        :param input_barriers:
        :return barriers_crossed:
        """
        # Initializing and setting all provided information
        barriers = input_data[0]
        batman_height = input_data[1]
        batman_duck = input_data[2]
        batman_jump = input_data[3]
        grenades = input_data[4]

        success = 0

        # Iterating through the barriers
        for barrier in input_barriers:
            # Checking which type of barrier & respective breaking condition
            if barrier[0] == 1 and (batman_height - batman_duck) < barrier[1]:
                success += 1
            elif barrier[0] == 2 and batman_jump > barrier[1]:
                success += 1
            elif grenades != 0:
                success += 1
                grenades -= 1
            elif grenades == 0:
                break

        return success


if __name__ == '__main__':
    inp_list = [6, 5, 1, 2, 3]
    inp_barriers = [
        [2, 2],
        [2, 1],
        [1, 10],
        [2, 8],
        [2, 4],
        [1, 2]
    ]
    question = Question3()
    print("Output list - " + str(question.barriers_broken_by_batman(inp_list, inp_barriers)))
