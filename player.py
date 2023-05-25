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
            tempMins = int(self.minutes_played) + int(other_player.minutes_played)
            self.minutes_played = str(tempMins)
            self.goals += other_player.goals
            self.assits += other_player.assits
            self.shots_on_target += other_player.shots_on_target
            self.progressive_passing_distance += other_player.progressive_passing_distance
            self.shot_creation_actions += other_player.shot_creation_actions
            self.total_shots += other_player.total_shots
            self.cmp += other_player.cmp
            self.pass_att += other_player.pass_att
    def ready_to_push(self):
        list = [] 
        list.append(self.name)
        list.append(self.nation)
        list.append(self.position)
        list.append(self.squad)
        list.append(self.age)
        list.append(self.born)
        list.append(self.minutes_played)
        list.append(self.goals)
        list.append(self.assits)
        list.append(self.total_shots)
        list.append(self.shots_on_target)
        list.append(self.shot_creation_actions)
        list.append(self.cmp)
        list.append(self.pass_att)
        list.append(self.progressive_passing_distance)
        # will use num for the Beans rating
        num = 0
        list.append(num)
        return tuple(list)

        