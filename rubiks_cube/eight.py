import seven

class AllYellow(seven.Penultimate):
    
    count_yellow=0
    def eight_all_yellow(self) -> None:
        for _ in range(4):
            if self.count_yellow==4:
                break
            elif self.top_face[2][0]==5:
                self.count_yellow+=1
                self.rotate_cube(1)
            else:
                break
        for _ in range(4):
            if self.count_yellow==4:
                break
            else:
                while(self.top_face[2][0]!=5):
                    self.top_layer()
                self.count_yellow+1
                self.right(1)
        while(self.front_face[0][0]!=self.front_face[1][1]):
            self.right(1)
        return