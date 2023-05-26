from pytimedinput import timedInput
import git
import schedule
import time
import scrapper
from algorithm import Algorithm
repo = git.Repo('/Users/josephbean/Personal Projects/WebScraper/Striker Compare')    
def default_values():
    return 50,50,50,50    
def auto_commit():
    repo.index.add(['Forward_Stats.db'])
    print('Files Added Successfully')
    repo.index.commit('Game happened! ')
    print('Commited successfully')
    origin.push()
    print('Pushed changes to origin')
    schedule.every().monday.at("17:15").do(main)
    schedule.every().tuesday.at("17:15").do(main)
    schedule.every().wednesday.at("17:15").do(main)
    schedule.every().thursday.at("17:15").do(main)
    schedule.every().friday.at("17:15").do(main)
    schedule.every().saturday.at("13:45").do(main)
    schedule.every().monday.at("13:45").do(main)
    
# Do some changes and commit

origin = repo.remote(name='origin')
  
existing_branch = repo.heads['main']
existing_branch.checkout()

'''
This function will get the user functions of the desired values for the algorithm
If the enter an incorrect input, it does to default values, but if all enter values
are valid, will be used in the algorithm
'''
def get_user_values(user):
    user_total_stats_values, timedOut1 = timedInput("Enter total stats value ")
    if (timedOut1):
        a, b, c, d = default_values()
        
    else:
        if user_total_stats_values.isdigit() and (0 <= int(user_total_stats_values) <= 100) :
            user_playmaking_stats_value, timedOut2 = timedInput("Enter playmaking stats value ")
            if(timedOut2):
                a, b, c, d = default_values()
            else:
                if user_playmaking_stats_value.isdigit() and ( 0 <= int(user_playmaking_stats_value) <= 100) :
                    a = int (user_total_stats_values)
                    b = 100 - a
                    c = int(user_playmaking_stats_value)
                    d = 100 - c
                else:
                    a, b, c, d = default_values()
                    print('Not a number or not in range. Will use default values (50%)')
        else:
            print('Not a number or not in range. Will use default values (50%)')
            a, b, c, d = default_values()
    if not user:
        auto_commit()
    return a, b, c, d


def main(user):
    total_stats_values , per90_stats_values, playmaking_stats_values ,shooting_stats_values = get_user_values(user)
    scrapper.scrap_stats(total_stats_values , per90_stats_values, playmaking_stats_values ,shooting_stats_values)
    


if __name__ == '__main__':
    temp, timedOut = timedInput("Are you a user? ")
    while True:
        #if you didn't time out (There was an answer), then go through the program yourself
        #else, assume it an automted task doer that is runnning the programmed
        if(not timedOut):
            print(not timedOut)
            main(not timedOut)
            break;
        schedule.run_pending()
        time.sleep(100)
    