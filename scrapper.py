import requests
from bs4 import BeautifulSoup, Comment
import sqlite3

def scrap_stats(total_stats_values , per90_stats_values, playmaking_stats_values ,shooting_stats_values):
    con = sqlite3.connect('Forward_Stats.db')
    cur = con.cursor()

    # Make the table with only these slots
    cur.execute('''CREATE TABLE IF NOT EXISTS stats(Player text PRIMARY KEY,Nation text,Pos text, Squads text,Age text,
    Born text, Mins Integer, Gls Integer, Ast Integer,  total_shots Integer, SoT Integer,  SCA Integer, pass_completions Integer, 
    pass_attempts Integer, PPD Integer,Beans real)''')

    # Header row
    cur.execute('''INSERT OR IGNORE INTO stats VALUES ('Name','Nation','Pos','Squad(s)','Age','Born','Min(s)',
    'Gls','Ast','Sh (Total shots)', 'SoT (Shots on target)', 'SCA (Shot creation actions)',
    'CMP (Pass completions)', 'PATT (Pass attempts)', 'PPD (Progressive passing distance)', 'Beans' )''')

    con.commit()

    # Gets all the links needed for the stats I want to use
    standard_soup = BeautifulSoup(requests.get('https://fbref.com/en/comps/9/stats/Premier-League-Stats').content, 'html.parser')
    goals_soup_URL = BeautifulSoup(requests.get('https://fbref.com/en/comps/9/gca/Premier-League-Stats').content, 'html.parser')
    passing_soup_URL = BeautifulSoup(requests.get('https://fbref.com/en/comps/9/passing/Premier-League-Stats').content, 'html.parser')
    shooting_soup_URL = BeautifulSoup(requests.get('https://fbref.com/en/comps/9/shooting/Premier-League-Stats').content, 'html.parser')

    # Gets all the stats from the links, even the ones I don't want
    Player_stats = BeautifulSoup(
        standard_soup.select_one('#all_stats_standard').find_next(text=lambda x: isinstance(x, Comment)), 'html.parser') # type: ignore
    goalStats = BeautifulSoup(
        goals_soup_URL.select_one('#all_stats_gca').find_next(text=lambda x: isinstance(x, Comment)), 'html.parser')  # type: ignore
    passingStats = BeautifulSoup(
        passing_soup_URL.select_one('#all_stats_passing').find_next(text=lambda x: isinstance(x, Comment)), 'html.parser') #type: ignore
    shootingStats = BeautifulSoup(
        shooting_soup_URL.select_one('#all_stats_shooting').find_next(text=lambda x: isinstance(x, Comment)), 'html.parser') #type: ignore



    # Total number of forwards
    num_of_forwards = 0
    # The whole player (Forwards only) data base stats
    Players = []
    '''
    this gets Name, Nation, position, Squad, Age, birth year, minutes, goals, assits, total shots, 
    shots on target, shot creation actions, progressive passing distance, pass completions, and pass attempts and
    '''
    for standard,shooting,goal,passing in zip (Player_stats.select('tr:has(td)'), shootingStats.select('tr:has(td)'),  goalStats.select('tr:has(td)'),passingStats.select('tr:has(td)')  ):
        standard_tds = [td.get_text(strip=True) for td in standard.select('td')]
        shooting_tds= [td.get_text(strip=True) for td in shooting.select('td')]
        goal_tds= [td.get_text(strip=True) for td in goal.select('td')]
        passing_tds= [td.get_text(strip=True) for td in passing.select('td')]
        # Each players' individual stats
        tempvar_stats = []
        if ( 'FW' in standard_tds[2]):
            num_of_forwards += 1    
            for i in range(0,6):
                tempvar_stats.append(standard_tds[i]) # Name, Nation, position, Squad, Age, birth year
            tempvar_stats.append(standard_tds[8]) # Minutes
            tempvar_stats.append(standard_tds[10]) # Goals
            tempvar_stats.append(standard_tds[11]) # Assits
            tempvar_stats.append(shooting_tds[8]) # Total shots
            tempvar_stats.append(shooting_tds[9]) # Shots on traget
            tempvar_stats.append(goal_tds[7]) # Shot creation actions
            tempvar_stats.append(passing_tds[7]) # Completed passes
            tempvar_stats.append(passing_tds[8] ) #  Pass attempts
            tempvar_stats.append(passing_tds[11]) # Progressive passing distance
            tempvar_stats.append(0) # My rating (Beans)
            Players.append(tuple(tempvar_stats))
    cur.executemany("INSERT OR REPLACE INTO stats VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    Players)
    con.commit()
    con.close()