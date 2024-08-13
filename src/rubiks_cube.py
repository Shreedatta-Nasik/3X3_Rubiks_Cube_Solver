import random
import numpy as np
import all_yellow_8

class RubiksCube(all_yellow_8.AllYellow):
    
    def rubiks_cube(self):\
        
        print("0")
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')
        self.one_daisy()
        print("1")
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')
        self.two_white_cross()
        print("2")
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')        
        self.three_half_t()
        print("3")
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')
        self.four_middle_layer()
        print("4")
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')
        self.five_yellow_cross()
        print("5")
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')
        self.six_full_t()
        print("6")
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')
        self.seven_penultimate()
        print("7")
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')
        self.eight_all_yellow()
        print("8")
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')
        while not (self.front_face[0][1]==self.front_face[1][1]):
            self.right()
        return
    
    def randomize(self):
        self.top_face = np.array([[5]*3]*3)
        self.front_face = np.array([[1]*3]*3)
        self.back_face = np.array([[4]*3]*3)
        self.left_face = np.array([[2]*3]*3)
        self.bottom_face = np.array([[6]*3]*3)
        self.right_face = np.array([[3]*3]*3)
        moves={1:self.up_left(0),
            2:self.up_right(0),
            3:self.down_left(0),
            4:self.down_right(0),
            5:self.right(0),
            6:self.left(0),
            7:self.front_right(0),
            8:self.front_left(0),
            9:self.rotate_cube(0)}
        for i in range(50):
            m=random.randint(1,9)
            moves.get(m)
        return