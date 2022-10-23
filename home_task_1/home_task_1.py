def arrayRandomCreate():
    import random
    array = [int(random.randint(0, 999)) for i in range(100000)]
    return array


def histogramCreate(array):
    histogram = [0] * 10
    for i in array:
        histogram[int(i / 100)] += 1
    return histogram


import time

calcTime = [0] * 100
sumTime = 0
for i in range(len(calcTime)):
    start = time.time()
    histogramCreate(arrayRandomCreate())
    end = time.time()
    calcTime[i] = end - start
    sumTime += calcTime[i]

print("Минимальное время работы: ", min(calcTime))
print("Максимальное время работы: ", max(calcTime))
print("Среднее время работы: ", (sumTime / len(calcTime)))
