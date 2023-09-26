def validIPAddresses(string):
    return validIPAddressesRecursive(string, 0, '', 0, [])


"""
O(1) time and O(1) space
"""
def validIPAddressesIterative(string):
    ipAddresses = []

    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                firstSegment = string[:i]
                secondSegment = string[i:i+j]
                thirdSegment = string[i+j:i+j+k]
                fourthSegment = string[i+j+k:]

                if (
                    isValidIPAddressSegment(firstSegment) and
                    isValidIPAddressSegment(secondSegment) and
                    isValidIPAddressSegment(thirdSegment) and
                    isValidIPAddressSegment(fourthSegment)
                ):
                    ipAddress = ".".join([
                        firstSegment,
                        secondSegment,
                        thirdSegment,
                        fourthSegment
                    ])
                    ipAddresses.append(ipAddress)

    return ipAddresses


"""
O(1) time and O(1) space
"""
def validIPAddressesRecursive(string, start, currentIp, currentSegment, ipAddresses):
    if currentSegment == 4:
        if start == len(string):
            ipAddresses.append(currentIp)
        return

    for i in range(1, min(4, len(string) - start + 1)):
        segment = string[start:start+i]
        if isValidIPAddressSegment(segment):
            newIp = currentIp + segment if currentSegment == 3 else currentIp + segment + '.'
            validIPAddressesRecursive(string, start + i, newIp, currentSegment + 1, ipAddresses)

    return ipAddresses


def isValidIPAddressSegment(segment):
    return segment and int(segment) <= 255 and len(segment) == len(str(int(segment)))