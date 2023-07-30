"""
O(n) time and O(k) space
n is the length of the competitions array
k is the number of teams
"""
def tournamentWinner(competitions, results):
    scoreboard = {}
    winningScore = 0
    winningTeam = ""

    for i in range(0, len(competitions)):
        [homeTeam, awayTeam] = competitions[i]

        currentWinningTeam = awayTeam if results[i] == 0 else homeTeam
        if currentWinningTeam not in scoreboard:
            scoreboard[currentWinningTeam] = 3
        else:
            scoreboard[currentWinningTeam] += 3

        if scoreboard[currentWinningTeam] > winningScore:
            winningScore = scoreboard[currentWinningTeam]
            winningTeam = currentWinningTeam

    return winningTeam
