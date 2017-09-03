###############################
#          stats.py           #
#    Statistics calculator    #
#      By Isaac Bankier       #
###############################

def mean(dataSet):
    sum = 0
    for data in dataSet:
        sum += data #Add everything in the list together
    return float(sum) / float(len(dataSet)) #return the sum divided by the length

def median(dataSet):
    dataSetLength = len(dataSet)

    if dataSetLength % 2 == 1: #if not divisable by 2
        medianIndex = dataSet[int(dataSetLength/2)] #return the middle number
    else:  #if divisable by 2
        medianIndex = mean([dataSet[int(dataSetLength/2)-1], dataSet[int(dataSetLength/2)]]) #return the mean of the two middle numbers

    return medianIndex

def mode(dataSet):
    exclusive = list(set(dataSet)) #list of each element in the list. No duplicates.
    dictionary = dict.fromkeys(exclusive, 0) #make a blank list with keys from exclusive
    for data in dataSet:
        dictionary[data] += 1 #count the amount for each item
    answer = sorted(list(map(lambda x: [dictionary[x], x], list(dictionary.keys()))))[-1][1] # find the most common answer
    return answer

options = {"1": mean, "2": median, "3": mode}
choice = input("""Welcome to the statistics calculator. Do you want to:
1) Find the mean
2) Find the median
3) Find the mode

:""")

function = options[choice]
print(function(input("Please enter a comma seperated list: ").split(","))) #Evaluate what they want
