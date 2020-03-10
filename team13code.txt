team_name = 'Team 13'
strategy_name = 'Business'
strategy_description = 'Collude until betrayed, betray 2x in a row in return, have a mounting chance to betray randomly'

def move(my_history, their_history, my_score, their_score):
  import random
  randbetray=0
  for i in my_history:
    randbetray+=1
  if len(their_history) >= 2:
    if 'b' in their_history[-2]:
     return 'b'
  elif random.randint(0,100) <= randbetray:
    return 'b'
  else:
    return 'c'
