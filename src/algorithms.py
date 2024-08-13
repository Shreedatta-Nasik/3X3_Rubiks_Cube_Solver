import cube

class Algorithms(cube.Cube): 
    
    #half_t algorithm
    def bottom_corner(self) -> None:
        self.up_right(1)
        self.right(1)
        self.down_right(1)
        self.left(1)
        
    #middle_layer algorithm
    def right_middle(self) -> None:
        self.right(1)
        self.up_right(1)
        self.right(1)
        self.down_right(1)
        self.left(1)
        self.front_left(1)
        self.left(1)
        self.front_right(1)
        self.right(1) 
        
    def left_middle(self) -> None:
        self.left(1)
        self.up_left(1)
        self.left(1)
        self.down_left(1)
        self.right(1)
        self.front_right(1)
        self.right(1)
        self.front_left(1)
        self.left(1)
      
    #full_t algorithm  
    def top_middle(self) -> None:
        self.up_right(1)
        self.right(1)
        self.down_right(1)
        self.right(1)
        self.up_right(1)
        self.left(1)
        self.left(1)
        self.down_right(1)
        
    #penultimate algorithm       
    def top_corner(self) -> None:
        self.right(1)
        self.up_right(1)
        self.left(1)
        self.up_left(1)
        self.right(1)
        self.down_right(1)
        self.left(1)
        self.down_left(1)
        
    #all_yellow algorithm    
    def top_layer(self) -> None:
        self.front_right(1)
        self.up_left(1)
        self.front_left(1)
        self.down_left(1)