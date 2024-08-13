import middle_layer_4

class YellowCross(middle_layer_4.MiddleLayer):
    
    def five_yellow_cross(self) -> None:
        
        for i in range(2):
            if(self.top_face[0][1]+self.top_face[1][0]+self.top_face[1][1]+self.top_face[1][2]+self.top_face[2][1]==25):
                return
            elif (self.top_face[1][0]+self.top_face[1][1]+self.top_face[1][2]==15):
                self.front_right(1)
                self.bottom_corner()
                self.front_left(1)
                return
            elif(self.top_face[0][1]+self.top_face[1][1]+self.top_face[2][1]==15):
                self.right(1)
                continue
            elif ((self.top_face[0][1]+self.top_face[1][0]+self.top_face[1][1]==15) or 
                  (self.top_face[1][0]+self.top_face[1][1]+self.top_face[2][0]==15) or 
                  (self.top_face[0][1]+self.top_face[1][1]+self.top_face[1][2]==15) or 
                  (self.top_face[2][1]+self.top_face[1][1]+self.top_face[1][2]==15)):
                while ((self.top_face[0][1]+self.top_face[1][0]+self.top_face[1][1]==15)==0):
                    self.right(1)
                self.front_right(1)
                self.bottom_corner()
                self.bottom_corner()
                self.front_left(1)
            else:
                while ((self.top_face[1][0]+self.top_face[1][1]+self.top_face[2][0]==15 or
                       self.top_face[0][1]+self.top_face[1][1]+self.top_face[1][2]==15 or 
                       self.top_face[2][1]+self.top_face[1][1]+self.top_face[1][2]==15 or
                       self.top_face[0][1]+self.top_face[1][0]+self.top_face[1][1]==15 or 
                       self.top_face[1][0]+self.top_face[1][1]+self.top_face[1][2]==15 or
                       self.top_face[0][1]+self.top_face[1][1]+self.top_face[2][1]==15)==0):
                    self.front_right(1)
                    self.bottom_corner()
                    self.front_left(1)
                continue