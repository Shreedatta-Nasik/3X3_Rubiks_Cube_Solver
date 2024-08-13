
from test_rubiks_cube.test_class_algo.test_cases import bottom_corner_cases,right_middle_cases,left_middle_cases,top_middle_cases,top_corner_cases,top_layer_cases
from src import algorithms

class TestAlgo(algorithms.Algorithms):
    
    
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
        
    def test_bottom_corners(self):
        test_object=bottom_corner_cases.TestBottomCorner()
        failures=0
        for i,j in enumerate(test_object.in_matrix):
            self.initialize(test_object,i)
            self.bottom_corner()
            if (self.matches(test_object,i))==False:
                failures+=1
        assert failures==0
            
            
    def test_right_middle(self):
        test_object=right_middle_cases.TestRightMiddle()
        failures=0
        for i,j in enumerate(test_object.in_matrix):
            self.initialize(test_object,i)
            self.right_middle()
            if (self.matches(test_object,i))==False:
                failures+=1
        assert failures==0
            
    def test_left_middle(self):
        test_object=left_middle_cases.TestLeftMiddle()
        failures=0
        for i,j in enumerate(test_object.in_matrix):
            self.initialize(test_object,i)
            self.left_middle()
            if (self.matches(test_object,i))==False:
                failures+=1
        assert failures==0
            
    def test_top_middle(self):
        test_object=top_middle_cases.TestTopMiddle()
        failures=0
        for i,j in enumerate(test_object.in_matrix):
            self.initialize(test_object,i)
            self.top_middle()
            if (self.matches(test_object,i))==False:
                failures+=1
        assert failures==0
            
    def test_top_corners(self):
        test_object=top_corner_cases.TestTopCorner()
        failures=0
        for i,j in enumerate(test_object.in_matrix):
            self.initialize(test_object,i)
            self.top_corner()
            if (self.matches(test_object,i))==False:
                failures+=1
        assert failures==0
            
    def test_top_layer(self):
        test_object=top_layer_cases.TestTopLayer()
        failures=0
        for i,j in enumerate(test_object.in_matrix):
            self.initialize(test_object,i)
            self.top_layer()
            if (self.matches(test_object,i))==False:
                failures+=1
        assert failures==0