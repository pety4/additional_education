import sys
import random

import numpy as np


def histDistance(hist1, hist2) -> float:
    from math import sqrt
    sum = 0
    for i in range(len(hist1)):
        sum += (hist1[i] - hist2[i]) ** 2
    return sqrt(sum)

def histogramCreate(array):
    histogram = [0] * 10
    for i in range(len(array)):
        histogram[int(array[i] / 100)] += 1
    return histogram

def writeObject(obj, objHist):
    with open("text.txt", 'a') as f:
        f.write(obj.__class__.__name__ + "\n")
        for x in objHist:
            f.write(str(x) + ' ')
        f.write("\n")

class NNClassifier():
    array = []

    def getData(self):
        with open("text.txt", "r") as f:
            n = 0
            for line in f:
                n += 1
            n = int(n / 2)
            self.array = [["", []]] * n
            f.seek(0, 0)
            for i in range(n):
                self.array[i] = [f.readline(), [float(i) for i in f.readline().split()]]
        return self.array

    def whatClassIsIt(self, objectHist):
        minDistance = sys.float_info.max
        for i in range(len(self.array)):
            self.array[i].append(histDistance(objectHist, self.array[i][1]))
            if (self.array[i][2]) < minDistance:
                minDistance = self.array[i][2]
                answer = self.array[i][0][0:len(self.array[i][0]) - 1]
        return answer
