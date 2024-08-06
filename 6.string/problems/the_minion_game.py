def minion_game(string):
    
    n = len(string)
    total_score = (n*(n+1))//2
    score_kevin = 0
    
    for i, ch in enumerate(string):
        if ch in "AEIOU":
            score_kevin += n - i
            
    score_stuart = total_score - score_kevin
    
    if score_stuart == score_kevin:
        print("Draw")
    elif score_stuart > score_kevin:
        print("Stuart", score_stuart)
    else:
        print("Kevin", score_kevin)


s = input()
minion_game(s)