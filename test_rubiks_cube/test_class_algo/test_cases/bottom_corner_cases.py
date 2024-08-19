import numpy as np

class TestBottomCorner:
    
    in_matrix=[]
    out_matrix=[]
    
    def __init__(self) -> None:
        self.bottom_corner_test_case()
        
    def bottom_corner_test_case(self):
        
        #1st testcase
        inp1=np.array([[[6, 5, 3], [2, 1, 6], [2, 1, 2]],
                        [[6, 2, 4], [3, 3, 2], [6, 4, 3]],
                        [[5, 3, 1], [6, 4, 3], [1, 1, 2]],
                        [[6, 1, 2], [4, 2, 4], [5, 4, 5]],
                        [[3, 1, 3], [2, 5, 5], [1, 3, 4]],
                        [[4, 5, 4], [5, 6, 6], [1, 6, 5]]]).reshape(6,3,3)
        
        out1=np.array([[[6, 5, 4], [2, 1, 1], [2, 1, 3]],
                        [[6, 3, 3], [3, 3, 2], [4, 4, 3]],
                        [[1, 2, 4], [6, 4, 3], [1, 1, 2]],
                        [[5, 1, 2], [4, 2, 4], [5, 4, 5]],
                        [[3, 5, 6], [2, 5, 6], [1, 3, 2]],
                        [[4, 5, 6], [5, 6, 6], [1, 6, 5]]]).reshape(6,3,3)
                        
        
        #2nd testcase ...
        inp2=np.array([[[5, 6, 2], [3, 1, 5], [3, 1, 3]],
                        [[4, 6, 3], [2, 3, 1], [5, 5, 6]],
                        [[1, 5, 1], [6, 4, 4], [3, 4, 5]],
                        [[2, 1, 2], [6, 2, 4], [1, 3, 5]],
                        [[6, 3, 6], [2, 5, 3], [4, 2, 6]],
                        [[1, 5, 4], [1, 6, 4], [2, 2, 4]]]).reshape(6,3,3)
        out2=np.array([[[5, 6, 4], [3, 1, 3], [3, 1, 2]],
                        [[5, 2, 6], [5, 3, 1], [6, 5, 6]],
                        [[1, 6, 3], [6, 4, 4], [3, 4, 5]],
                        [[1, 1, 2], [6, 2, 4], [1, 3, 5]],
                        [[6, 3, 2], [2, 5, 5], [4, 2, 3]],
                        [[1, 5, 4], [1, 6, 4], [2, 2, 4]]]).reshape(6,3,3)

        #3rd testcase ...
        inp3=np.array([[[1, 1, 1], [1, 1, 1], [1, 1, 1]],
                        [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
                        [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
                        [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
                        [[5, 5, 5], [5, 5, 5], [5, 5, 5]],
                        [[6, 6, 6], [6, 6, 6], [6, 6, 6]]]).reshape(6,3,3)
        out3=np.array([[[1, 1, 6], [1, 1, 5], [1, 1, 1]],
                        [[2, 2, 5], [4, 2, 2], [5, 2, 2]],
                        [[4, 2, 2], [4, 4, 4], [4, 4, 4]],
                        [[4, 3, 3], [3, 3, 3], [3, 3, 3]],
                        [[5, 5, 3], [5, 5, 1], [5, 5, 1]],
                        [[6, 6, 2], [6, 6, 6], [6, 6, 6]]]).reshape(6,3,3)
    
        self.in_matrix=[inp1,inp2,inp3]
        self.out_matrix=[out1,out2,out3]