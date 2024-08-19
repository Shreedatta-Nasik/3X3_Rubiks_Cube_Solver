import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))
sys.path.append(src_path)
import numpy as np
import s6x
import full_t_cases

class TestMidLyr(s6x.FullT):
    
    def initialize(self,test_object,n) -> None:
        self.front_face=test_object.in_matrix[n][0]
        self.right_face=test_object.in_matrix[n][1]
        self.back_face=test_object.in_matrix[n][2]
        self.left_face=test_object.in_matrix[n][3]
        self.top_face=test_object.in_matrix[n][4]
        self.bottom_face=test_object.in_matrix[n][5]
        
    def print_face(self):
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')
        
        
    def matches(self,test_object,n):
        return ( (self.front_face==test_object.out_matrix[n][0]).all() and
        (self.right_face==test_object.out_matrix[n][1]).all() and
        (self.back_face==test_object.out_matrix[n][2]).all() and
        (self.left_face==test_object.out_matrix[n][3]).all() and
        (self.top_face==test_object.out_matrix[n][4]).all() and
        (self.bottom_face==test_object.out_matrix[n][5]).all())
        
    def test_full_t(self):
        test_object=full_t_cases.TestCaseFullT()
        failures=0
        for i,_ in enumerate(test_object.in_matrix):
            self.initialize(test_object,i)
            self.six_full_t()
            if(self.matches(test_object,i))==False:
                failures+=1
        assert failures==0