from stats.baseStat import BaseStat
class BaseStatHandler():
    def __init__(self, statsList):
        self.stats = []
        for stat in statsList:
            self.stats.append(BaseStat(stat[0], stat[1]))

    def print_stats(self):
        print('Stats -')
        for i in range(len(self.stats)):
            self.stats[i].print_stat()
            
    def add_stat(self, name, statValue):
        newStat = BaseStat(name, statValue)
        self.stats.append(newStat)
        return True