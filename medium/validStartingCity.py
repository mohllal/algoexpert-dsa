def validStartingCity(distances, fuel, mpg):
    return validStartingCityLinearTimeAndConstantSpace(distances, fuel, mpg)


"""
O(n^2) time and O(1) space
n is the number of cities
"""
def validStartingCityQuadraticTimeAndConstantSpace(distances, fuel, mpg):
    for i in range(0, len(distances)):
        validStartingCity = True
        remainingFuelMiles = 0
        for j in range(i, len(distances)):
            currentFuelMiles = remainingFuelMiles + (fuel[j] * mpg)
            remainingFuelMiles = currentFuelMiles - distances[j]

            if remainingFuelMiles < 0:
                validStartingCity = False
                break

        if validStartingCity == True:
            return i

"""
O(n) time and O(1) space
n is the number of cities
"""
def validStartingCityLinearTimeAndConstantSpace(distances, fuel, mpg):
    milesRemaining = 0

    milesRemainingAtCandidateStartingCity = 0
    candidateStartingCity = 0

    for i in range(1, len(distances)):
        milesRemaining += (fuel[i - 1] * mpg) - distances[i - 1]

        if milesRemaining < milesRemainingAtCandidateStartingCity:
            candidateStartingCity = i
            milesRemainingAtCandidateStartingCity = milesRemaining

    return candidateStartingCity