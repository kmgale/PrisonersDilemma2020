import random 

team_name = 'Team7'
strategy_name=  'B or C because H'
strategy_description = 'the first round I am going to betray, and then in the other rounds depending on whether they betrayed or colluded in the prevoius round the code will have a higher chance to betray or collude that round.'

IncreaseChanceB = False
IncreaseChanceC = False
GreaterIncreaseB = False
GreaterInceaseC = False

def move(my_history, their_history, my_score, their_score):
    global IncreaseChanceB,IncreaseChanceC,GreaterIncreaseB,GreaterInceaseC
    p = random.randint(1, 100)

    if len(my_history) == 0:
      return 'b'

    elif len(my_history) == 50:
      if their_history.count('b') > their_history.count('c'):
        IncreaseChanceB = True
      elif their_history.count('b') < their_history.count('c'):
        IncreaseChanceC = True

    elif len(my_history) == 100:
      if their_history.count('b') > their_history.count('c'):
        GreaterIncreaseB = True
      elif their_history.count('b') < their_history.count('c'):
        GreaterIncreaseC = True

    elif len(my_history) >= 1 and their_history[-1] == 'b':
      if IncreaseChanceB == True and GreaterIncreaseB == False and p <= 79:
        return 'b'
      elif IncreaseChanceB == False and GreaterIncreaseB == False and p <= 74:
        return 'b'
      elif IncreaseChanceB == True and GreaterIncreaseB == True and p <= 87:
        return 'b'
      elif IncreaseChanceB == False and GreaterIncreaseB == True and p <= 82:
        return 'b'
      else:
        return 'c'

    elif len(my_history) >= 1 and their_history[-1] == 'c':
      if IncreaseChanceC == False and GreaterIncreaseC == False and p <= 64:
        return 'c'
      elif IncreaseChanceC == True and GreaterIncreaseC == False and p <= 69:
        return 'c'
      elif IncreaseChanceC == True and GreaterIncreaseC == True and p <= 77:
        return 'c'
      elif IncreaseChance == False and GreaterIncreaseC == True and p <= 72:
        return 'c'
      else:
        return 'b'
