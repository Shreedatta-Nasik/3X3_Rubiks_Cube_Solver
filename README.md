#  3X3 Rubik's cube solver
This is a python package which solves the scrabled 3X3 rubik's cube using [daisy chain method](https://www.ipassio.com/blog/how-to-solve-rubiks-cube?srsltid=AfmBOorD3J2wNmD-HqpxjutP0jiKfP2pF17ylBd04CntT-9CUOZW4Idt)
Which is one pf the most popular and easy methods of solving the said cube. There are mainly 8 phases is solving the cube. Think of it as a 7 patterns that need to appear on the cube for solving. In my package the cube is
represented by a 6X3X3 numpy array where the top face and the bottom faces are fixed and they are yellow and white respectively. For the movements of the cube I have defined 9 movements. There are some other functions
like randomize, print_face etc. This package has been tested using pytest. you can find the test cases and the test method [here](https://github.com/Shreedatta-Nasik/Rubiks_cube/tree/master/test_rubiks_cube)
to execute these tests and testcases install pytest and execute the command pytest in the terminal.

## The 7 patterns
  1. Daisy
     ![1.Daisy](https://github.com/user-attachments/assets/8fb87cd8-1871-4c07-a37d-252f3f12804b)
  2. White Cross
     ![image](https://github.com/user-attachments/assets/05673e41-cc1a-4a0a-a2fc-d7200735b072)
  3. Half TY
     ![image](https://github.com/user-attachments/assets/d362a9f0-30c3-4b1b-8abe-1620de8bf94e)
  4. Middle
     ![image](https://github.com/user-attachments/assets/48981d7c-9ddd-45d0-a4ef-4daf4f006880)
  5. Full T
     ![image](https://github.com/user-attachments/assets/168a66d5-3f5b-4518-9c6a-be4d6a164ed4)
  6. Penultimate
     ![image](https://github.com/user-attachments/assets/adf25297-dfc7-4f56-bd44-d78f1932f754)
  7. Complete
     ![image](https://github.com/user-attachments/assets/48e9b775-beda-4d5b-aad4-152caaae37f4)

## Cube Movements
  1. Up right [UR]
     ![image](https://github.com/user-attachments/assets/039834d5-c5b3-4882-b210-02d13702b5e7)
  2. Down right [UR']
     ![image](https://github.com/user-attachments/assets/ae9775c2-ed3c-4da6-a69c-99f359cb2ebd)
  3. Up left [UL]
     ![image](https://github.com/user-attachments/assets/276336b7-5e0b-43b3-ac75-02ee4c1633b8)
  4. Down left [UL']
     ![image](https://github.com/user-attachments/assets/c0338ebd-4e05-4102-8fa5-352d5c228d39)
  5. Left[ L]
     ![image](https://github.com/user-attachments/assets/f6eaf2ee-0c73-4ab0-9ba8-393ba2cb6a23)
  6. Right [R]
     ![image](https://github.com/user-attachments/assets/8ce8aaa9-5c07-4a54-b6a4-561f6fdf15c9)
  7. Front right [F]
      ![image](https://github.com/user-attachments/assets/59820671-1466-44a1-a180-b9af3c62a4cf)
  8. Front left [F']
      ![image](https://github.com/user-attachments/assets/cbbf13d2-acb5-413a-8e00-6864b2b5d85b)
  9. Rotate cube [ROR]:
      Here the front face which was facing is rotated left. so for the above example if the front face was White the after this movement the front face would be Blue

## Main Funtions

 1. ### RubiksCube():
    Creates the class for the for the execution of the operations of the Rubik's Cube.  
 
 2. ### input_face():
    This function is used to input the the scrambled cube. The user has to input 6 3x3 Matrices for the respective faces in the form R for Red, B for Blue, G for Green, O for Orange, Y for Yellow, W for
    White.
    for example: r r g r r r w y r for a single face
    the above function is not case sensitive
 
 3. ### rubiks_cube():
    This function solves the scrambled cube and prints the result at each phase of the pattern of the cube.
 4. ### solution:
    This attribute contains the steps that are required to solve the cube. 
 5. ### randomize():
    This function scrambles the cube. It return a scrambled 6X3X3 cube

## Sample Code

 ### 1. Input the scrambled cube and solve:

      from rubiks_cube import RubiksCube
      cube=RubiksCube()
      cube.input_cube()
      cube.rubiks_cube()
      print(cube.solution)

 ### 2. Randomize the Scramble and solve:

      from rubiks_cube import RubiksCube
      cube=RubiksCube()
      cube.randomize()
      cube.rubiks_cube()
      print(cube.solution)


  

