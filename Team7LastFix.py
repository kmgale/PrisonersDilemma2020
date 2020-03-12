import random 

team_name = 'Team7'
strategy_name=  'B or C because H'
strategy_description = 'the first round I am going to betray, and then in the other rounds depending on whether they betrayed or colluded in the prevoius round the code will have a higher chance to betray or collude that round.'


def move(my_history, their_history, my_score, their_score):
    mynumbB = 74
    mynumbC = 64
    p  = random.randint(1,100)
    if len(my_history) == 0:
      return 'b'

    elif len(my_history) == 50:
      if their_history.count('b') > their_history.count('c'):
        mynumbB += 5
      elif their_history.count('b') < their_history.count('c'):
        mynumbC += 5

    elif len(my_history) == 100: 
      if their_history.count('b') > their_history.count('c'):
        mynumbB += 8
      elif their_history.count('b') < their_history.count('c'):
        mynumbC += 8 

    elif len(my_history) >= 1 and their_history[-1] == 'b':
      if p <= mynumbB:
        return 'b'
      else:
        return 'c'
    elif len(my_history) >= 1 and their_history[-1] == 'c':
      if p <= mynumbC:
        return 'c'
      else:
        return 'b'
