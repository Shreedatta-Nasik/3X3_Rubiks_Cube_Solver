import s6x

class Penultimate(s6x.FullT):
    
    count_penult=0
    
    def no_crnr_pcs(self) -> None:
        for _ in range(4):
            if((self.front_face[0][2]+self.right_face[0][0]+self.top_face[2][2])==(self.front_face[1][1]+self.right_face[1][1]+5)):
                self.count_penult+=1
            self.rotate_cube(0)
        return
                
    def seven_penultimate(self) -> None:
        for _ in range(5):
            self.no_crnr_pcs()
            if self.count_penult==4:
                return
            elif self.count_penult>0:
                while(((self.front_face[0][2]+self.right_face[0][0]+self.top_face[2][2])==(self.front_face[1][1]+self.right_face[1][1]+5))==0):
                    self.rotate_cube(1)
                while(((self.front_face[0][2]+self.right_face[0][0]+self.top_face[2][2]==self.front_face[1][1]+self.right_face[1][1]+5) and 
                       (self.front_face[0][0]+self.left_face[0][2]+self.top_face[2][0]==self.front_face[1][1]+self.left_face[1][1]+5) and 
                       (self.back_face[0][2]+self.left_face[0][0]+self.top_face[0][0]==self.back_face[1][1]+self.left_face[1][1]+5) and 
                       (self.back_face[0][0]+self.right_face[0][2]+self.top_face[0][2]==self.back_face[1][1]+self.right_face[1][1]+5))==0):
                    self.top_corner()
                return
            else:
                self.top_corner()