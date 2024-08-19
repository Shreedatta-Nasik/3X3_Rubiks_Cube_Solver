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
        print(self.solution)
        print("1")
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')
        self.two_white_cross()
        print(self.solution)
        print("2")
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')       
        self.three_half_t()
        print(self.solution) 
        print("3")
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')
        self.four_middle_layer()
        print(self.solution) 
        print("4")
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')
        self.five_yellow_cross()
        print(self.solution) 
        print("5")
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')
        self.six_full_t()
        print(self.solution) 
        print("6")
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')
        self.seven_penultimate()
        print(self.solution) 
        print("7")
        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')
        self.eight_all_yellow()
        print(self.solution) 
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
        print('1')
        self.top_face = np.array([[5]*3]*3)
        self.front_face = np.array([[1]*3]*3)
        self.back_face = np.array([[4]*3]*3)
        self.left_face = np.array([[2]*3]*3)
        self.bottom_face = np.array([[6]*3]*3)
        self.right_face = np.array([[3]*3]*3)
        moves={1:self.up_left,
            2:self.up_right,
            3:self.down_left,
            4:self.down_right,
            5:self.right,
            6:self.left,
            7:self.front_right,
            8:self.front_left,
            9:self.rotate_cube}
        for i in range(1000):
            m=random.randint(1,9)
            moves[m](1)
        self.solution.append('govinda')
        return