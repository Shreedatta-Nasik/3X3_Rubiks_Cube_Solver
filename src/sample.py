import rubiks_cube
import numpy as np
q = rubiks_cube.RubiksCube()
in_t_1 = np.array([[[5, 2, 3], [1, 1, 5], [4, 1, 3]],
                        [[4, 6, 2], [3, 3, 2], [6, 1, 3]],
                        [[4, 3, 6], [1, 4, 4], [4, 6, 5]],
                        [[1, 6, 1], [5, 2, 3], [3, 2, 2]],
                        [[2, 4, 6], [3, 5, 2], [2, 4, 5]],
                        [[5, 6, 1], [5, 6, 5], [1, 4, 6]]]).reshape(6, 3, 3)

[[5, 3, 2], [3, 3, 3], [3, 3, 3]],
[[1, 4, 5], [4, 4, 4], [4, 4, 4]],
[[1, 2, 3], [2, 2, 2], [2, 2, 2]],
[[4, 1, 2], [1, 1, 1], [1, 1, 1]],
[[5, 5, 3], [5, 5, 5], [4, 5, 5]],
[[6, 6, 6], [6, 6, 6], [6, 6, 6]]

q.front_face = in_t_1[0]
q.right_face = in_t_1[1]
q.back_face = in_t_1[2]
q.left_face = in_t_1[3]
q.top_face = in_t_1[4]
q.bottom_face = in_t_1[5]
q.rubiks_cube()
print(f'{np.array(q.front_face).tolist()},')
print(f'{np.array(q.right_face).tolist()},')
print(f'{np.array(q.back_face).tolist()},')
print(f'{np.array(q.left_face).tolist()},')
print(f'{np.array(q.top_face).tolist()},')
print(f'{np.array(q.bottom_face).tolist()}')
print(q.solution)