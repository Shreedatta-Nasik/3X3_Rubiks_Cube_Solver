import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rubiks_cube'))
sys.path.append(src_path)
import random
import numpy as np
import eight

class RubiksCube(eight.AllYellow):

    def process(self):
    
        sol=[]
        i=0
        while(i<(len(self.solution)-3)):
            if (self.solution[i]!=self.solution[i+1] or self.solution[i+1]!=self.solution[i+2] or self.solution[i+2]!=self.solution[i+3]):
                sol.append(self.solution[i])
                i+=1
            else:
                i+=4
        if (i==len(self.solution)-3):
            sol.append(self.solution[i])
            sol.append(self.solution[i+1])
            sol.append(self.solution[i+2])
        return sol
    
    #this Function solves the Rubik's cube
    def rubiks_cube(self):
        
        print("Scrambled Cube")
        self.print_face()
        self.one_daisy()
        print("One")
        self.print_face()
        self.two_white_cross()
        print("Two")
        self.print_face()
        self.three_half_t()
        print("Three")
        self.print_face()
        self.four_middle_layer()
        print("Four")
        self.print_face()
        self.five_yellow_cross()
        print("Five")
        self.print_face()
        self.six_full_t()
        print("Six")
        self.print_face()
        self.seven_penultimate()
        print("Seven")
        self.print_face()
        self.eight_all_yellow()
        print("Eight")
        self.print_face()
        while not (self.front_face[0][1]==self.front_face[1][1]):
            self.right()
        self.solution=self.process()
        return
    
    #this function scrambles the a solved cube by performing random cube movements for a certain steps
    #You can change it to any value. Default is set to 1000 mives
    def randomize(self):
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
            moves[m](0)
        return