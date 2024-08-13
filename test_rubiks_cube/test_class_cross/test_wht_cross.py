from src import white_cross_2
from test_rubiks_cube.test_class_cross import wht_cross_cases

class TestWhtCross(white_cross_2.White_cross):
    
    
    def initialize(self,test_object,n) -> None:
        self.front_face=test_object.in_matrix[n][0]
        self.right_face=test_object.in_matrix[n][1]
        self.back_face=test_object.in_matrix[n][2]
        self.left_face=test_object.in_matrix[n][3]
        self.top_face=test_object.in_matrix[n][4]
        self.bottom_face=test_object.in_matrix[n][5]
        
    def print_face(self):
        print(self.front_face)
        print(self.right_face)
        print(self.back_face)
        print(self.left_face)
        print(self.top_face)
        print(self.bottom_face)
        
        
    def matches(self,test_object,n):
        return ( (self.front_face==test_object.out_matrix[n][0]).all() and
        (self.right_face==test_object.out_matrix[n][1]).all() and
        (self.back_face==test_object.out_matrix[n][2]).all() and
        (self.left_face==test_object.out_matrix[n][3]).all() and
        (self.top_face==test_object.out_matrix[n][4]).all() and
        (self.bottom_face==test_object.out_matrix[n][5]).all())
        
    def test_wht_cross(self):
        test_object=wht_cross_cases.TestCaseWhtCross()
        failures=0
        for i,j in enumerate(test_object.in_matrix):
            self.initialize(test_object,i)
            self.one_daisy()
            self.two_white_cross()
            if(self.matches(test_object,i))==False:
                failures+=1
        assert failures==0
        