# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# PART I
# Dutch goal scorers
goal_scorer_0 = 'Ruud Gullit'
goal_scorer_1 = 'Marco Van Basten'

# Netherlands scored twice againts URSS. This was the exact time that happened!
goal_0 = 32
goal_1 = 54


# Convert inter to strings
goal_first = str(goal_0)
goal_snd = str(goal_1)

# Goals report
scorers = goal_scorer_0 + ' ' + goal_first + \
    ',' + ' ' + goal_scorer_1 + ' ' + goal_snd
print(scorers)
# Report
report = f'{goal_scorer_0} scored in the {goal_first}nd minute n\ {goal_scorer_1} scored in the {goal_snd}nd minute'

print(report)

# PART II

player = 'Gut von Examplestein'  # Name of the goal scorer

first_name = player[:3]  # First name
print(first_name)

last_name_len = len(player[9:])  # Last name lenght
print(last_name_len)

name_short = f'{player[0]}. {player[4:]}'
print(name_short)

chant = f'{first_name}!\t' * 3
print(chant)

chant_length = len(chant)
print(chant_length)

print(chant[14] != '')
