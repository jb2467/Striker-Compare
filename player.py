class Player:
    name: str
    nation: str
    position: str
    squad : str
    age: str
    born: int
    minutes_played: int
    goals: int
    assits: int
    total_shots:int
    shots_on_target: int 
    cmp:int
    pass_att:int
    shot_creation_actions: int
    progressive_passing_distance: int
    beans:float
    SCA90: float
    shots_on_target_percent: float
    goals_per_90: float
    assits_per_90: float
    cmp_percent: float

    
    #goals,assits, shots_on_target, shot_creation_actions, progressive_passing_distance, SCA90, shots_on_target_percent, goals_per_90, assits_per_90, cmp_percent)
    def __init__(self, updated_stats):
        updated = tuple(updated_stats)
        self.name = updated_stats[0]
        self.nation = updated_stats[1]
        self.position = updated_stats[2]
        self.squad = updated_stats[3]
        self.age = updated_stats[4]
        self.born = updated_stats[5]
        self.minutes_played = updated_stats[6]
        self.goals = updated_stats[7]
        self.assits = updated_stats[8]
        self.shots_on_target = updated_stats[9]
        self.progressive_passing_distance = updated_stats[10]
        self.shot_creation_actions = updated[11]
        self.SCA90 = updated[12]
        self.shots_on_target_percent = updated[13]
        self.goals_per_90 = updated[14]
        self.assits_per_90 = updated[15]
        self.cmp_percent = updated[16]
        self.beans = 0
        




    def __init__(self, list):
        tup = tuple(list)
        self.name = tup[0]
        self.nation = tup[1]
        self.position = tup[2]
        self.squad = tup[3]
        self.age = tup[4]
        self.born = tup[5]
        # Needs to get rid of the comma to allow minutes played to be used later
        # Needs to use the list since I will be chaning the value the list holds
        if',' in list[6]:
            temp = list[6].split(',')
            num = ''
            for element in temp:
                num += element
            list[6] = num
        self.minutes_played = int(list[6])
        self.goals = int(tup[7])
        self.assits = int(tup[8])
        self.total_shots = int(tup[9])
        self.shots_on_target = int(tup[10])
        self.shot_creation_actions = int(tup[11])
        self.cmp = int(tup[12])
        self.pass_att = int(tup[13])
        self.progressive_passing_distance = int(tup[14])
        self.beans = 0
    # To compare the players
    def equals(self, other_player):
        if isinstance(other_player, Player):
            if other_player.name == self.name and other_player.age == self.age:
                return True
        return False
    def add_new_stats(self, other_player):
        if isinstance(other_player, Player):
            # Make sure all of the positions they played on are included
            num = other_player.position.count(',')
            if num < 1  and other_player.position not in self.position:
                self.position = self.position + ', ' + other_player.position
            if num >=1:
                temp = other_player.position.split(',') 
                for i in range(0,num):
                    if temp[i] not in self.position:
                        self.position = self.position + ', ' + temp[i]
            # All of the teams they played for 
            if other_player.squad not in self.squad:
                self.squad = self.squad + ', ' + other_player.squad
            # all of the new stats from the other team(s) they played for
            self.minutes_played = int(self.minutes_played) + int(other_player.minutes_played)
            self.goals += other_player.goals
            self.assits += other_player.assits
            self.shots_on_target += other_player.shots_on_target
            self.progressive_passing_distance += other_player.progressive_passing_distance
            self.shot_creation_actions += other_player.shot_creation_actions
            self.total_shots += other_player.total_shots
            self.cmp += other_player.cmp
            self.pass_att += other_player.pass_att
    '''
    Used to give the stats I want to use for the algorithm
    '''
    def recalculate(self):
        updated_stats = []
        updated_stats.append(self.name)
        updated_stats.append(self.nation)
        updated_stats.append(self.position)
        updated_stats.append(self.squad)
        updated_stats.append(self.age)
        updated_stats.append(self.born)
        updated_stats.append(self.minutes_played)
        updated_stats.append(self.goals)
        updated_stats.append(self.assits)
        updated_stats.append(self.shots_on_target)
        updated_stats.append(self.shot_creation_actions)
        updated_stats.append(self.progressive_passing_distance)
        updated_stats.append(((self.shot_creation_actions)/self.minutes_played)*90)
        if self.total_shots  == 0: 
            updated_stats.append(0)
        else:
            updated_stats.append((self.shots_on_target)/self.total_shots)
        updated_stats.append(((self.goals)/self.minutes_played ) * 90 )
        updated_stats.append(self.assits/self.minutes_played*90)
        if self.pass_att == 0:
            updated_stats.append(0)
        else:
            updated_stats.append(self.cmp/self.pass_att)
        # Will be the rating 
        updated_stats.append(0)
        return tuple(updated_stats)



        