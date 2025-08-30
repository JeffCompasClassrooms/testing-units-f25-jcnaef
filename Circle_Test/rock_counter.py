
class Rock_Counter:
    def __init__(self):
        self.rockCount = 0
        self.rockColorCount = {}

    def rock_found(self,color):
        self.rockCount += 1
        if color in self.rockColorCount:
            self.rockColorCount[color] += 1
        else:
            self.rockColorCount[color] = 1
    
    def mul_rocks_found(self,lColors):
        for color in lColors:
            self.rock_found(color)

    def get_num_rocks(self):
        return self.rockCount
#    
    def rock_lost(self,color):
        if color in self.rockColorCount:
            if self.rockColorCount[color] > 0:
                self.rockCount -= 1
                self.rockColorCount[color] -= 1
                if self.rockColorCount[color] == 0:
                    self.rockColorCount.pop(color)
            else:
                raise Exception("You didn't have a rock of this color to lose")

        else:
            raise Exception("You didn't have a rock of this color to lose")

    def mul_rocks_lost(self,lColors):
        for color in lColors:
            self.rock_lost(color)

    def get_num_color_rocks(self,color):
        return self.rockColorCount[color]
    
    def get_rock_color_count(self):
        return self.rockColorCount
    
    def get_total_num_rock_colors(self):
        return len(self.rockColorCount.keys())

    def has_rock_of_color(self,color):
        if color in self.rockColorCount:
            return True
        else:
            return False
    
    def lost_all_rocks(self):
        self.rockCount = 0
        self.rockColorCount = {}

    def lost_all_color_rocks(self,color):
        if color in self.rockColorCount:
            nLostRocks = self.rockColorCount[color]
            self.rockCount -= nLostRocks
            self.rockColorCount.pop(color)
        else:
            raise Exception("You didn't have a rock of this color to lose")
