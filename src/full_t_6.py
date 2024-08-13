import yellow_cross_5

class FullT(yellow_cross_5.YellowCross):
    
    def six_full_t(self) -> None:
        for i in range(4):
            while(self.front_face[0][1]!=self.front_face[1][1]):
                self.right(1)
            if(self.front_face[0][1]==self.front_face[1][1] and 
               self.right_face[0][1]==self.right_face[1][1] and 
               self.left_face[0][1]==self.left_face[1][1] and 
               self.back_face[0][1]==self.back_face[1][1]):
                return 
            elif(self.front_face[0][1]==self.front_face[1][1] and 
                self.right_face[0][1]!=self.right_face[1][1] and 
                self.left_face[0][1]!=self.left_face[1][1] and 
                self.back_face[0][1]!=self.back_face[1][1]):
                while ((self.front_face[0][1]==self.front_face[1][1] and 
                           self.right_face[0][1]==self.right_face[1][1] and 
                           self.left_face[0][1]==self.left_face[1][1] and 
                           self.back_face[0][1]==self.back_face[1][1])==0):
                    self.top_middle()
                return
            else:
                self.rotate_cube(1)
        
        for i in range(4):
            self.top_middle()
            for i in range(4):
                if(self.front_face[0][1]==self.front_face[1][1] and 
                self.right_face[0][1]!=self.right_face[1][1] and 
                self.left_face[0][1]!=self.left_face[1][1] and 
                self.back_face[0][1]!=self.back_face[1][1]):
                    while ((self.front_face[0][1]==self.front_face[1][1] and 
                            self.right_face[0][1]==self.right_face[1][1] and 
                            self.left_face[0][1]==self.left_face[1][1] and 
                            self.back_face[0][1]==self.back_face[1][1])==0):
                        self.top_middle()
                    return
                else:
                    self.right(1)
            self.rotate_cube(1)