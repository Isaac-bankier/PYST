##############################
#       overlapping.py       #
# If two lists overlap at all#
#      By Isaac Bankier      #
##############################

def overlap(list1, list2):
    result = False

    list1 = list(set(list1))
    list2 = list(set(list2))

    #loop through each member of the list and see if its in the second list.
    #If it is return true
    for member in list1:
        if member in list2:
            result = True

    return result

print(overlap([3, 7], [4, 5, 8]))
