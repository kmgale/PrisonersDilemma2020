team_name = 'EEE-UR'
strategy_name = 'Our milkshakes brings all the Bodens to the yard'
strategy_description = 'Kermit the frog will turn into emperor palpatine'

def move(my_history, their_history, my_score, their_score):
  if len(my_history) == 0:
    return 'c'
  elif len(my_history) >= 1 and 'b' in their_history:
    return 'b'
  else:
    return 'c'
