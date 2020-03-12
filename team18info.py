import random 

team_name = 'Team LN'
strategy_name=  'In hindsight, two might hit a lot harder than one will.'
strategy_description = 'Collude on the first turn. If they betray two turns in a row, collude. If they collude two turns in a row, betray. Otherwise, random choice.'
    


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''


    if len(my_history) < 2:
      return 'c'
    elif len(my_history) >= 3 and their_history[-1] and their_history[-2] == 'b':
      return 'c'
    elif len(my_history) >= 3 and their_history[-1] and their_history[-2] == 'c':
      return 'b'   
    elif len(my_history) >= 2 and their_history[-1] == 'b':
      return 'b'
    elif len(my_history) >= 2 and their_history[-1] == 'c':
      return 'c'
    else:
      choices = ['c','b']
      return random.choice(choices)

