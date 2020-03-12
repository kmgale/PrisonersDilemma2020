####
#     Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random 

team_name = 'tresamigos'
strategy_name=  'Amigos will stay amigos but three is a crowd.'
strategy_description = 'Collude on first turn. If they betray on last turn, collude, if they betray twice in a row, betray, if they collude on last turn, randomly choose.'
    


def move(my_history, their_history, my_score, their_score):
    try:
      if len(my_history) == 0:
        #return random.choice(choices)
        return 'c'
      # make sure that there's enough history
      elif len(my_history) >= 1 and their_history[-1] == 'b':
        if their_history[-2] == 'b':
          return 'b'
        elif their_history[-2] == 'c':
          return 'c'
      elif len(my_history) >= 1 and their_history[-1] == 'c':
        return random.choice(['c','b'])
      else:
        return random.choice(['c','b'])
    except: 
      return random.choice(['c','b'])
