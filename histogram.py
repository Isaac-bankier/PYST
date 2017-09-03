##############################
#        histogram.py        #
#    generate a histogram    #
#      By Isaac Bankier      #
##############################
 
def histogram(dataSet, symbol="*", gap=0):
    for data in dataSet: # Go through each entry in the list
        print(symbol*data+gap*"\n") # Print it out

histogram([4, 9, 7])
