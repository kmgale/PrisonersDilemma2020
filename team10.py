####
#     Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random 

team_name = 'Team10'
strategy_name=  'If I am going down, you are coming with me.'
strategy_description = 'Our strategy is to betray if we are being betrayed but if we are not being betrayed, we will collude.'
    


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty.
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].

    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.

    # collude on the first move:
    choices = random.choice('cb')
    if len(my_history) <= 1 and len(their_history) <= 1:
      return choices
    if len(my_history) >= 1 and their_history[-1] == 'b':
      return 'b'
    else:
      return 'c'
