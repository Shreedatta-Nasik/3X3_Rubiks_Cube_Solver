import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))
sys.path.append(src_path)
import three
import half_t_cases

class TestHalfT(three.Half_t):
    
    def initialize(self,test_object,n) -> None:
        self.front_face=test_object.in_matrix[n][0]
        self.right_face=test_object.in_matrix[n][1]
        self.back_face=test_object.in_matrix[n][2]
        self.left_face=test_object.in_matrix[n][3]
        self.top_face=test_object.in_matrix[n][4]
        self.bottom_face=test_object.in_matrix[n][5]
                
        
    def matches(self,test_object,n):
        return ( (self.front_face==test_object.out_matrix[n][0]).all() and
        (self.right_face==test_object.out_matrix[n][1]).all() and
        (self.back_face==test_object.out_matrix[n][2]).all() and
        (self.left_face==test_object.out_matrix[n][3]).all() and
        (self.top_face==test_object.out_matrix[n][4]).all() and
        (self.bottom_face==test_object.out_matrix[n][5]).all())
        
    def test_half_t(self):
        test_object=half_t_cases.TestCaseHalfT()
        failures=0
        for i,_ in enumerate(test_object.in_matrix):
            self.initialize(test_object,i)
            self.three_half_t()
            if(self.matches(test_object,i))==False:
                failures+=1
        assert failures==0