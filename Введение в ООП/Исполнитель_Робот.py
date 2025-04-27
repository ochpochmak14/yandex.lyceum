class Robot: 
    def __init__(self, position): 
        self.coord_x, self.coord_y = position
        self.start_pos = position
        self.route = [position] 
        
    def move(self, commands): 
        self.route = [self.start_pos]  
        for command in commands: 
            if command == 'N' and self.coord_y < 100: 
                self.coord_y += 1 
            elif command == 'S' and self.coord_y > 0: 
                self.coord_y -= 1 
            elif command == 'E' and self.coord_x < 100: 
                self.coord_x += 1 
            elif command == 'W' and self.coord_x > 0: 
                self.coord_x -= 1 
            self.route.append((self.coord_x, self.coord_y))  
        self.start_pos = (self.coord_x, self.coord_y)  
        return self.coord_x, self.coord_y
    
    def path(self): 
        return self.route
