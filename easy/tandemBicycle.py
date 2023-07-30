"""
O(nlog(n)) time and O(1) space
n is the length of the input speed array
"""
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if fastest:
        blueShirtSpeeds.reverse()
        return calculateTandemSpeed(redShirtSpeeds, blueShirtSpeeds)
    else:
        return calculateTandemSpeed(redShirtSpeeds, blueShirtSpeeds)


"""
O(n) time and O(1) space
n is the length of the input speed array
"""
def calculateTandemSpeed(redShirtSpeeds, blueShirtSpeeds):
    tandemSpeed = 0
    for i in range(0, len(redShirtSpeeds)):
        tandemSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return tandemSpeed