team_name = '6/suBcriSis'
strategy_name = 'Alternate'
strategy_description = '''Collude, then alternate.\n'''
    
def move(my_history, their_history, my_score, their_score):
    #Colludes on even numbered rounds (first round is round #0).
    if len(my_history)%2 == 0:
        return 'c'
    else:
        return 'b'
