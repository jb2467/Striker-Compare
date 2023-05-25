class Algorithm:
    total_stats_values: float
    per90_stats_values: float
    playmaking_stats_values: float
    shooting_stats_values: float

    # Used to set the value stats across every player
    def __init__(self, total_stats_values , per90_stats_values, playmaking_stats_values ,shooting_stats_values):
        Algorithm.total_stats_values = total_stats_values
        Algorithm.per90_stats_values = per90_stats_values
        Algorithm.playmaking_stats_values = playmaking_stats_values
        Algorithm.shooting_stats_values = shooting_stats_values
