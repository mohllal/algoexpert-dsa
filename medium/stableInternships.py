"""
O(n^2) time and O(n^2) space
n is the number of interns/teams
"""
def stableInternships(interns, teams):
    freeInterns = list(range(len(interns)))

    teamsInternsRanks = []
    for team in teams:
        ranks = {team[i]: i for i in range(len(team))}
        teamsInternsRanks.append(ranks)

    internsMatched = {}
    teamsMatched = {}

    while len(freeInterns) > 0:
        currIntern = freeInterns.pop()
        currPreferences = interns[currIntern]

        for currTeam in currPreferences:
            if currTeam not in teamsMatched:
                teamsMatched[currTeam] = currIntern
                internsMatched[currIntern] = currTeam
                break
            else:
                currMatchedIntern = teamsMatched[currTeam]
                currTeamInternsRanks = teamsInternsRanks[currTeam]

                if currTeamInternsRanks[currMatchedIntern] > currTeamInternsRanks[currIntern]:
                    teamsMatched[currTeam] = currIntern
                    internsMatched[currIntern] = currTeam
                    freeInterns.append(currMatchedIntern)
                    break

    matches = [[intern, team] for team, intern in teamsMatched.items()]
    return matches