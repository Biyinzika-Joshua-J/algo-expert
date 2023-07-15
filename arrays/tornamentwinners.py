# their will always be one tornament winner and atleast 2 teams

def winners(competitions, results): # return the winning team
    standings = {}
    for i in range(len(competitions)):
        competition = competitions[i]
        competitionResult = results[i]
        if competitionResult == 1:
            winner = competition[0]
            if winner not in standings:
                standings[winner] = 0
            standings[winner] += 3
        else:
            winner = competition[1]
            if winner not in standings:
                standings[winner] = 0
            standings[winner] += 3
    greatestScore = 0
    tonarmentWinner = None
    for key, value in standings.items():
        if value > greatestScore:
            greatestScore = value
            tonarmentWinner = key
    return tonarmentWinner

# optimized approach with one loop
# O(n) time and O(K) where n is the number of competitions and K is the number of teams competing in these competitions
def winnersOptimized(competitions, results): # return the winning team
    standings = {}
    greatestScore = 0
    tonarmentWinner = None
    for i in range(len(competitions)):
        competition = competitions[i]
        competitionResult = results[i]
        if competitionResult == 1:
            winner = competition[0]
            if winner not in standings:
                standings[winner] = 0
            standings[winner] += 3
            if standings[winner] > greatestScore:
                greatestScore = standings[winner]
                tonarmentWinner = winner
        else:
            winner = competition[1]
            if winner not in standings:
                standings[winner] = 0
            standings[winner] += 3
            if standings[winner] > greatestScore:
                greatestScore = standings[winner]
                tonarmentWinner = winner
    
   
    return tonarmentWinner



print(winnersOptimized([["HTML", "C#"],["C#", "Python"],["Python", "HTML"]], [0,0,1]))