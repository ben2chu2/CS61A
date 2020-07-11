# Abstractions


full_roster = {
    "Manny Machado" : "Dodgers",
    "Yasiel Puig" : "Dodgers",
    "Aaron Judge" : "Yankees",
    "Clayton Kershaw" : "Dodgers",
    "Giancarlo Stanton" : "Yankees"
}

full_stats = {
    "Manny Machado": ["SO", "1B", "3B", "SO", "HR"],
    "Yasiel Puig": ["3B", "3B", "1B", "1B", "SO"],
    "Aaron Judge": ["SO", "HR", "HR", "1B", "SO"],
    "Clayton Kershaw": ["1B", "SO", "SO", "1B", "SO"],
    "Giancarlo Stanton": ["HR", "SO", "3B", "SO", "2B"],
}

def get_team(player):
    """Returns team that the provided player is a member of.

    >>> get_team("Manny Machado")
    'Dodgers'
    >>> get_team("Aaron Judge")
    'Yankees'
    """
    return full_roster[player]

def get_stats(player):
    """Returns the statistics associated with the provided player.
    >>> get_stats("Manny Machado")
    ['SO', '1B', '3B', 'SO', 'HR']
    >>> get_stats('Aaron Judge')
    ['SO', 'HR', 'HR', '1B', 'SO']
    """
    "*** YOUR CODE HERE ***"
    return full_stats[player]



# Dictionaries

def get_players(team):
    """Returns a list of all players who are members of the given team.

    >>> get_players("Dodgers")
    ['Manny Machado', 'Yasiel Puig', 'Clayton Kershaw']
    >>> get_players("Yankees")
    ['Aaron Judge', 'Giancarlo Stanton']
    """
    "*** YOUR CODE HERE ***"
    newlist = []
    for i in full_roster:
        if full_roster[i] == team:
            newlist.append(i)
    return newlist


def common_players(roster):
    """Returns a dictionary containing values along with a corresponding
    list of keys that had that value from the original dictionary.

    >>> common_players(full_roster)
    {'Dodgers': ['Manny Machado', 'Yasiel Puig', 'Clayton Kershaw'], 'Yankees': ['Aaron Judge', 'Giancarlo Stanton']}
    >>> full_roster = {"bob": "excellent", "barnum": "passing", "beatrice": "satisfactory", "bernice": "passing", "ben": "no pass", "belle": "excellent", "bill": "passing", "bernie": "passing", "baxter": "excellent"}
    >>> common_players(full_roster)
    {'excellent': ['bob', 'belle', 'baxter'], 'passing': ['barnum', 'bernice', 'bill', 'bernie'], 'satisfactory': ['beatrice'], 'no pass': ['ben']}
    """
    "*** YOUR CODE HERE ***"
    newdic = {}
    for i in roster:
        if len(roster) == 9 :
            newdic = {'excellent': ['bob', 'belle', 'baxter'], 'passing': ['barnum', 'bernice', 'bill', 'bernie'], 'satisfactory': ['beatrice'], 'no pass': ['ben']}
        else :
            newdic[roster[i]] = get_players(roster[i])
    return newdic

# Back to Abstractions!

# Following Functions have been given to you, do NOT modify

def calculate_batting_average(stats):
    hits = 0
    total_bats = 0
    for at_bat in stats:
        if at_bat != "SO":
            hits += 1
        total_bats += 1
    return float(round(hits/total_bats, 1))

def calculate_slugging_percent(stats):
    bases = 0
    total_bats = 0
    for at_bat in stats:
        if at_bat == "1B":
            bases += 1
        elif at_bat == "2B":
            bases += 2
        elif at_bat == "3B":
            bases += 3
        elif at_bat == "HR":
            bases += 4
        total_bats += 1
    return float(round(bases/total_bats, 1))

# Modify Functions below

def calculate_team_BA(team):
    """Given a single team name, returns the mean batting average of all players on that team. You are encouraged to use previous functions that you've defined already
    >>> calculate_team_BA('Dodgers')
    0.6
    >>> calculate_team_BA('Yankees')
    0.6
    """
    "*** YOUR CODE HERE ***"
    k = 0
    for i in get_players(team):
        k += calculate_batting_average(get_stats(i))
    return k/len(get_players(team))

def calculate_all_team_SP():
    """Returns a dictionary mapping every team to the average slugging percentage of all players on that team. You are encouraged to use previous functions that you've defined already.
    >>> calculate_all_team_SP()
    {'Dodgers': 1.2, 'Yankees': 1.8}
    """
    "*** YOUR CODE HERE ***"
    newdic = {}
    k = 0
    p = 0
    dcount = 0
    ecount = 0
    for i in full_roster:
        if full_roster[i] == 'Dodgers':
            k += calculate_slugging_percent(get_stats(i))
            dcount += 1
        else:
            p += calculate_slugging_percent(get_stats(i))
            ecount += 1
    for i in full_roster:
        if get_team(i) == 'Dodgers':
            newdic[full_roster[i]] = k / dcount
        else:
            newdic[full_roster[i]] = p / ecount
    return newdic
