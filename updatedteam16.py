import random

team_name = 'kool cids :/'
strategy_name = 'last move and random'
strategy_description = 'If both of us betrayed in the last round, then we collude. If something else happened, 30% of the time we betry and 70% of the time we collude.'

def move(my_history, their_history, my_score, their_score, result='c'):
  if len(their_history)>=1:
    if my_history[-1] == 'b' and their_history[-1] == 'b':
      return 'c'
    else:
      if random.random()<0.3: #30% betray
        return 'b' 
      else:
        return 'c' 
  else:
    if random.random()<0.3: #30% betray
      return 'b' 
    else:
        return 'c' #but 70% of the time collude
