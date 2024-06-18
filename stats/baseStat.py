class BaseStat():
    
    def __init__(self, name, statMax):
        self.name = name
        self.statPoints = statMax
        self.statMax = statMax
        
    # return True if alive
    #   Fasle if dead
    def reduce_points(self, points):
        self.statPoints -= points
        if self.statPoints <= 0:
            return True
        return False
    
    def add_points(self, points):
        self.statPoints += points
        if self.statPoints > self.statMax:
            self.statPoints = self.statMax
            return True
        return False
    
    def print_stat(self):
        print(self.name + ': ' + str(self.statPoints))
    
    def get_stat_name(self):
        return self.name
    
    def get_stat_points(self):
        return self.statPoints
    
    def get_stat_max(self):
        return self.statMax