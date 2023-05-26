class Algorithm:
    total_stats_values: float
    per90_stats_values: float
    playmaking_stats_values: float
    shooting_stats_values: float
    diction: dict

    # Used to set the value stats across every player
    def __init__(self, total_stats_values , per90_stats_values, playmaking_stats_values ,shooting_stats_values):
        Algorithm.total_stats_values = total_stats_values/100
        Algorithm.per90_stats_values = per90_stats_values/100
        Algorithm.playmaking_stats_values = playmaking_stats_values/100
        Algorithm.shooting_stats_values = shooting_stats_values/100
        Algorithm.diction = {}
        

    def make_dictionary(self, players:list):
        for element in players:
            self.diction[element[0]] = 0
        
    def calculate(self, players:list, index, total, playmaking):
        sum = 0;
        last_rating = 0
        rank = 0
        num_of_same = 0
        last_stat = 0
        t = self.total_stats_values 
        p = self.playmaking_stats_values
        if  not total:
            t = self.per90_stats_values
        if not playmaking:
            p = self.shooting_stats_values
        r1 = (t * p) /3
        num_of_forwads = len(players)
        new_list = sorted(players, key=lambda x: x[index], reverse=True) #sorted based off total goals

        for element in new_list:
            if element[index] == last_stat:
                #firs tplater does not match this
                num_of_same+=1
                sum = self.diction[element[0]]
                sum += last_rating
                self.diction[element[0]] = sum
            else:
                rank = rank + num_of_same
                last_rating = r1 * ((num_of_forwads - rank)/ num_of_forwads)
                num_of_same = 1
                sum = self.diction[element[0]]
                sum += last_rating
                self.diction[element[0]] = sum
                last_stat = element[index]
        return self.diction