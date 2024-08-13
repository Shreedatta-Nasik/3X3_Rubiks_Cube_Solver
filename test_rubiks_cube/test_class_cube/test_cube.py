from src import cube
from test_rubiks_cube.test_class_cube.test_cases import down_right_cases,up_left_cases,up_right_cases,down_left_cases,left_cases,right_cases,front_right_cases,front_left_cases,rotate_cube_cases

class TestCube(cube.Cube):

    def initialize(self, test_object, n) -> None:
        self.front_face = test_object.in_matrix[n][0]
        self.right_face = test_object.in_matrix[n][1]
        self.back_face = test_object.in_matrix[n][2]
        self.left_face = test_object.in_matrix[n][3]
        self.top_face = test_object.in_matrix[n][4]
        self.bottom_face = test_object.in_matrix[n][5]

    
    def matches(self, test_object, n):
        return ((self.front_face == test_object.out_matrix[n][0]).all() and
                (self.right_face == test_object.out_matrix[n][1]).all() and
                (self.back_face == test_object.out_matrix[n][2]).all() and
                (self.left_face == test_object.out_matrix[n][3]).all() and
                (self.top_face == test_object.out_matrix[n][4]).all() and
                (self.bottom_face == test_object.out_matrix[n][5]).all())
        

    def test_up_right(self):
        t_obj1=up_right_cases.TestCaseUpRight()
        failures = 0
        for i, j in enumerate(t_obj1.in_matrix):
            self.initialize( t_obj1,i)
            self.up_right(0)
            if (self.matches(t_obj1, i)) == False:
                failures += 1
        assert failures == 0
        
    def test_down_right(self):
        t_obj2=down_right_cases.TestCaseDownRight()
        failures = 0
        for i, j in enumerate(t_obj2.in_matrix):
            self.initialize( t_obj2,i)
            self.down_right(0)
            if (self.matches(t_obj2, i)) == False:
                failures += 1
        assert failures == 0
        
    def test_up_left(self):
        t_obj3=up_left_cases.TestCaseUpLeft()
        failures = 0
        for i, j in enumerate(t_obj3.in_matrix):
            self.initialize( t_obj3,i)
            self.up_left(0)
            if (self.matches(t_obj3, i)) == False:
                failures += 1
        assert failures == 0
        
    def test_down_left(self):
        t_obj4=down_left_cases.TestCaseDownLeft()
        failures = 0
        for i, j in enumerate(t_obj4.in_matrix):
            self.initialize(t_obj4,i)
            self.down_left(0)
            if (self.matches(t_obj4, i)) == False:
                failures += 1
        assert failures == 0
        
    def test_left(self):
        t_obj5=left_cases.TestCaseLeft()
        failures = 0
        for i, j in enumerate(t_obj5.in_matrix):
            self.initialize(t_obj5,i)
            self.left(0)
            if (self.matches(t_obj5, i)) == False:
                failures += 1
        assert failures == 0
        
    def test_right(self):
        t_obj1=right_cases.TestCaseRight()
        failures = 0
        for i, j in enumerate(t_obj1.in_matrix):
            self.initialize( t_obj1,i)
            self.right(0)
            if (self.matches(t_obj1, i)) == False:
                failures += 1
        assert failures == 0
        
    def test_front_right(self):
        t_obj1=front_right_cases.TestCaseFrontRight()
        failures = 0
        for i, j in enumerate(t_obj1.in_matrix):
            self.initialize( t_obj1,i)
            self.front_right(0)
            if (self.matches(t_obj1, i)) == False:
                failures += 1
        assert failures == 0
    
    def test_front_left(self):
        t_obj1=front_left_cases.TestCaseFrontLeft()
        failures = 0
        for i, j in enumerate(t_obj1.in_matrix):
            self.initialize( t_obj1,i)
            self.front_left(0)
            if (self.matches(t_obj1, i)) == False:
                failures += 1
        assert failures == 0
        
    def test_rotate_cube(self):
        t_obj1=rotate_cube_cases.TestCaseRotateCube()
        failures = 0
        for i, j in enumerate(t_obj1.in_matrix):
            self.initialize( t_obj1,i)
            self.rotate_cube(0)
            if (self.matches(t_obj1, i)) == False:
                failures += 1
        assert failures == 0
    