def stringToArray(string):
    return [int(i) for i in (string.split(','))]


def arrayToString(array):
    sumStr = ''
    for i in array:
        sumStr += str(i) + ','
    return sumStr[0:len(sumStr) - 1]


def histDistance(hist1, hist2) -> float:
    from math import sqrt
    sum = 0
    for i in range(len(hist1)):
        sum += (hist1[i] + hist2[i]) ** 2
    return sqrt(sum)


def writeHistToFile(hist1, hist2):
    with open('hist.txt', 'w') as file:
        file.write(arrayToString(hist1) + '\n' + arrayToString(hist2))


def readHistFromFile():
    with open('hist.txt', 'r') as file:
        hist1 = file.readline()
        hist2 = file.readline()
    return stringToArray(hist1[0:len(hist1) - 1]), stringToArray(hist2)


def triangle(a):
    triangleArray = [''] * (a + 1)
    for i in range(a + 1):
        triangleArray[i] = ' ' * (a - i) + '*' * (2 * i + 1)
        print(triangleArray[i])

triangle(5)