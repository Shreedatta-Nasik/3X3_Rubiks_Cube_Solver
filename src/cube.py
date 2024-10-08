import numpy as np

#this class defines the basic movements of the cube.
class Cube:

    # color code for the cube
    cube_code = {"R": 1, "B": 2, "G": 3, "O": 4, "Y": 5, "W": 6}

    front_face = []
    right_face = []
    back_face = []
    left_face = []
    top_face = []
    bottom_face = []

    solution = []
    #while calling the functions the 1,0 is used for whether the called funtion is incuded in the solution list or not
    #up_right(0) means that i am performing up_right but do not add this to the solution list
    #uo_right(1) means the opposite

    def input_cube(self):
        
        self.front_face = self.input_face('Front Face')
        self.right_face = self.input_face('Right Face')
        self.back_face = self.input_face('Back Face')
        self.left_face = self.input_face('Left Face')
        self.top_face = self.input_face('Top Face')
        self.bottom_face = self.input_face('Bottom Face')

    def input_face(self,face_name) -> np.array:

        face = list(map(str.upper, input(
            f"Enter the {face_name} matrix of the faces").split()))
        for i, j in enumerate(face):
            face[i] = self.cube_code.get(j)
        return np.array(face).reshape(3, 3)

    #the right part of the cube goes up
    def up_right(self,n) -> None:

        temp = np.array(self.front_face)[:, 2]
        self.front_face[:, 2] = self.bottom_face[:, 2]
        self.bottom_face[:, 2] = self.back_face[:, 0][::-1]
        self.back_face[:, 0] = self.top_face[:, 2][::-1]
        self.top_face[:, 2] = temp
        self.right_face = np.rot90(m=self.right_face,k=-1,axes=(0,1))
        if n==1:
            self.solution.append("UR")

    #the right part of the cube goes down
    def down_right(self,n) -> None:

        self.up_right(0)
        self.up_right(0)
        self.up_right(0)
        if n==1:
            self.solution.append("UR'")

    #the left part of the cube goes up
    def up_left(self,n) -> None:

        temp = np.array(self.front_face)[:, 0]
        self.front_face[:, 0] = self.bottom_face[:, 0]
        self.bottom_face[:, 0] = self.back_face[:, 2][::-1]
        self.back_face[:, 2] = self.top_face[:, 0][::-1]
        self.top_face[:, 0] = temp
        self.left_face = np.rot90(m=self.left_face,k=1,axes=(0,1))
        if n==1:
            self.solution.append("UL")
    
    #the left part of the cube goes down
    def down_left(self,n) -> None:

        self.up_left(0)
        self.up_left(0)
        self.up_left(0)
        if n==1:
            self.solution.append("UL'")

    #the front row  part of the cube moves anti-clockwise
    def left(self,n) -> None:

        temp = np.array(self.front_face)[0]
        self.front_face[0] = self.left_face[0]
        self.left_face[0] = self.back_face[0]
        self.back_face[0] = self.right_face[0]
        self.right_face[0] = temp
        self.top_face = np.rot90(m=self.top_face,k=1,axes=(0,1))
        if n==1:
            self.solution.append("L")
    
    #the front row  part of the cube moves anti-clockwise
    def right(self,n) -> None:

        temp = np.array(self.front_face)[0]
        self.front_face[0] = self.right_face[0]
        self.right_face[0] = self.back_face[0]
        self.back_face[0] = self.left_face[0]
        self.left_face[0] = temp
        self.top_face = np.rot90(m=self.top_face,k=-1,axes=(0,1))
        if n==1:
            self.solution.append("R")

    #the front face is rotated clockwise
    def front_right(self,n) -> None:

        temp = np.array(self.left_face)[:, 2]
        self.left_face[:, 2] = self.bottom_face[0]
        self.bottom_face[0] = self.right_face[:, 0][::-1]
        self.right_face[:, 0] = self.top_face[2]
        self.top_face[2] = temp[::-1]
        self.front_face = np.rot90(m=self.front_face,k=-1,axes=(0,1))
        if n==1:
            self.solution.append("F")

    #the front face is rotated anit-clockwise
    def front_left(self,n) -> None:

        temp = np.array(self.bottom_face)[0]
        self.bottom_face[0] = self.left_face[:, 2]
        self.left_face[:, 2] = self.top_face[2][::-1]
        self.top_face[2] = self.right_face[:, 0]
        self.right_face[:, 0] = temp[::-1]
        self.front_face = np.rot90(m=self.front_face,k=1,axes=(0,1))
        if n==1:
            self.solution.append("F'")

    #the whole cube is rotated clockwise
    def rotate_cube(self,n) -> None:

        temp = np.array(self.front_face)
        self.front_face = self.right_face
        self.right_face = self.back_face
        self.back_face = self.left_face
        self.left_face = temp
        self.top_face = np.rot90(m=self.top_face,k=-1,axes=(0,1))
        self.bottom_face = np.rot90(self.bottom_face,1,axes=(0,1))
        if n==1:
            self.solution.append("ROR")
    
    #function for printing the cube
    def print_face(self) -> None:

        print(f'{np.array(self.front_face).tolist()},')
        print(f'{np.array(self.right_face).tolist()},')
        print(f'{np.array(self.back_face).tolist()},')
        print(f'{np.array(self.left_face).tolist()},')
        print(f'{np.array(self.top_face).tolist()},')
        print(f'{np.array(self.bottom_face).tolist()}')
