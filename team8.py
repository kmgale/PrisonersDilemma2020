import random
###
# Each team's file must define four tokens:
# team_name: a string
# strategy_name: a string
# strategy_description: a string
# move: A function that returns 'c' or 'b'
####

team_name = 'Hairline Gang'
strategy_name = 'Mainly Betray, Sometimes Collude'
strategy_description = 'If they betrayed last or if they only colluded last, we betray no matter what'

def move(my_history, their_history, my_score, their_score):
  if len(my_history) == 0:
    return 'b'
  elif len(my_history) >= 1 and their_history[-1] == 'b':
    return 'b'
  else: 
    choice = ['b','c']
    return random.choice(choice)

