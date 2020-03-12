team_name = '01'
strategy_name = 'Patterns in their_history'
strategy_description = 'If we colluded and they betrayed last time, betray. If not, then if they have colluded 3 times in a row, betray. If not, then if they have betrayed more than 5 times in the last 10, betray or if they have colluded more than 5 times in the last 10, collude. Otherwise, betray'

def move(my_history, their_history, my_score, their_score):
  returned = False
  #if we colluded and they betrayed last time, betray
  if len(their_history) >= 3:
    if my_history[-1] == 'c' and their_history[-1] == 'b':
      return 'b'
      returned =True
    #if they colluded three times in a row, betray
    elif their_history[len(their_history)-2: len(their_history)+ 1] == 'ccc':
      return 'b'
      returned = True
  #if none of the above are true, check past 10 in history
  if returned == False and len(their_history) >= 10:
    collude_in_history = 0
    betray_in_history = 0
    for i in their_history[len(their_history) -9: len(their_history) + 1]:
      if i == 'c':
        collude_in_history += 1
      elif i == 'b':
        betray_in_history += 1
      #if they colluded more than 5 times in the past ten, collude
      if collude_in_history > 5:
        return 'c'
        returned = True
      #if they betrayed more than 5 times in the past ten, betray
      elif betray_in_history > 5:
        return 'b'
        returned = True
    #if none of these, then betray
  if returned == False:
    return 'b'
