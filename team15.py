import random 

team_name = 'Blueface Baby, Iiigghht?'
strategy_name=  'heads collude, tails betray, but if they betrayed last, I betray no matter what'
strategy_description = 'We will betray first and then every time after they betray we will collude until they betray twice in a row in which case we will betray.'
    


def move(my_history, their_history, my_score, their_score):

    if len(my_history) == 0:
      return 'b'
    elif len(my_history) >= 1 and their_history[-1] == 'b':
      if len(my_history) >= 3 and their_history[-3] == 'b':
        return 'b'  
      else: 
        return 'c'
    elif len(my_history) >= 98 and their_history[-1] == 'c':
      return 'b'
    else: 
      return 'c'
      
   
   
