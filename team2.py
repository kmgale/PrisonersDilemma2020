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
      choices = ['c','b']
      return random.choice(choices)
    else:
      choices = ['c','b']
      return random.choice(choices)


    '''if my_history[-1] == 'b' and their_history[-1] == 'c':
      my_score += 100
      their_score -= 500
    elif their_history[-1] == 'b' and my_history[-1] == 'c':
      my_score -= 500
      their_score += 100
    elif my_history[-1] == their_history[-1]:
      if my_history[-1] == 'b':
        my_score -= 250
        their_score -= 250
      elif my_history[-1] == 'c':
        my_score += 0
        their_score += 0'''

def move2(my_history, their_history, my_score, their_score):
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
    if len(my_history) == 0:
      return 'c'
    # make sure that there's enough history
    elif len(my_history) >= 1 and their_history[-1] == 'b':
      return 'b'
    else:
      choices = ['c','b']
      return random.choice(choices)


      
      

    


    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Collude on the first move
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='c'):
         print 'Turn 1 test passed'
     # Test 2: if they betrayed last time, i should betray this time
    if test_move(my_history='bcbc',
              their_history='cccb', 
              # Note the scores are for testing move()
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='c'):       
      print 'vengeance test successful.'
