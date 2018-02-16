myMatrix = [0, 1, 2, 3, 4,
            5, 6, 7, 8, 9,
            10, 11, 12, 13, 14,
            15, 16, 17, 18, 19,
            20, 21, 22, 23, 24]


def lookUp(iVal, bVal):
    if iVal == 0:
        return 0
    for iVal in bVal:
        return iVal * bVal


def printMatrix():
    for i in range(5):
        print ([myMatrix[lookUp(i, b)] for b in range(5)])

printMatrix()
