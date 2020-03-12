####
#     Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random

team_name = 'BRUH'
strategy_name = 'Vengeance'
strategy_description = 'if they '
    


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history) == 0:
      return 'c'
    elif their_history[-5] == 'b' :
      if random() < .5:
        return 'b'
      else:
        return 'c'
