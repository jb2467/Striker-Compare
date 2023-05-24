# Striker-Compare

This is a program that uses a Python bot to scrape premier league stats from _Football Reference_ and ranks all of the forwards in the Premier League based on a rating (_Beans_). It will update the ratings after every game and be added, commited and pushed to git.

## Disclaimers
The users running the program will be able to select how much they value the total, per90/%, playmaking, and shooting stats. However, if the user fails to enter these numbers in 5 seconds it will default to 50% for all of these. This is because the program must be run after every game. This program has a schedule to follow and will run at a certain time (after every game), since this is automatic and won't enter any numbers for the values it will need a default. (50%)

# Calculating the algorithm (_Beans_)
These stats will be used to make an algorithm based on these stats:
  Total goals
  Total Assists
  Total Shots on target
  Total progressive passing distance
  Total shot creation actions
  Shot on target %
  Shot creation actions per 90 minutes
  Goals per 90 minutes
  Assits per 90 minutes
  Pass completions per 90 minutes
These total Per 90/% will be broken into two categories (Playmaking and Shooting)
  Planking:
    Total Assists
    Total progressive passing distance
    Total shot creation actions
    Shot creation actions per 90 minutes
    Assits per 90 minutes
    Pass completions per 90 minutes
  Shooting: 
    Total goals
    Total Shots on target
    Total shot creation actions
    Shot on target %
    Shot creation actions per 90 minutes
    Goals per 90 minutes
  Shot creation actions (total and per 90) will count as both playmaking and shooting. This is because this stat takes into the playmaking leading up to the shot as well as the shot

The algorithm will allow the user to control how much the algorithm values:
Total stats, Per 90/% stats (add to 1), and Playmaking stats, Scoring stats (add to 1)

## MATH of algorithm
Let: 
s = How much you value scoring as a fraction (out of 100)
p = How much you value playmaking as a fraction (out of 100)
s+p=1

t = How much you value the total stats as a fraction (out of 100)
n = how much you value the per 90s/% stats as a fraction (out of 100)
t + n
For total:
Let: 
a = ast
b = shot creation (playmaking)
c = progressive passing distance 

d = goals
e = shots on target
f = shot creation (scoring)

Each shooting variable will be the same value as each other (a = b = c)
Each playmaking variable will be the same value as each other (d = e = f)

a + b + c + d + e + f = t or n (depending if we're calculating the total stats or per90/% stats)
### For total stats
a + b + c = t * p
d + e + f = t * s
3a = t * p
3d = t * s
a = (t * p)/3
d = (t * s)/3

'a' represents the max a total playmaking stat can be worth of the player's overall _Beans_ rating. 
'd' represents the max a total shooting stat can be worth of the player's overall _Beans_ rating. 

### For per90/% stats
a + b + c = n * p
d + e + f = n * s
3a = n * p
3d = n * s
a = (n * p)/3
d = (n * s)/3

'a' represents the max a Per90/% playmaking stat can be worth of the player's overall _Beans_ rating. 
'd' represents the max a Per90/% shooting stat can be worth of the player's overall _Beans_ rating. 

The league's leader in a stat earns the value of 'a' or 'b'
The league's second leader in a stat will earn the value of ('a' or 'b') *  ((Total number of forwards -1)/Total Number of forwards)
The league's third leader in a stat will earn the value of ('a' or 'b')*  ((Total number of forwards -2)/Total Number of forwards)
etc.
#### If multiple players have the same amount of goals they will earn the same amount of _Beans_ rating
So if Legues has 4 players and player 1 has 20 assists, player 2 has 15 assists, player 3 has 15 assists, player 4 has 2 assists
Player 1 earns 'a' or 'b'  amount for that stat
Player 2 earns ('a' or 'b') *  ((4 -1)/4) = ('a' or 'b') * 3/4
Player 3 earns ('a' or 'b') *  ((4 -1)/4) = ('a' or 'b') * 3/4
Player 4 earns ('a' or 'b') *  ((4 - 3)/4) = ('a' or 'b') * 1/4 
(this will be 1/4 because player 4 is technically the 4th highest goal scorer. Goes 1st, 2nd, 2nd, 4th)

#### If a Player is on multiple squads in one season
If this is the case, the player's total stats will be added and the per90 and % stats will be added and recalculated based off the minutes, total attempts and completed attempts
