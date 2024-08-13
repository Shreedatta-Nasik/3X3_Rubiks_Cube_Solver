import numpy as np

class TestCaseFrontRight:

    in_matrix = []
    out_matrix = []

    def __init__(self) -> None:
        self.front_right_test_cases()


    def front_right_test_cases(self):

        # 1st testcase
        in_t_1 = np.array([[[6, 5, 3], [2, 1, 6], [2, 1, 2]],
                           [[6, 2, 4], [3, 3, 2], [6, 4, 3]],
                           [[5, 3, 1], [6, 4, 3], [1, 1, 2]],
                           [[6, 1, 2], [4, 2, 4], [5, 4, 5]],
                           [[3, 1, 3], [2, 5, 5], [1, 3, 4]],
                           [[4, 5, 4], [5, 6, 6], [1, 6, 5]]]).reshape(6, 3, 3)

        out_t_1 = np.array([[[2, 2, 6], [1, 1, 5], [2, 6, 3]],
                            [[1, 2, 4], [3, 3, 2], [4, 4, 3]],
                            [[5, 3, 1], [6, 4, 3], [1, 1, 2]],
                            [[6, 1, 4], [4, 2, 5], [5, 4, 4]],
                            [[3, 1, 3], [2, 5, 5], [5, 4, 2]],
                            [[6, 3, 6], [5, 6, 6], [1, 6, 5]]]).reshape(6, 3, 3)

        # 2nd testcase ...
        in_t_2 = np.array([[[5, 6, 2], [3, 1, 5], [3, 1, 3]],
                           [[4, 6, 3], [2, 3, 1], [5, 5, 6]],
                           [[1, 5, 1], [6, 4, 4], [3, 4, 5]],
                           [[2, 1, 2], [6, 2, 4], [1, 3, 5]],
                           [[6, 3, 6], [2, 5, 3], [4, 2, 6]],
                           [[1, 5, 4], [1, 6, 4], [2, 2, 4]]]).reshape(6, 3, 3)
        out_t_2 = np.array([[[3, 3, 5], [1, 1, 6], [3, 5, 2]],
                            [[4, 6, 3], [2, 3, 1], [6, 5, 6]],
                            [[1, 5, 1], [6, 4, 4], [3, 4, 5]],
                            [[2, 1, 1], [6, 2, 5], [1, 3, 4]],
                            [[6, 3, 6], [2, 5, 3], [5, 4, 2]],
                            [[5, 2, 4], [1, 6, 4], [2, 2, 4]]]).reshape(6, 3, 3)

        # 3rd testcase ...
        in_t_3 = np.array([[[1, 1, 1], [1, 1, 1], [1, 1, 1]],
                           [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
                           [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
                           [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
                           [[5, 5, 5], [5, 5, 5], [5, 5, 5]],
                           [[6, 6, 6], [6, 6, 6], [6, 6, 6]],]).reshape(6, 3, 3)
        out_t_3 = np.array([[[1, 1, 1], [1, 1, 1], [1, 1, 1]],
                            [[5, 2, 2], [5, 2, 2], [5, 2, 2]],
                            [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
                            [[3, 3, 6], [3, 3, 6], [3, 3, 6]],
                            [[5, 5, 5], [5, 5, 5], [3, 3, 3]],
                            [[2, 2, 2], [6, 6, 6], [6, 6, 6]]]).reshape(6, 3, 3)

        self.in_matrix = [in_t_1, in_t_2, in_t_3]
        self.out_matrix = [out_t_1, out_t_2, out_t_3]

    
