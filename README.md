#  3X3 Rubik's cube solver
This is a python package which solves the scrabled 3X3 rubik's cube using [daisy chain method](https://www.ipassio.com/blog/how-to-solve-rubiks-cube?srsltid=AfmBOorD3J2wNmD-HqpxjutP0jiKfP2pF17ylBd04CntT-9CUOZW4Idt)
Which is one pf the most popular and easy methods of solving the said cube. There are mainly 8 phases is solving the cube. Think of it as a 7 patterns that need to appear on the cube for solving. In my package the cube is
represented by a 6X3X3 numpy array where the top face and the bottom faces are fixed and they are yellow and white respectively. For the movements of the cube I have defined 9 movements. There are some other functions
like randomize, print_face etc. This package has been tested using pytest. you can find the test cases and the test method [here](https://github.com/Shreedatta-Nasik/Rubiks_cube/tree/master/test_rubiks_cube)
to execute these tests and testcases install pytest and execute the command pytest in the terminal.

## The 7 patterns
  1. Daisy
     ![image](https://github.com/user-attachments/assets/7ee283ee-892e-4007-82e9-2287977b0a20)
  2. White Cross
     ![image](https://github.com/user-attachments/assets/8018a46d-6e48-40bd-b695-44ae1014da12)
  3. Half TY
     ![image](https://github.com/user-attachments/assets/1a7dade5-7999-4874-baea-7357d7aa1eab)
  4. Middle
     ![image](https://github.com/user-attachments/assets/7d5078be-c8f9-4226-82b0-2eab0e6511d0)
  5. Full T
     ![image](https://github.com/user-attachments/assets/33e0b05e-7c86-4e15-a4c1-1b235d8db24b)
  6. Penultimate
     ![image](https://github.com/user-attachments/assets/d732c1b7-6996-43fa-8f9f-05d274bcf4d9)
  7. Complete
     ![image](https://github.com/user-attachments/assets/3e9b244e-f526-4117-a05d-b1d11de7d9e3)


## Cube Movements
  1. Up right [UR]
    ![image](https://github.com/user-attachments/assets/fff3f929-0b47-4532-9fbb-2b0566ccd011)
  2. Down right [UR']
     ![image](https://github.com/user-attachments/assets/c3a48cd3-b580-4a3f-bb88-d41888fb7d4f)
  3. Up left [UL]
     ![image](https://github.com/user-attachments/assets/da126661-e54f-4609-8973-938511257747)
  4. Down left [UL']
     ![image](https://github.com/user-attachments/assets/151d4616-369d-4962-b2dd-0bb1606adc9e)
  5. Left[ L]
     ![image](https://github.com/user-attachments/assets/46a9eb0f-e1f4-4a22-9c29-a71f3bc1153b)
  6. Right [R]
     ![image](https://github.com/user-attachments/assets/afedf707-6ba0-442d-a32a-35b10d3b1459)
  7. Front right [F]
      ![image](https://github.com/user-attachments/assets/55270127-1422-4c31-8701-b35e6357bd1b)
  8. Front left [F']
      ![image](https://github.com/user-attachments/assets/495dc726-12ba-4ed4-b5a4-887b86307822)
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

      from rubiks_cube import rubiks_cube
      cube=rubiks_cube.RubiksCube()
      cube.input_cube()
      cube.rubiks_cube()
      print(cube.solution)

 ### 2. Randomize the Scramble and solve:

      from rubiks_cube import rubiks_cube
      cube=rubiks_cube.RubiksCube()
      cube.randomize()
      cube.rubiks_cube()
      print(cube.solution)


  

