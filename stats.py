import statistics

def mean(dataSet):
    sum = 0
    for data in dataSet:
        sum += data
    return float(sum) / float(len(dataSet))

def median(dataSet):
    dataSetLength = len(dataSet)

    if dataSetLength % 2 == 1:
        medianIndex = dataSet[int(dataSetLength/2)]
    else:
        medianIndex = mean([dataSet[int(dataSetLength/2)-1], dataSet[int(dataSetLength/2)]])

    return medianIndex

def mode(dataSet):
    dataSetLength = len(dataSet)
    dataSetExclusiveLength = len(list(set(dataSet)))

    workingSet = zip(list(set(dataSet))), list(map(int, list("0"*dataSetExclusiveLength)))

    for data in dataSet:
        workingl

options = {"1": mean, "2": median, "3": mode}

choice = input("""Welcome to the statistics calculator. Do you want to do:
1) Find the mean
2) Find the median
3) Find the mode

:""")

function = options[choice]
print(function([1, 2, 3, 4]))
