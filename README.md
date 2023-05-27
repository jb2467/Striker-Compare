# Striker-Compare

This is a program that uses a Python bot to scrape premier league stats from _Football Reference_ and ranks all of the forwards in the Premier League based on a rating (_Beans_). It will update the ratings after every game and be added, commited and pushed to git.

## Disclaimers
The users running the program will be able to select how much they value the total, per90/%, playmaking, and shooting stats. However, if the user fails to enter these numbers in 5 seconds it will default to 50% for all of these. This is because the program must be run after every game. This program has a schedule to follow and will run at a certain time (after every game), since this is automatic and won't enter any numbers for the values it will need a default. (50%)

# Calculating the algorithm (_Beans_)
These stats will be used to make an algorithm based on these stats:
  - Total goals
  - Total Assists
  - Total Shots on target
  - Total progressive passing distance
  - Total shot creation actions
  - Shot on target %
  - Shot creation actions per 90 minutes
  - Goals per 90 minutes
  - Assits per 90 minutes
  - Pass completions per 90 minutes

The algorithm will allow the user to control how much the algorithm values:
  - Total stats, Per 90/% stats (add to 1)
  - Playmaking stats, shooting stats (add to 1)


