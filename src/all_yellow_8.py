import penultimate_7

class AllYellow(penultimate_7.Penultimate):
    
    count_yellow=0
    def eight_all_yellow(self) -> None:
        for i in range(5):
           if self.count_yellow==4:
               return
           for i in range(4):
               if (self.top_face[2][0]!=5):
                   while(self.top_face[2][0]!=5):
                       self.top_layer()
                   self.count_yellow+1
               self.right(1)
           else:
               self.count_yellow+=1
               self.rotate_cube(1)