import daisy_1

# a step focused on getting a white cross pattern on the white face of the cube

class White_cross(daisy_1.Daisy):
            
    def two_white_cross(self) -> None:
        for i in range(4):
            while((self.front_face[0][1]==self.front_face[1][1] 
                   and self.top_face[2][1]==6)==0):
                self.right(1)
            self.front_right(1)
            self.front_right(1)
            self.rotate_cube(1)
        return 
    
    