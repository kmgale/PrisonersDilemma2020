####
#     Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random

team_name = 'Team4'
strategy_name = 'Vengeance'
strategy_description = 'if they betrayed in the last 5 turns theres a 50% cance of betraying else collude.  '
    


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history) < 5:
      return 'c'
    elif their_history[-5] == 'b' and their_history[-4] == 'b' and their_history[-3] == 'b' and their_history[-2] == 'b' and their_history[-1] == 'b' :
      if random.randint() < .6:
            return 'b'
      else:
            return 'c'
    else:
        return 'c'
