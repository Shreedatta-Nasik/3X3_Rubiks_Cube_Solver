import half_t_3

class MiddleLayer(half_t_3.Half_t):
    
    count_mid_lyr=0
    
    def no_mid_pcs(self) -> int:
        r=0
        for j in range(4):
            if self.front_face[0][1]!=5 and self.top_face[2][1]!=5:
                    r=r+1
            self.rotate_cube(0)
        return r

    def pop_mid_pcs(self) -> None:
        if not (self.front_face[1][0]==self.front_face[1][1] and self.left_face[1][2]!=5):
            self.left_middle()
        if not (self.front_face[1][2]==self.front_face[1][1] and self.right_face[1][0]!=5):
            self.right_middle()
        return
    
    def four_middle_layer(self) -> None:
       for i in range(15):
           for j in range(8):
               if((self.front_face[1][0]+self.front_face[1][1]+self.front_face[1][2]==3*self.front_face[1][1])and 
                  self.left_face[1][2]==self.left_face[1][1] and 
                  self.right_face[1][0]==self.right_face[1][1]):
                   self.count_mid_lyr+=1
                   break
               r=self.no_mid_pcs()
               if r==0:
                   self.pop_mid_pcs()
               if(self.front_face[0][1]==self.front_face[1][1] and self.top_face[2][1]==self.right_face[1][1]):
                   self.right_middle()
                   continue
               if(self.front_face[0][1]==self.front_face[1][1] and self.top_face[2][1]==self.left_face[1][1]):
                   self.left_middle()
                   continue
               if self.count_mid_lyr==4:
                   return
               else:
                   self.right(1)
           self.rotate_cube(1)                