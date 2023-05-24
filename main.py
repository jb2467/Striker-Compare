import scrapper
from pytimedinput import timedInput

def default_values():
    return 50,50,50,50

def get_user_values():
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
                    print('Not a number or not in range')

        else:
            print('Not a number or not in range')
            a, b, c, d = default_values()
    return a, b, c, d

    
def main():
    total_stats_values , per90_stats_values, playmaking_stats_values ,shooting_stats_values = get_user_values()
    scrapper.scrap_stats(total_stats_values , per90_stats_values, playmaking_stats_values ,shooting_stats_values)
    
if __name__ == '__main__':
    main()
    