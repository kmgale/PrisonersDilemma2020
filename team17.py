team_name = 'Team 16'
strategy_name = 'friendly is just the tip of the iceberg :)'
strategy_description = 'Betray if other team betray. Collude if other team colludes.'

def move(my_history, their_history, my_score, their_score):
  import random
  b=0
  c=0
  if 'b' in their_history:
    b+=1
  if 'c' in their_history:
    c+=1
  if int(b)>=int(c):
    return 'b'
  if int(c)<int(b):
    return 'c'
