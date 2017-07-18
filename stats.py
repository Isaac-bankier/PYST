###############################
#          stats.py           #
#    Statistics calculator    #
#      By Isaac Bankier       #
###############################

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
    exclusive = list(set(dataSet))
    dictionary = dict.fromkeys(exclusive, 0)
    for data in dataSet:
        dictionary[data] += 1
    answer = sorted(list(map(lambda x: str(dictionary[x])+"|"+str(x), list(dictionary.keys()))))[-1].split("|")[1]
    return answer

options = {"1": mean, "2": median, "3": mode}
choice = input("""Welcome to the statistics calculator. Do you want to do:
1) Find the mean
2) Find the median
3) Find the mode

:""")

function = options[choice]
print(function([1, 2, 3, 4, 4, 4]))
