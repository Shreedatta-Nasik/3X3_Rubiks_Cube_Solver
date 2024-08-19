import algorithms as al

# a step which is focused on gettin a daisy pattern on top of cube
class Daisy(al.Algorithms):
    
    count_daisy=0
    
    def white(self,i,j) -> None:
        if i==0 and j ==1:
            while(self.top_face[2][1]==6):
                self.right(1)
        else:    
            while(self.top_face[i][j]==6):
                self.right(1)
        if i==0:
            self.front_right(1)
            self.left(1)
        if i==2:
            print(1)
            self.front_left(1)
            self.left(1)
        if j==0:
            self.up_left(1)
        else:
            self.up_right(1)
        
    def bottom_white(self,j) -> None:
        if j==0:
            while(self.top_face[1][0]==6):
                self.right(1)
            self.up_left(1)
            self.up_left(1)
        else:
            while(self.top_face[1][2]==6):
                self.right(1)
            self.up_right(1)
            self.up_right(1)
            
                        
    def one_daisy(self) -> None:
        for i in range(12):
            if self.front_face[0][1]==6:
                self.white(0,1)
                self.count_daisy+=1
                continue
            if self.front_face[1][0]==6:
                self.white(1,0)
                self.count_daisy+=1
                continue
            if self.front_face[1][2]==6:
                self.white(1,2)
                self.count_daisy+=1
                continue
            if self.front_face[2][1]==6:
                self.white(2,1)
                self.count_daisy+=1
                continue
            if self.count_daisy==4:
                return 
            elif i==11:
                self.bottom_face_condition()
            else:
                self.rotate_cube(1)        
        
    def bottom_face_condition(self) -> None:
        for i in range(2):
            if self.count_daisy==4:
                return 
            if self.bottom_face[0][1]==6:
                self.rotate_cube(1)
                self.bottom_white(0)
                self.count_daisy+=1
            if self.bottom_face[1][0]==6:
                self.bottom_white(0)
                self.count_daisy+=1
            if self.bottom_face[1][2]==6:
                self.bottom_white(2)
                self.count_daisy+=1
            if self.bottom_face[2][1]==6:
                self.rotate_cube(1)
                self.bottom_white(2)
                self.count_daisy+=1