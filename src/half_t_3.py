import white_cross_2

class Half_t(white_cross_2.White_cross):
    
    count_half_t=0
    
    def bottom_corner_condition(self) -> None:
        for j in range(4):
            if((
                ((self.right_face[0][0]==self.front_face[1][1]) and (self.top_face[2][2]==6) and (self.front_face[0][2]==self.right_face[1][1])) or 
                ((self.top_face[2][2]==self.front_face[1][1]) and (self.front_face[0][2]==6) and (self.right_face[0][0]==self.right_face[1][1])) or 
                ((self.front_face[0][2]==self.front_face[1][1]) and (self.right_face[0][0]==6) and (self.top_face[2][2]==self.right_face[1][1])))==1):
                while (((self.front_face[2][2]==self.front_face[1][1]) and (self.bottom_face[0][2]==6) and (self.right_face[2][0]==self.right_face[1][1]))==0):
                    self.bottom_corner()
                self.count_half_t+=1
                return
            elif(((self.front_face[2][2]==6) or (self.bottom_face[0][2]==6) or (self.right_face[2][0]==6))):
                self.bottom_corner()
            self.right(1)


    def three_half_t(self) -> None:
        for i in range(8):
            if((((self.front_face[2][2]==self.front_face[1][1]) and 
                 (self.bottom_face[0][2]==6) and 
                 (self.right_face[2][0]==self.right_face[1][1]))==0)):
                self.bottom_corner_condition()
            if self.count_half_t==4:
                return
            self.rotate_cube(1) 