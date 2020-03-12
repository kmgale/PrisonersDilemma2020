team_name = 'EEE-UR'
strategy_name = 'You only get one chance...'
strategy_description = 'If they have betrayed ANYONE EVER, betray them.'

def move(my_history, their_history, my_score, their_score):
  if len(my_history) == 0:
    return 'c'
  elif len(my_history) >= 1 and 'b' in their_history:
    return 'b'
  else:
    return 'c'
